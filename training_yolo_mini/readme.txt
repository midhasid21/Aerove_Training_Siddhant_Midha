The format in the annotations is 
<leftmostx> <leftmosty> <w> <h>

yolov4tiny format is
<classno> <xcen> <ycen> <w> <h>

instructions: https://colab.research.google.com/drive/1hQO4nOoD6RDxdbz3C1YSiifTsyZjZpYm?usp=sharing#scrollTo=hRoFfkBFT7Hm
refer to this drive link for the related files: https://drive.google.com/drive/folders/13ySERHyIFTZ3kVoidHD6rAklnvnir286?usp=sharing

the three py files do the following: 
>>> opr.py enodes into yolo format
>>> the diverges.py one separates into multiple files as per the frames
>>> convtoimage.py converts video into frames
also note that this procedure would be better than hand-annotating as one run of the scripts can give us ~2-3K images
also note the sizes of the images in the diverges.py one, so as to scale b/w 0 and 1 appropriately

sidenote: while taking a video does get us lot of data, we need to remove redundancies by observing that upto, say, a 10-frame movement, not much features differ. So just taking all of the 20+K images may be a waste. Could do it if we can fast enough?

----------------------------------
