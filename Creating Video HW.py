import os
import cv2
path = "Images"
img = []
for file in os.listdir(path):
    name, ex = os.path.splitext(file)
    if ex in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        f_name = path+"/"+file
        print(f_name)
        img.append(f_name)
print(len(img))
cnt = len(img)
frame = cv2.imread(img[0])
h,w,c = frame.shape
size = (w,h)
print(size)
out = cv2.VideoWriter("Friends.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for i in range(cnt-1):
    frame = cv2.imread(img[i])
    out.write(frame)
out.release()
print("D")
