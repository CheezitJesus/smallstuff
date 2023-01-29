#
from datetime import datetime
import time
import os
import socket
import psutil

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
timeZone = time.tzname[0]
print(currentTime)
print(timeZone)

f = open('/etc/os-release', 'r')
osInfoRaw = f.read().split('\n')
osInfo = osInfoRaw[0][13:]
osInfo = osInfo[:len(osInfo)-1]
osType = osInfoRaw[1][6:]
osType = osType[:len(osType)-1]
os.system('uname -r > temp.txt')
f.close()
x = open('temp.txt', 'r')
kernelVersion = x.read()
kernelVersion = kernelVersion[:len(kernelVersion)-1]
os.system('lscpu > temp.txt')
x.close()
y = open('temp.txt', 'r')
cpuInfoRaw = y.read().split('\n')
architecture = cpuInfoRaw[0].split()
architecture = architecture[1]
y.close()

m = open('/proc/meminfo', 'r')
memInfoRaw = m.read().split('\n')
memFree = memInfoRaw[1].split()
memFree = int(memFree[1])
memTotal = memInfoRaw[0].split()
memTotal = int(memTotal[1])
memUsed = memTotal - memFree
m.close()

os.system('df > temp.txt')
f = open('temp.txt', 'r')
fileInfo = f.read()
fileInfo = fileInfo[:-1]
f.close()

os.system('lsblk > temp.txt')
f = open('temp.txt', 'r')
partInfo = f.read()
partInfo = partInfo[:-1]
f.close()

hostname = socket.gethostname()

os.socket('ip a > temp.txt')
f = open('temp.txt', 'r')

#print(fileInfo)
#print(architecture)
#print(kernelVersion)
#print(kernelInfo)
#print(architecture)
#print(modelName)
