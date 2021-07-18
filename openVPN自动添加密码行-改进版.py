# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 16:21
# @Author  : 

"""将指定目录下的ovpn文件的最后添加一行 auth-user-pass pass.txt,实现openvpn的免输入登录
"""
import os
from os.path import abspath

"""ovpn所在目录=D:\\Desktop\\openvpn 备份  \要写成\\  转义字符""" 

ovpn_list=['ovpn所在目录']  #将存放ovpn的文件夹目录放入列表ovpn_list中
ovpn_dir = os.listdir(ovpn_list[0])  # 返回该文件夹目录路径下的文件,存储在列表ovpn_dir中
# print('该目录下的文件有:',ovpn_dir)
# print('_______________________________')

lst=[]  # 定义一个空列表,用于存放ovpn_list目录下每个文件的位置信息

for item in ovpn_dir:  # 遍历ovpn_dir
    olst = os.path.join('ovpn所在目录', item)  # 将ovpn文件与其父目录拼接成一个绝对路径
    d=os.path.splitext(olst)  # 分离文件名和扩展名
    if d[1] == '.ovpn':  # 判断扩展名是否为ovpn; 若是 则添加到列表lst中
        lst.append(olst)

# print('其中ovpn文件有:',lst)

for i in lst:  # 遍历列表lst,在lst列表中的每个ovpn文件的最后添加一行 'auth-user-pass pass.txt'
    with open(i, 'r') as f:   # 读取ovpn文件最后一行的信息 如果存在'auth-user-pass pass.txt' 则继续遍历下一个文件,否则 添加
        lines = f.readlines()  # 读取所有行
        # first_line = lines[0]  # 取第一行
        last_line = lines[-1]  # 逆序取最后一行
        # print('文件' + i + '第一行为：' + first_line)
        # print('文件' + i + '最后一行为：' + last_line)
        print(last_line)

        if last_line != 'auth-user-pass pass.txt':
            with open(i, 'a') as f:
                f.write('auth-user-pass pass.txt')
        else:
            continue
print('结束')


