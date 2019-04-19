#coding:utf-8
#wangjing
#index --> img --> mac
import os
f1 = "info2.txt"
all=[]
with open(f1,"rb") as f:
	all=f.readlines()

index = [0,13382,21826]
for i in index:
	url = all[i].strip().split(' ')[0]
	os.system("scp %s ouousei@192.168.0.221:/Users/ouousei/wj/facecover_jpg/"%url)
