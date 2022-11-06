import os,time
import socket
import time
import json
import requests
import threading


def test():
    while True:
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server_socket.bind(('127.0.0.1', 6666))
        tcp_server_socket.listen(64)
        client_socket, clientAddr = tcp_server_socket.accept()
        recv_data = client_socket.recv(1024)
        u = recv_data.decode('utf-8')
        client_socket.close()
        payload = {'url': u}

        resp = requests.get('http://127.0.0.1:8775/task/new')
        taskid = resp.json()['taskid']

        headers = {'Content-Type': 'application/json'}
        if resp.json()['success']:
            url = "http://127.0.0.1:8775/option/%s/set" % taskid
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            if resp.json()['success']:
                url = "http://127.0.0.1:8775/scan/%s/start" % taskid
                resp = requests.post(url, data=json.dumps(payload), headers=headers)
                if resp.json()['success']:
                    taskids.append(taskid)
        else:
            print("new task error")


def st():
    while True:
        for taskid in taskids:
            time.sleep(1)
            url = "http://127.0.0.1:8775/scan/%s/status" % taskid
            resp = requests.get(url)
            if resp.json()['status'] != 'terminated':
                pass
            else:
                url = "http://127.0.0.1:8775/scan/%s/data" % taskid
                data = requests.get(url)
                if data.json()['data']:
                    member = [members.get('value') for members in data.json().get('data')]
                    hh=member[0]
                    existence_url=hh.get('url')
                    existence_query=hh.get('query')
                    print('[+] 存在注入 url:'+existence_url+' 参数:'+existence_query)
                url = "http://127.0.0.1:8775/task/%s/delete" % taskid
                requests.get(url)
                taskids.remove(taskid)
        time.sleep(3)



if __name__ == '__main__':
    print("By T00ls.Com")
    taskids=[]
    threads=[]
    threads.append(threading.Thread(target=test))
    threads.append(threading.Thread(target=st))
    for t in threads:
        t.start()



