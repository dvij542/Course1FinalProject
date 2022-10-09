# from asyncio.windows_events import NULL
import cv2
import numpy as np
import glob

RUN_NO = 4
INPUT_FOLDER = 'run'+str(RUN_NO)+'_video'
OUTPUT_FILE = 'run'+str(RUN_NO)+'_video.mp4'
img_array = []
print(INPUT_FOLDER+'/*')
# file_list = glob.glob(INPUT_FOLDER+'/*')
# file_list.sort()
file_list = []
for i in range(16,655) :
    file_list.append(INPUT_FOLDER+'/frame_'+str(i)+'.png')
print(file_list)
for filename in file_list:
    img = cv2.imread(filename)
    # if img != None:
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter(OUTPUT_FILE,cv2.VideoWriter_fourcc(*'mp4v'), 10, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()