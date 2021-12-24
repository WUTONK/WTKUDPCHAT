import socket
from threading import Thread
import hashlib
import re
import time

# 创建套接字
main_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def main():
    license()


def listen():

    while 1:
       pass


    # 关闭服务器
    

def encrypt_psw(str):
    """
    使用 MD5 算法对用户的密码进行加密
    :param str: 待加密的密码字符串
    :return: 加密后的密码字符串
    """
    hl = hashlib.md5()
    hl.update(str.encode("utf-8"))  # 必须编码后才能加密
    return hl.hexdigest()

def check_user(username, encrypted_psw):
    
    #打开用户列表
    with open("./usrlist.txt", "r") as users_file:
        users_data = users_file.read()
    users_list = users_data.split()
    for user in users_list:
        if user == username:
            # 获得对应用户名的密码在列表中的索引
            index = users_list.index(user) + 1 #加1将指针移动到该用户名的密码
            if users_list[index] == encrypted_psw:
                return "登录成功！"
            else:
                return "密码输入有误，请重新输入！"
    else:
        return "不存在该用户，请先注册！"


if __name__ == "__main__":
    main()