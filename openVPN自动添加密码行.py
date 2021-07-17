# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 16:21
# @Author  : 

"""将指定目录下的ovpn文件的最后添加一行 auth-user-pass pass.txt,实现openvpn的免输入登录
"""
import os
from os.path import abspath

ovpn_dir = os.listdir('C:\\Users\\Yong Huan\\Downloads\\Telegram Desktop\\OpenVPN-Collection-(@proSSH)\\ExpressVPN-(@proSSH) 143')  # 返回该路径下的文件和目录信息,存储在列表ovpn_dir中
# print(ovpn_dir)

lst=[]  # 定义一个空列表,用于存放ovpn文件位置信息

for item in ovpn_dir:  # 遍历ovpn_dir ,将ovpn文件和父目录拼接成一个绝对路径,并存放在lst列表中
    olst = os.path.join('C:\\Users\\Yong Huan\\Downloads\\Telegram Desktop\\OpenVPN-Collection-(@proSSH)\\ExpressVPN-(@proSSH) 143', item)
    lst.append(olst)
# print(lst)


for i in lst:  # 遍历列表,在列表中的每个ovpn文件的最后添加一行 auth-user-pass pass.txt
    with open(i, 'a') as f:
        f.write('auth-user-pass pass.txt')
