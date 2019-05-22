from socket import *
import struct

ADDR = ('127.0.0.1',8110)
st = struct.Struct('i32sif')
s = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("Id:"))
    name =input("Name:").encode()
    age = int(input("Age:"))
    score = float(input("score:"))
    data= st.pack(id,name,age,score)
    s.sendto(data,ADDR)

s.close()
