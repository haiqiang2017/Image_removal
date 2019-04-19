
import glob  
import os  
import sys  
  
from PIL import Image  
  
EXTS =['jpg']#, 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG']
  
def avhash(im):  
    if not isinstance(im, Image.Image):  
        im = Image.open(im)  
    im = im.resize((8, 8), Image.ANTIALIAS).convert('L')  
    avg = reduce(lambda x, y: x + y, im.getdata()) / 64.  
    return reduce(lambda x, (y, z): x | (z << y),  
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),  
                  0)  
  
def hamming(h1, h2):  
    h, d = 0, h1 ^ h2  
    print d
    while d: 
        print d,d-1,d&(d-1)
        h += 1  
        d &= d - 1  
    return h  
  
if __name__ == '__main__':  


    out=open("info.txt",'w')
    if len(sys.argv) <= 1 or len(sys.argv) > 3:  
        print "Usage: %s image.jpg [dir]" % sys.argv[0]  
    else:  
        im, wd = sys.argv[1], '.' if len(sys.argv) < 3 else sys.argv[2]  
        h = avhash(im)  
  
        os.chdir(wd)  
        images = []
        cnt=0 
        images=open("imglist").read().splitlines()
        for img in images:
                print >>out,img,avhash(img)
                perc = 100. * cnt / len(images)  
                x = int(2 * perc / 5)  
                print '\rCalculating... [' + '#' * x + ' ' * (40 - x) + ']',  
                print '%.2f%%' % perc, '(%d/%d)' % (cnt, len(images)),  
                sys.stdout.flush()  
                cnt+=1
        # seq = []  
        # prog = int(len(images) > 50 and sys.stdout.isatty())  
        # for f in images:  
        #     seq.append((f, hamming(avhash(f), h)))  
        #     if prog:  
        #         perc = 100. * prog / len(images)  
        #         x = int(2 * perc / 5)  
        #         print '\rCalculating... [' + '#' * x + ' ' * (40 - x) + ']',  
        #         print '%.2f%%' % perc, '(%d/%d)' % (prog, len(images)),  
        #         sys.stdout.flush()  
        #         prog += 1  
  
        # if prog: print  
        # for f, ham in sorted(seq, key=lambda i: i[1]):  
        #     print>>out,"%d\t%s" % (ham, f)  
    out.close()
