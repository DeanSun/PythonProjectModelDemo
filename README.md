## 程序目录结构说明
+ **demo**
   + 该目录是用来放置python程序使用的   
   + `__init__.py`   
   这个是让程序认定该部分是一个py包，必须要有的文件   
   ps:暂时先设定为空，到时候所有程序进行统一处理 
+ **docs**  
   + 包的参考文档
+ **script**    
   + 该目录是用来添加部分可执行脚本程序的
+ **test**
   + 该目录是用来添加测试文件的
+ **requirements.md**
  + 该文件内为需要加入一下项目依赖的py程序，这个不用开发者来处理，管理员会定期进行更新
+ **setup.py**
   + 打包和发布管理   
   ps: 暂时先不进行处理
---
## 程序环境说明
+ python版本需要使用 3.x(3.7以上) 版本

## 环境安装与设置
+ python 下载
  + windows:https://www.python.org/downloads/windows/
  + LINUX/UNIX:https://www.python.org/downloads/source/
  + MacOS:https://www.python.org/downloads/mac-osx/
  + other:https://www.python.org/download/other/
+ pip 
  + python 3.4+ 版本自带此工具
  + pip更新语句   
  window:   
  `python -m pip install -U pip`   
  Linux or macOS:   
  `pip install -U pip`
  
  
 + python 环境打包命令    
 `python setup.py sdist --formats=gztar,zip`
