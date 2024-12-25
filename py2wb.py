import os
import sys
import shutil
from pathlib import Path
# from header import get_header
from data.wubi86yd import get_wubi86yd

wubi86yd = get_wubi86yd()

def convert(SRC_DIR, OUT_DIR, FILE_ENDSWITH_FILTER):
	# 遍历源文件夹文件，处理
	for file_path in SRC_DIR.iterdir():
		if file_path.is_file():
			file_name = file_path.name
			# print(file_name)
			if not file_name.endswith(FILE_ENDSWITH_FILTER):
				continue
			print(file_name)

			src_file_path = SRC_DIR / file_name
			out_file_path = OUT_DIR / file_name
			
			# 添加词库头
			# with open(out_file_path, 'a', encoding='utf-8') as o:
			#     o.write(get_header(file_name))


			with open(src_file_path, 'r', encoding='utf-8') as f:
				num = 0			# 统计文件中不包含在 wubi86yd 中的字的行数
				res = ''		# 生成的词库串
				res_dict = {}
				count = 0		# 统计文件中词组包含非文字行的数量

				for line in f.readlines():
					if line.startswith(('#', ' ', '\n', '-', '.', 'n', 'v', 's', 'c', 'u')):    # 忽略非词表行处理
						res = res + line
					else:
						line_arr = line.strip().split('\t')

						word = line_arr[0]
						# pinyin = line_arr[1]
						pinyin = ''
						weight = (len(line_arr) > 2 and line_arr[2]) or ''

						# 统计并列出文件中词组包含的非文字行
						ctn = False
						for w in word:
							if w in (('·','(',')','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
								count = count + 1
								print(f'{count} - {line.strip()}')
								ctn = True
						if ctn:
							continue

						# 对字词进行遍历处理并组合成五笔字库结构
						if len(word) == 1:
							# ^ 单字情况
							if wubi86yd.get(word):
								res = res + f'{word}\t{wubi86yd[word]}\t{pinyin}{weight}\n'
							else:
								num = num + 1
								print(f'{num} - {word}')
								res = res + f'{word}\txxxx\t{pinyin}{weight}\n'
						elif len(word) == 2:
							# ^ 2字词
							for w in word:
								if not wubi86yd.get(w):
									num = num + 1
									print(f'{num} - {word}')

							res = res + f'{word}\t{wubi86yd[word[0]][:2]}{wubi86yd[word[1]][:2]}\t{pinyin}{weight}\n'
						elif len(word) == 3:
							# ^ 3字词
							for w in word:
								if not wubi86yd.get(w):
									num = num + 1
									print(f'{num} - {word}')

							res = res + f'{word}\t{wubi86yd[word[0]][0]}{wubi86yd[word[1]][0]}{wubi86yd[word[2]][:2]}\t{pinyin}{weight}\n'
						elif len(word) >= 4:
							# ^ 4+字词
							for w in word:
								if not wubi86yd.get(w):
									num = num + 1
									print(f'{num} - {word}')

							res = res + f'{word}\t{wubi86yd[word[0]][0]}{wubi86yd[word[1]][0]}{wubi86yd[word[2]][0]}{wubi86yd[word[len(word) - 1]][0]}\t{pinyin}{weight}\n'

				
				# for key, value in res_dict.items():
				# 	res = res + f'{key}\t{value}\n'


				with open(out_file_path, 'w', encoding='utf-8') as o:
					o.write(res)


if __name__ == '__main__':
	current_dir = Path.cwd()
	src_dir = current_dir / ((len(sys.argv) > 1 and sys.argv[1]) or 'cn_dicts_cell')			# 设置待处理的拼音词库文件夹
	out_dir =  current_dir / ((len(sys.argv) > 2 and sys.argv[2]) or'out/cn_dicts_cell')		# 转换后输出的五笔词库文件夹
	file_endswith_filter = (len(sys.argv) > 3 and sys.argv[3]) or 'dict.yaml'
	# 如果存在输出文件，先删除
	if os.path.exists(out_dir):
		shutil.rmtree(out_dir)
	os.mkdir(out_dir)

	convert(src_dir, out_dir, file_endswith_filter)
