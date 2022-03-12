# -*- coding: utf-8 -*-
"""
Created on TUE May 4 10:49:00 2021
@author: Jayden
    
"""
import os
import pymysql

### Global ###
username = "xxxx"
password = "xxxx"
file_path = os.getcwd()+'xxxx.txt'
msg_list = []

### Class ###
class Msg :
    seq = ""
    srcnum = ""
    date = ""
    srccid = ""
    
    def __init__(self, seq, srcnum, date, srccid):
        self.seq = seq
        self.srcnum = srcnum
        self.date = date
        self.srccid = srccid
        

def read_msg(file_path):
    f = open(file_path, 'r', errors='ignore')
    lines = f.read().split()
    f.close()
    
    i=0
    while( i < (len(lines))):
        if(i==len(lines)) :
            break;
        else :
            m = Msg(lines[i],lines[i+1],lines[i+2],"")
            msg_list.append(m)
            i=i+3
        
#Print CID
def print_CID():
    line=""
    for i in msg_list:
        line = line + "$" + str(i.seq+"$"+i.srcnum+"$"+i.date+"$"+i.srccid) + "\n"

    f = open("202104_CID.txt",'w')
    f.write(line)
    f.close    
    

# Msg Read
read_msg(file_path)

# MySQL Connection
conn = pymysql.connect((Skip caused by Security))                
# Connection으로부터 Cursor 생성
curs = conn.cursor()
query = "SET @@global.tmp_table_size=1024*1024*64"
curs.execute(query)

#SQL문 실행
for m in msg_list:
    query = (Skip caused by Security)
    curs.execute(query)
    result_check = curs.fetchone()  
    if(result_check == None):
        m.srccid = "미조회"
    else:
        m.srccid = result_check[1]
    
    print(m.srcnum+"/"+m.srccid)

print_CID()    