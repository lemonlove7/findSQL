# findSQL
在日常渗透中，手工检测注入点变得繁琐，用过sqlmap4burp++.0.2这个插件，很好用，但是要人工去识别是否可能存在注入点然后右键发送到sqlmap中进行检测，还是有点不方便

于是乎就想着节省时间写了这个，目前还是不是很完善，大佬轻喷

# 功能
burp开启代理模式，对流量进行检测，联动sqlmapapi自动查找可能存在注入的点，目前只支持get类型的注入检测
# 用法
注意:路径中不要有中文字符，否则会报错
### 安装Jython

需要先在burp中安装Jython
Jython下载地址: https://www.jython.org/download.html

在下载页面选择Jython Standalone 将jython的jar包下载下来

<img width="1135" alt="image" src="https://user-images.githubusercontent.com/56328995/197370668-5d31248a-9465-4afd-90d5-877b1a61a2fa.png">

打开Burp Suite-->Extender-->选中Option-->Python Environment的配置项-->点击Select file-->选中下载的jython-standalone-2.7.1.jar文件

<img width="869" alt="image" src="https://user-images.githubusercontent.com/56328995/197370847-9a9a92d8-6e06-4eb9-a312-c5c4c441ba74.png">

### 导入findSQL.py

打开Burp Suite-->Extender-->Burp Extensions-->add-->Extension Details(Extension type:python)-->select file(选择findSQL.py)-->打开-->next

<img width="782" alt="33" src="https://user-images.githubusercontent.com/56328995/200166398-1b226e41-6bd1-42fe-8a96-55066d824bdd.png">

### python运行sqlmapapi.py

找到sqlmap目录，在该目录下使用python运行sqlmapapi.py服务端

```python3 sqlmapapi.py -s```

<img width="670" alt="image" src="https://user-images.githubusercontent.com/56328995/197371414-fa373e22-86d4-4008-a210-3e9d0a94114f.png">

### 运行sql.py

```python3 sql.py```

# 使用效果
这里使用SQLi-LABS进行演示

<img width="1272" alt="66" src="https://user-images.githubusercontent.com/56328995/200166411-9bf565b7-a996-44a3-99f4-57b6ec75aea6.png">

检测出存在注入
