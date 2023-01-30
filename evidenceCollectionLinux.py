#Braedon Lyons
from datetime import datetime
import time
import os
import socket
import psutil

now = datetime.now()
timeZone = time.tzname[0]

f = open('/etc/os-release', 'r')
osInfoRaw = f.read().split('\n')
osInfo = osInfoRaw[0][6:]
osInfo = osInfo[:len(osInfo)-1]
osType = osInfoRaw[4][13:]
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

os.system('ip a > temp.txt')
f = open('temp.txt', 'r')
ipInfoRaw = f.read().split('\n')
ips = []
current = []
check = False
count = 0
maxlen = len(ipInfoRaw)-1
for line in ipInfoRaw:
    current.append(line)
    count = count + 1
    if count < maxlen:
        if ipInfoRaw[count][0].isnumeric():
            ips.append(current)
            current=[]
f.close()

os.system('w > temp.txt')
f = open('temp.txt', 'r')
users = f.read()
f.close()
f = open('/etc/passwd', 'r')
passwd = f.read().split('\n')
uid0users = []
for line in passwd:
    linelist = line.split(':')
    if len(linelist) >= 2 and int(linelist[2]) == 0:
        uid0users.append(line)
passwd = passwd[0:5]

os.system('sudo find / -perm -4000 -user root > temp.txt 2> /dev/null')
f = open('temp.txt', 'r')
rootfiles = f.read().split('\n')
rootfiles = rootfiles[0:5]
f.close()

os.system('ps aux > temp.txt')
f = open('temp.txt', 'r')
psinfo = f.readlines()
pids=[]
ncfiles = []
for line in psinfo:
    if "nc -l 8888" in line:
        newline = line.split()
        pid = newline[1]
        pids.append(pid)
if pids != []:
    for pid in pids:
        os.system('lsof -p ' + pid + ' > lsof.txt 2> /dev/null')
        d = open('lsof.txt', 'r')
        nccur = d.read().split('\n')
        if ncfiles == []:
            ncfiles.append(nccur[0])
        nccur = nccur[1:]
        for line in nccur:
            ncfiles.append(line)
f.close()
d.close()

os.system('lsof -nP +L1 > temp.txt 2> /dev/null')
f = open('temp.txt', 'r')
delfiles = f.read().split('\n')
f.close()

filename = 'test.txt' #static value for now, would change if script required
os.system('find ~ -mtime -1 -ls | grep ' + filename + ' > temp.txt')
f = open('temp.txt', 'r')
modifiedFiles = f.read().split('\n')
f.close()

output = []

output.append('SIFT Linux info collection script output')
output.append('\n')
output.append('current date and time:')
output.append(str(now) + ' ' + timeZone)
os.system('uptime -p > temp.txt')
f = open('temp.txt', 'r')
uptime = f.read()
output.append('\nThis computer has been ' + str(uptime))
output.append('Operating system: ' + osType)
output.append('\nKernel version: ' + kernelVersion)
output.append('\nCPU architecture: ' + architecture)
output.append('\nAmount of free physical memory: ' + str(memFree))
output.append('\nAmount of used physical memory: ' + str(memUsed))
output.append('')
output.append('\nFile system disk space usage information:\n')
output.append(fileInfo)
output.append('')
output.append('\nList of all partitions:\n')
output.append(partInfo)
output.append('\nHostname: ' + hostname)
output.append('')
output.append('\nAll currently logged in users:\n')
output.append(users)
output.append('')
output.append('\nList of all users (only first 5 shown):\n')
for line in passwd:
    output.append(line+'\n')
output.append('')
output.append('\nList of all users with uid=0:\n')
for user in uid0users:
    output.append(user+'\n')
output.append('')
output.append("\nAll SUID files owned by root (only first 5 shown)\n")
for line in rootfiles:
    output.append(line+'\n')
output.append('')
psinfo = psinfo[0:6]
output.append('\nList of all processes (only first 5 shown)\n')
for line in psinfo:
    output.append(line)
output.append('')
if len(ncfiles) > 6:
    ncfiles = ncfiles[0:6]
output.append('\nList of all files opened by netcat (only first 5 be shown)\n')
for line in ncfiles:
    output.append(line+'\n')
output.append('')
output.append('\nList of all deleted files (only first 5 shown):\n')
delfiles = delfiles[0:6]
for line in delfiles:
    output.append(line+'\n')
output.append('')
output.append('\nFiles wihtin home directory modified within the last 24 hours:\n')
for line in modifiedFiles:
    output.append(line+'\n')

with open(r'LinOutput.txt', 'w') as fp:
    for line in output:
        fp.write(line)
    print('LinOutput.txt file generated')

os.system('rm temp.txt')
os.system('rm lsof.txt')

