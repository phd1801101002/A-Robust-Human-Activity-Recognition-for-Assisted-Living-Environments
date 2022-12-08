import numpy as np
import os
import time
from scipy import io
import array
from PIL import Image as im
from natsort import natsorted
import cv2

####------- Load data from .dat files -------######

def bin_loader_proto(file_path):                                               
    depthFrames = np.fromfile(file_path,dtype="uint16")
    print(depthFrames.shape)
    return depthFrames

#### -------------- Save Images -------------- ####
def save_frames(file,file_path,save_path):
    print(os.path.join(file_path,file))
    x = bin_loader_proto(os.path.join(file_path,file))
    #print(x.shape)
    number_frames = (x[0:4]).view(np.uint64)
    width = x[4:6].view(np.uint32)
    height = x[6:8].view(np.uint32)
    size = x[8:10].view(np.uint32)
    data = x[10:]
    print("Formatted", number_frames, width, height, size)
    for i in range(int(number_frames)):
        frm = np.reshape(data[217092 * i + 4:217092 * (i + 1)], (-1, 512)).astype("uint8")
        img = im.fromarray(frm)
        path = os.path.join(save_path, file.split('.')[0])
        if not os.path.exists(path):
            os.mkdir(path)
        # print(path)
        img.save(path + '/' + str(i) + '.png')


#file_path = "path-to-depth-files"
#save_path="path-to-save-images"
for file in os.listdir(file_path):
    save_frames(file,file_path,save_path)
