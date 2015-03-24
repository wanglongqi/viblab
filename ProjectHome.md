![http://viblab.googlecode.com/svn/trunk/viblab.png](http://viblab.googlecode.com/svn/trunk/viblab.png)

本项目包括实际工作中遇到的，本人使用业余时间和部分工作时间完成的程序模块。程序包括以下几个部分：

  * 与DASP的数据交换，包括输入输出DASP格式文件，部分代码还在整理过程中
  * 绘图功能，对振动信号的时域、谱、相关函数等等进行绘图
  * 时域分析功能，这部分包括一些时域特性的分析，特别是统计特性的分析，这些模块大多是需要使用时完成的。
  * 其他功能，其他辅助性的模块

谱分析功能，网上现成的代码很多，协议问题就不放到网上了，不过嵌入进去并不是很困难。

现在整个项目还处于很初级的阶段，大部分模块不提供下载，项目的代码可以使用SVN获取，详见Source选项卡。由于本项目大部分代码是基于Python的，而且现在的设计也是仅做到Python模块为止，当然最终可能会将这些模块汇集成一个GUI或者命令行可执行文件，不过短期内可能该项目都是单个模块单个模块的发布。对于那些需要使用这些模块的人们来说，可能需要安装Python和相应用到的库（比如：numpy和scipy等），对此我深表歉意。

现在 **仅在SVN源中提供下载** 的模块包括:
  * [weighting](weighting.md): 提供国际标准ISO2631-1:1997中的Wk计权的计算（对应国标GB/T13441.1中的Wk计权），其他几个计权方式由于暂时不需要所以没有提供。该计权程序可以用来进行Z振级的计算。
  * [vibstat](vibstat.md): 提供振动信号多个方面的统计信息的计算，包括峰值，有效值，VDV，振级，Z振级，峰值系数等等。
  * [spec](spec.md): 导入Thomas Cokelaer的谱分析库，可进行周期图，AR，Eig，Music等等多种参数和非参数谱分析。
  * [window](window.md): 导入Scipy的窗函数库，可进行针对谱分析的各种加窗操作。
  * [dsp2hdf](dsp2hdf.md), [hdf2dsp](hdf2dsp.md)： DASP文件格式到HDF5格式之间的相互转换功能。
  * [dsp2ary](dsp2ary.md), [ary2dsp](ary2dsp.md)：DASP文件读入输出Python环境的接口程序，该程序模块是DASPIO的核心。
  * [daspfilename](daspfilename.md): 使用树状结构管理DASP测试文件的类，方便联合其他分析工具使用。
  * [gdat2dsp](gdat2dsp.md): 将文本文件转换为DASP数据文件，仅仅为了方便操作使用，模块的功能在[ary2dsp](ary2dsp.md)中实现，该模块可能仅实现了部分DASP的数据格式。

该项目的模块都比较缺乏说明，有时间的话我会对项目的代码做个说明，不过这可能需要过一段时间。

如果你对这个项目感兴趣，你可能对http://code.google.com/p/abaqus-helper也会感兴趣，那个项目可以将本项目输出的结果结合到Abaqus的计算中去。


---


欢迎大家和我联系，大家共同学习共同提高啦！

软件的协议问题我还没有搞太明白，不过我不是很介意使用GPL协议发布，这个我再研究研究吧。
