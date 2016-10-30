# DocUtil
A Simple automatic document generate tool for markdown user.

---

这是一款基于Python实现的自动化的文档生成工具。简单高效！

专门为Markdown语法文档编写者制作的Markdown 文件转换为HTML文件自动化工具。

## 使用方式

由于是基于Python实现的，所以需要有Python环境的支持。

### 清理public文件夹下的旧的html文件
> python Entrance.py -c clean

### 基于source文件夹里面的.md源文件重新生成html文件，并输出到public文件夹下
> python Entrance.py -g generate


## 缺点

模板文件使用的不够彻底，私人定制性不够强。还有就是生成html文件的时候代码的耦合性太强，这样非常的不好！

下一个版本将进行大面积的重构，以达到较好的使用效果。

## 关于release

这里新增了一个release文件夹，内包含一个md2html.exe的小工具，可以方便的将单个的markdown源文件

转换成html文件，具体请参照word使用文档。

## 后续的话

如果你看到了这句话，说明我的1.0版本还没有彻底的升级。当然了你也可以修改源代码来适配你的审美。
我会不定期的对此工具进行优化的，有兴趣的话可以给我提issue。

如果你对此也很有兴趣，不妨fork一下咯。
