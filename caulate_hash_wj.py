# _*_encoding: utf-8 _*_
from percephash import avhash
f1="bank_img_list"
all= []
with open(f1,"rb") as f:
    all= f.readlines()
res= []
with open("info.txt","wb") as f:
    for line in all:
#        print line
        hash_img = avhash(line.strip())
        fid = line.strip()
        h = fid+ " "+str(hash_img)
        f.write(h+'\n')
