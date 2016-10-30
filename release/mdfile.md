[toc]

继上次的那个Python程序打包成windows下可执行的小工具，接连收到了许多小伙伴关于如何打包的疑问，这里简单的做下总结。

---

## 准备

关于pyinstaller，需要了解的就是它不是一个库，而是一个工具，一个可以将你的.py程序打包成windows下可以执行的exe文件。

### 依赖

pyinstaller依赖于pywin32，所以在下载pyinstaller之前，应该确保自己的电脑上安装了适配于自己电脑系统的pywin32。

详见：
> http://www.softpedia.com/get/Programming/Other-Programming-Files/PyWin32.shtml#download


### pyinstaller下载

第二步就是下载这个工具了。

> http://www.pyinstaller.org/

官网的右侧有下载的链接，找到合适的版本，下载即可。目前最新版本为3.2，相比于2.X版本，已经fixed了很多的bug了。



## 语法

总的来说，这个工具还是很人性化的，这也让我们有很多的选择空间。下载完刚才的那个工具后，随便解压到一个文件夹即可。

### 核心命令

> python pyinstaller.py [opt] target_python_file

对于[opt]可选命令，就是通过制定不同的参数来实现不同的打包方式。

### 可选项

 - `-F , -onefile`:    指明该选项，将会生成一个总的exe文件，所有的文件都会被添加到这一个中。

 - `-D, -onedir`:  产生一个目录来盛装用于分发的exe文件，也比较方便。

 - `-K, -tk`：  在部署的时候，包含TCL/TK，这对于有图形界面的python文件比较的适用。

 - `-a, -ascii`: 不包含编码，因为在支持Unicode的Python版本上默认包含所有的编码，这个选项基本上不怎么用得到。

 - `-d, -debug`:  产生Debug版本的可执行文件。

 - `-w, -windowed, -noconsole`: 适用Windows子系统执行，当exe文件运行的时候，不会出现命令行CMD窗口。（因为是windows子系统，所以只在windows平台下有效。）

 - `-c, -nowindowed, -console`: 与上相反，出现CMD窗口，辅助用户操作。

 - `-s, -strip`:  这个参考别人的话为“可执行文件和共享库将run through strip，注意Cygwin的strip往往使得普通的win32DLL无法使用”。

 - `-X, -upx`:  压缩方式，如果有UPX安装，则会压缩源文件来执行。

 - `-o DIR, -out=DIR`:  指定DIR作为exe的生成目录，如果未指定，默认为pyinstaller的解压目录，且会根据python文件创建出同名的目录来保存生成的exe文件。

 - `-p, DIR, -path=DIR`:  设置导入的环境变量路径，windows下英文的分号分隔，也可以使用多个`-p`选项来设置导入多个路径（其实这个选项有点鸡肋，分发版的话基本上不怎么用得到）。

 - `-icon=<FILE.ICO>`: 将file.ico添加为exe文件的图标（可以自定义，注意为ico文件，否则格式不正确的话会出错的）。

 - `-icon = <FILE.EXE, N>`: 原理同上（只是把file.exe文件的第N个图标作为资源来使用，不怎么用得到）。


## 实战

说了这么多，还是来点实际的吧。

```
#include "stdio.h"
main()
{
　for(j=1;j<10;j++)
　{
　　 result=i*j;
　　 printf("%d*%d=%-3d",i,j,result);/*-3d表示左对齐，占3位*/
　}
}
```