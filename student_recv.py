from socket import *
import struct
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8110))

# 确定数据结构
st =struct.Struct("i32sif")

# 打开文件
f = open("student.txt",'a')

while  True:
    data,addr =s.recvfrom(1024)
    data =st.unpack(data)
    print(data)
    info = "%d  %s  %d  %.2f\n"%(data[0],data[1].decode(),data[2],data[3])
    f.write(info)
    print(info)

s.close
f.close
