➭ 详细说明 [一种获取五笔大词库的方式](https://aituyaa.com/%E4%B8%80%E7%A7%8D%E8%8E%B7%E5%8F%96%E4%BA%94%E7%AC%94%E5%A4%A7%E8%AF%8D%E5%BA%93%E7%9A%84%E6%96%B9%E5%BC%8F/) 

该五笔大词库是基于极爽词库和白霜拼音转换而来的，没有具体统计数量，估计有个一两百万条吧 ~ 转换的同时，保留了原始词频，所以并不用担心重码问题。

**如果感觉还是不够大，怎么办？**

在仓库中我们附上了制作的 Python 转换脚本 - [py2wb.py](https://github.com/loveminimal/rime-frost-wubi-dict/blob/master/py2wb.py)，你只需要执行它，就可以自己将现在拼音词库转换五笔词库了。

```
# py py2wb.py [拼音词库所在目录] [五笔词库输出目录] [拼音词库目录文件筛选]
py py2wb.py src out 8105.dict.yaml
```

带 `[]` 中的参数都是可选的，但输入顺序不能乱。其中通过 `[拼音词库目录文件筛选]` ，你可以实现筛选转换的拼音词库文件，默认为 `.dict.yaml` 。