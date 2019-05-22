from socket import *
import struct
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8110))

# 确定数据结构
st =struct.Struct("i32sif")

# 打开文件
f = open("student.txt",'a')

for i in range(5):
    print(i)
