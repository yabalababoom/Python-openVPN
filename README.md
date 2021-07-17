# Python-openVPN-自动填写密码+自动添加代码到配置文件
有些openvpn配置文件需要自动填写密码,网上搜到的方法是在配置文件中添加一行'auth-user-pass pass.txt',在配置文件所在目录新建pass.txt,第一行填写账号,第二行填写密码。这种方法免于了每次连接时的手动输入，但是仍然要在配置文件中添加'auth-user-pass pass.txt'，有点麻烦。
最近新学了Python，利用代码实现 在ovpn配置文件中添加'auth-user-pass pass.txt'
2021/7/17  第一版

"""将指定目录下的ovpn文件的最后添加一行 auth-user-pass pass.txt,实现openvpn的免输入登录
"""
import os
from os.path import abspath

ovpn_dir = os.listdir('ovpn配置文件所在目录')  # 返回该路径下的文件和目录信息,存储在列表ovpn_dir中
# print(ovpn_dir)

lst=[]  # 定义一个空列表,用于存放ovpn文件位置信息

for item in ovpn_dir:  # 遍历ovpn_dir ,将ovpn文件和父目录拼接成一个绝对路径,并存放在lst列表中
    olst = os.path.join('ovpn配置文件所在目录', item)
    lst.append(olst)
# print(lst)


for i in lst:  # 遍历列表,在列表中的每个ovpn文件的最后添加一行 auth-user-pass pass.txt
    with open(i, 'a') as f:
        f.write('auth-user-pass pass.txt')
有待改进，比如"ovpn配置文件所在目录",可以存放在一个列表内,输入一次就行,以后再改吧.
