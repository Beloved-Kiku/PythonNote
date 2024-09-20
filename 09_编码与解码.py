# 任何数据在我们计算机内部都是采用二进制存储的
# 我们在计算机上看到的文字，图片，音频，视频等数据，都是二进制数据经过编码后显示出来的
print('abc'.encode('utf-8'))  # 将字符串abc编码成utf-8格式 三个字节 一个字母一个字节
print('啊'.encode('utf-8'))  # 将字符串啊编码成utf-8格式 一个汉字三个字节
print('啊'.encode('gbk'))  # 将字符串abc编码成gbk格式 一个汉字两个字节
# 在python3中我们的字符串采用的编码方式是unicode编码,在计算机内部存储的时候，会先将其转换成utf-8编码，然后再存储
# ASCII码地址:https://www.asciitable.com/