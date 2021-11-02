import numpy as np
import cv2
import os
import json
VIDEOS_DIR=r"/Users/seawavve/Desktop/swing_PBL/swingmybaby1 2/"
FILE_NAME=r"gyro_swings1"


def get_preprocessed_video():
    print("--------Preprocess Train Video-------")
    print('input file name: ',FILE_NAME)
    input_path=os.path.join(VIDEOS_DIR, FILE_NAME + '.mp4')
 
    cap = cv2.VideoCapture(input_path)
    # Initialize frame counter
    cnt = 0
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('input width: ', w_frame, 'input height: ', h_frame)
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
    

    print('output width: ',w_frame ,'output height: ',h_frame)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cnt+=1
            print('NOW output FRAME:', cnt)
            cv2.imwrite("/Users/seawavve/Desktop/swing_PBL/img/"+FILE_NAME+"/frame%d.jpg" % cnt, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    print('input frame: ',cnt)
    cap.release()

if __name__=="__main__":
    get_preprocessed_video()
