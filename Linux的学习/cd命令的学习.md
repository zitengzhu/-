**cd切换工作目录**

**当Linux终端(命令行)打开的时候，会默认以用户的HOME目录为当前的工作目录**

**我们可以通过cd命令，更改当前所在的工作目录**

**语法:cd\[Linux路径]**

**cd命令无需选项，只有参数，表示要切换到哪个目录下**

**cd命令直接执行，不写参数，表示回到用户的HOME目录**



**示例：**

\[zzt@localhost ~]$ ls  #当前工作目录为HOME目录

公共  模板  视频  图片  文档  下载  音乐  桌面

\[zzt@localhost ~]$ cd /  #使用cd命令将工作目录改为根目录

\[zzt@localhost /]$ ls 

afs  boot  etc   lib    media  opt   root  sbin  sys  usr

bin  dev   home  lib64  mnt    proc  run   srv   tmp  var

\[zzt@localhost /]$ cd  # cd命令不写参数将工作目录切换回HOME目录

\[zzt@localhost ~]$ ls

公共  模板  视频  图片  文档  下载  音乐  桌面





