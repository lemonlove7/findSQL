#coding=utf-8
import os
import time
from burp import IBurpExtender
from burp import IProxyListener
import sys
import socket

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
sql_dict=['?id=','?page=','?dir=','?search=','?category=','?file=','?class=','?url=','?news=','?item=','?menu=','?lang=','?name=','?ref=','?title=','?view=','?topic=','?thread=','?type=','?date=','?form=','?join=','?main=','?nav=','?region=']

class BurpExtender(IBurpExtender,IProxyListener):
    def registerExtenderCallbacks(self,callbacks):
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("FindSQL v1.0")
        print('''
        [+] findSQL scan is loaded
        [+] ^_^
        [+] #####################################
        [+] findSQL v1.0
        [+] author:刘一手
        [+] team:鹏组安全
        [+] By T00ls.Com
        [+] github:https://github.com/lemonlove7/findSQL
        [+] #####################################
        [+] Please enjoy it
        ''')
        callbacks.registerProxyListener(self)
    def processProxyMessage(self,messageIsRequest,message):
        if not messageIsRequest:
            RepReq = message.getMessageInfo()
            url=RepReq.getUrl()
            Rep_B = RepReq.getResponse()
            Rep = self._helpers.analyzeResponse(Rep_B)
            for i in sql_dict:
                if i in str(url):
                    if 'baidu.com' in str(url):
                        break
                    if 'csdn.net' in str(url):
                        break
                    Status_code=Rep.getStatusCode()
                    Length=Rep.getHeaders()
                    Lengths = "".join(Length)
                    if 'Content-Length' in Lengths and str(Status_code)=='200':
                        tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tcp_client_socket.connect(('127.0.0.1', 6666))
                        send = str(url)
                        tcp_client_socket.send(send.encode("utf-8"))
                        feedback = tcp_client_socket.recv(1024)
                        feedback.decode('utf-8')
                        tcp_client_socket.close()
                        break
