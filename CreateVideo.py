import os 
import cv2

path = "images"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)
        
print(len(Images))
count = len(Images)
frame = cv2.imread(Images[0])

frame.shape(50,90)



size = (width,height)
print(size)

out = cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0, count-1):
    cv2.imread()
    out.write()

print("done")   