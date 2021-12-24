from tkinter import *
import socket
import time
from tkinter import messagebox
from threading import Thread
import re

class Client:

    def __init__(self):
        # 创建套接字
        self.Client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # 绑定端口号
        self.Client_socket.connect(("",7788)) #空双引号是因为电脑会自动检测到自己的IP 地址,所以不用填写

    def send_login_info(self, password_str):

        # 告诉服务器本次请求的类型，“1” 是验证登录
        self.Client_socket.sendall("1".encode("utf-8"))
        usrname = password_str[0]
        password = password_str[1]   
        print (usrname,password)

        # 将用户名和密码按照一定规律组合后一起发送给服务器
        usrname_psw = usrname + "#$#$" + password
        self.Client_socket.sendall(usrname_psw.encode("utf-8"))

class LoginPanel:

    #初始化用户名和密码
    def __init__(self):
        self.usrname = ""
        self.password = ""

    def inputpassword(self):
        usrname = str(input("请输入用户名:"))
        password = str(input("请输入密码:"))

        return usrname, password


def main():
    #将登陆输入函数实例化
    login_input = LoginPanel()
    password_str = login_input.inputpassword()
    print(password_str)
    list(password_str)
    print(password_str)

    #将客户端类实例化
    Clt = Client()
    Clt.send_login_info(password_str)

def send_register_info(self, username, password, confirm):
        """
        发送用户注册的用户名和密码给服务器，并返回注册结果
        :param username: 待注册的用户名
        :param password: 待注册的密码
        :param confirm: 确认密码
        :return: 注册结果
        """
        # 判断两次输入的密码是否一致
        if not password == confirm:
            return "密码不一致，请重新输入！"
        # 告诉服务器本次请求类型，“2” 是注册用户
        self.client_socket.sendall("2".encode("utf-8"))

        # 将用户名和密码按一定规律组装后发送给服务器
        username_psw = username + "#!#!" + password
        self.client_socket.sendall(username_psw.encode("utf-8"))

        # 获取服务器返回的结果
        check_result = self.client_socket.recv(1024).decode("utf-8")
        return check_result
if __name__ == "__main__":
    main()