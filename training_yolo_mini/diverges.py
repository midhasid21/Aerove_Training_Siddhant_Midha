fn = open("video_initial_mast_training_001_foryolo.txt","r")
for i, line in enumerate(fn):
    f = open("frame%i.txt" %(i),'w')

    f.truncate(0)
    l = line.split() 
    xcen = float(l[1])
    ycen = float(l[2])
    w = float(l[3])
    h = float(l[4])
    xcen = xcen/1920 
    w = w/1920
    ycen = ycen/1080
    h = h/1080
    if(i == 1):
        print(xcen)
    string = '0' +' ' + str(xcen) + ' ' + str(ycen) + ' ' + str (w) + ' ' + str(h)
    f.write(string)
    f.close()
