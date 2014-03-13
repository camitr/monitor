#!/usr/bin/python

import os
import paramiko
#hostname = raw_input('IP:')
#dur	= raw_input('duration:')
#username = raw_input('username:')
#print hostname
#print username
 
pidp=os.getpid()
print pidp
f=open('pidpython','w')

f.write(str(pidp))
f.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect(hostname='10.129.200.146',username='admin',password='ttt23$')
print "Analysing the packets......."
stdin,stdout,stderr=\
ssh.exec_command("./infyloop.sh")
type(stdin)
out=stdout.readlines()
print out


#ssh.exec_command("ls")

