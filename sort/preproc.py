import re
obj_arr = []
count = 0
frame = 0
lines = open('1_result.txt','r').readlines()
stopwords = ["mast:","(left_x:","top_y:","width:","height:","%"]
print(lines[10])
for line in lines:
	if('Objects:' in line):
		obj_arr.append(count)
	count += 1
print(obj_arr[0])
with open('det.txt','w') as f:
	for i in range(1,len(obj_arr)):
		if(i == len(obj_arr)-1):
			break
		local_lines = []
		local_conf = []
		for j in range(obj_arr[i],obj_arr[i+1]):
			if('mast:' in lines[j]):
				local_lines.append(lines[j])
		if(len(local_lines) == 0):
			strr = str(frame) + ',-1,' + str(1) + ',' + str(1) + ',' + str(1) + ',' + str(1) + ',' + str(0) + ',-1,-1,-1'
			f.write(strr)
			f.write("\n")
			frame+=1
			continue
		print(local_lines)
		for i in range(len(local_lines)):
			line = local_lines[i]
			querywords = line.split()
			last = querywords[len(querywords)-1]
			last = last.strip(")")
			querywords.pop()
			querywords.append(last)
			resultwords  = [word for word in querywords if word.lower() not in stopwords]
			result = ' '.join(resultwords)
			result = result.split()
			conf = result[0]
			conf = conf[0: -1]
			lx = result[1]
			ly = result[2]
			w = result[3]
			h = result[4]
			local_lines[i] = [lx,ly,w,h,conf]
			local_conf.append(conf)
		confidence = max(local_conf)

		best_line = local_lines[local_conf.index(confidence)]
		result = best_line
		conf = result[4]
		lx = result[0]
		ly = result[1]
		w = result[2]
		h = result[3]
		strr = str(frame) + ',-1,' + str(lx) + ',' + str(ly) + ',' + str(w) + ',' + str(h) + ',' + str(conf) + ',-1,-1,-1'
		frame += 1
		f.write(strr)
		f.write("\n")

