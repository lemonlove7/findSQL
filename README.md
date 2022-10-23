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

打开Burp Suite-->Extender-->Burp Extensions-->add-->Extension Details(Extension type:python)-->select file(选择findSQL.py)-->打开-->next

<img width="925" alt="image" src="https://user-images.githubusercontent.com/56328995/197371301-45f08d1b-53e8-4369-b91a-d1be0d47e77f.png">

### python运行sqlmapapi.py

找到sqlmap目录，在该目录下使用python运行sqlmapapi.py服务端

```python3 sqlmapapi.py -s```

<img width="670" alt="image" src="https://user-images.githubusercontent.com/56328995/197371414-fa373e22-86d4-4008-a210-3e9d0a94114f.png">

### 运行sql.py

```python3 sql.py```

# 使用效果
这里使用SQLi-LABS进行演示


