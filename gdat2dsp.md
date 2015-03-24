# Introduction #

[gdat2dsp](gdat2dsp.md) 是 [DASPIO](DASPIO.md) 的子模块[ary2dsp](ary2dsp.md)的功能示例，它可以用来将文本文件转换为DASP的tsp文件和sts文件，不保证这一过程与DASP的转换完全一致。不过它的速度应该比DASP的本身实现快很多，特别是当转换的文件来自有限元模型的输出结果的时候（这是该模块的设计背景）。

# Details #

[gdat2dsp](gdat2dsp.md) 相较于DASP提供的转换程序是相当迅速的。下面我们看一下这一程序的使用方法：

该程序使用guidata开发的，代码非常简单。界面实际就是个输入窗口，如下图所示

![http://viblab.googlecode.com/svn/wiki/begin.png](http://viblab.googlecode.com/svn/wiki/begin.png)

在上图中相应位置填写相应内容后点击确定就可以进行转换了。信息不全的部分用桔黄色标识出来了，如果在信息不全的情况下点击确定那么程序将给出提示。

![http://viblab.googlecode.com/svn/wiki/error.png](http://viblab.googlecode.com/svn/wiki/error.png)

请注意：很多默认值可能是适合给定文件的实际情况，请仔细核对。

在程序开始转换前，程序会将输入再次打印出来，请仔细核对各项参数是否正确。

![http://viblab.googlecode.com/svn/wiki/view.png](http://viblab.googlecode.com/svn/wiki/view.png)

上述窗口关闭后转换就开始了，一般的有限元计算文件应该可以在几秒钟内完成转换。

# Note #

该程序的命令行版本[dat2dsp](dat2dsp.md)可以批量的完成本程序的功能，如需要可以下载[dat2dsp](dat2dsp.md)的命令行版本。