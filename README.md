# copy_gallery-dl 说明文档
`copy_gallery-dl`是一个配合`gallery-dl`运作，在`gallery-dl`下载图片之后把下载的图片文件发送到剪贴板的小工具。
## 快速开始
```
copy_gallery-dl [options] <url1> <url2> ...
```
`copy_gallery-dl`会将所有接收到的参数全部传给`gallery-dl`，所以用法和`gallery-dl`是一样的。

## 注意事项
 1. 首先安装和配置好`gallery-dl`，简单的中文配置教程可以看我写的这篇[专栏](https://www.bilibili.com/read/cv25014520)。
 2. `copy_gallery-dl`会寻找三个地方的`gallery-dl`：同一目录下的`gallery-dl.exe`、配置文件`config.json`中的文件路径和环境变量中的`gallery-dl`。
 3. 当`copy_gallery-dl.exe`和`gallery-dl.exe`在同一文件夹下时，优先使用同一文件夹下的`gallery-dl.exe`。
 4. 当`copy_gallery-dl.exe`所在的目录下存在`config.json`时，读取`config.json`中的`gallery-dl`文件路径。
 5. 当既不在同一文件夹下、也没有配置配置文件时，默认使用环境变量里的`gallery-dl`。
 6. 注意不要让`copy_gallery-dl`和`gallery-dl`的配置文件有冲突。推荐把`gallery-dl`的配置文件保存为`gallery-dl.conf`，`copy_gallery-dl`的配置文件名为`config.json`并一定要和`copy_gallery-dl.exe`在同一目录下。
 7. 无论哪个配置文件，windows路径里的反斜杠`\`一定全都要换成`/`正斜杠。
## 配置文件
`copy_gallery-dl`会读取同一目录下的`config.json`文件，配置文件格式如下：
```
{
    "gallery_path": "G:/安装包/gallery-dl.exe"
    }
```

在我提供的压缩包内我提供了`config.json`的范例文件，请根据自身需要修改。

我还提供了`gallery-dl`的配置文件`gallery-dl.conf`，请配合上文里的专栏进行修改，这里不再赘述。
### 再次强调
* 在修改路径时一定要把反斜杠`\`全部换成`/`正斜杠

