# 初识sed和gawk

**学习内容**：

>- 学习sed编辑器
>- gawk编辑器入门
>- sed编辑器基础

shell脚本最常见的一个用途就是处理文本文件，但仅靠shell脚本命令来处理文本文件的内容有点勉为其难。如果我们想在shell脚本中处理任何类型的数据，需要熟悉Linux中的sed和gawk工具。这两个工具可以极大简化我们需要进行的数据处理任务。

## 文本处理

当我们需要自动处理文本文件，又不想动用交互式文本编辑器时，sed和gawk是我们最好的选择。

### sed编辑器

也被称为**流编辑器**（stream editor），会在编辑器处理数据之前**基于预先提供的一组规则**来编辑数据流。

sed编辑器可以根据命令来处理数据流中的数据，这些命令既可以从终端输入，也可以存储进脚本文件中。

sed会执行以下的操作：

- 一次从输入中读取一行数据
- 根据所提供的命令匹配数据
- 按照命令修改流中的数据
- 将新的数据输出到STDOUT

这一过程会重复直至处理完流中的所有数据行。

sed命令的格式如下：

```shell
sed options script file
```

选项`options`可以允许我们修改`sed`命令的行为

| 选项        | 描述                            |
| --------- | ----------------------------- |
| -e script | 在处理输入时，将script中指定的命令添加到已有的命令中 |
| -f file   | 在处理输入时，将file中指定的命令添加到已有的命令中   |
| -n        | 不产生命令输出，使用`print`命令来完成输出      |

`script`参数指定用于流数据上的单个命令，如果需要多个命令，要么使用`-e`选项在命令行中指定，要么使用`-f`选项在单独的文件中指定。

#### 在命令行中定义编辑器命令

默认sed会将指定命令应用到STDIN输入流上，我们可以配合管道命令使用。

```shell
wsx@wsx-laptop:~/tmp$ echo "This is a test" | sed 's/test/big test/'
This is a big test
```

`s`命令使用斜线间指定的第二个文本来替换第一个文本字符串模式（注意是替换整个模式，支持正则匹配），比如这个例子用`big test`替换了`test`。

假如有以下文本：

```shell
wsx@wsx-laptop:~/tmp$ cat data1.txt
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
```

键入命令，查看输出

```shell
wsx@wsx-laptop:~/tmp$ sed 's/dog/cat/' data1.txt
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
The quick brown fox jumps over the lazy cat.
```

可以看到符合模式的字符串都被修改了。

要记住，sed并不会修改文本文件的数据，**它只会将修改后的数据发送到STDOUT**。

#### 在命令行上使用多个编辑器命令

使用`-e`选项可以执行多个命令

```shell
wsx@wsx-laptop:~/tmp$ sed -e 's/brown/green/; s/dog/cat/' data1.txt
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
```

