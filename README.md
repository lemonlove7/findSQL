# findSQL
查找可能存在注入的点，目前只支持get类型的注入
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
打开Burp Suite-->Extender-->
