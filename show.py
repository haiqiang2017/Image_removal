import os,sys
import Image
def paste(img,pic,pos):
    if len(pic)==0:
        return img
    try:
        img1= Image.open(pic).resize((64,64))
        img.paste(img1, pos)
    except:
        print "can not find img",pic
        return img
    return img

def merge(pic1,pic2,output):
    merge_img = Image.new('RGB', (128,64), 0xffffff)
    merge_img = paste(merge_img,pic1,(0,0))
    merge_img = paste(merge_img,pic2,(64,0))
#    merge_img = paste(merge_img,pic3,(800,20))
#    draw= ImageDraw.Draw(merge_img)
 #   font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', 18)
#    draw.text((0,0),"query", fill="red",font=font)
#    draw.text((400,0),"groundtruth: "+str(round(info1,3)), fill="red",font=font)
#    draw.text((800,0),"predict : "+str(round(info2,3)), fill="red",font=font)
    merge_img.save(output,quality=100)
def hamming(h1, h2):
    h, d = 0, h1 ^ h2
#    print d
    while d:
#        print d,d-1,d&(d-1)
        h += 1
        d &= d - 1
    return h


data=[]
names=[]
linesa=open("info2.txt").readlines()
for line in linesa:    
    data.append(int(line.split(" ")[-1]))
    names.append(line.split(" ")[0])

length=len(linesa)
#$print data[:100]
lines=open("output_4")
cnt=0
for line in lines:
    array=line.split(" ")
    a=int(array[0])
    b=int(array[1])
    merge("imgs/"+names[a],"imgs/"+names[b],str(cnt)+".jpg")
    print cnt,hamming(data[a],data[b])
    cnt+=1
    if cnt>=50:
        break
