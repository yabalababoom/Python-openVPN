# Python-openVPN-自动填写密码+自动添加代码到配置文件

# 2021/7/17  第一版

有些openvpn配置文件需要自动填写密码,网上搜到的方法是在配置文件中添加一行'auth-user-pass pass.txt',在配置文件所在目录新建pass.txt,第一行填写账号,第二行填写密码。这种方法免于了每次连接时的手动输入，但是仍然要在配置文件中添加'auth-user-pass pass.txt'，有点麻烦。
最近新学了Python，利用代码实现 在ovpn配置文件中添加'auth-user-pass pass.txt'




# 2021/7/18  第二版

1.改进了对ovpn文件同目录下文件的分类,只有ovpn文件需要添加密码行
2.若ovpn文件文件最后一行已有'auth-user-pass pass.txt',则跳过,否则添加
