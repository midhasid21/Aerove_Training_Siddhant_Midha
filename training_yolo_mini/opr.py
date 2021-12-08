file = open("video_initial_mast_training_001.txt","r")
read = file.readlines()
newlist = []
for element in read:
    element = element.split('\t')
    string = '0'
    element[3] = element[3].split('\n')
    element[3] = element[3][0]
    xcen = int(element[0]) + int(element[2])/2
    ycen = int(element[1]) + int(element[3])/2
    string += '\t' + str(xcen) + '\t' + str(ycen) + '\t' + str(element[2]) + '\t' + str(element[3]) + '\n'
    newlist.append(string)
#'894\t468\t54\t54\n',
#print(newlist)
with open('video_initial_mast_training_001_foryolo.txt','w') as f:
    for line in newlist:
        f.write(line)
file.close()
