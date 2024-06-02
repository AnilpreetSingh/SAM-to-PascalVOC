import os
import cv2
import shutil
import np

def saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir):
    for imgname in os.listdir(JPEGimagespath):
        _,imgNumber=imgname.split('_')
        imgNumber,_=imgNumber.split('.')

        if  int(imgNumber) not in ExclusionList:
            img=cv2.imread(JPEGimagespath+'/'+imgname)
            cv2.imwrite(finalimagedir+'/'+imgname ,img)  

    print('Finished Copying Images')

    for maskname in os.listdir(segclasspath):
        _,maskNumber=maskname.split('_')
        maskNumber,_=maskNumber.split('.')

        if  int(maskNumber) not in ExclusionList:
        
            mask=cv2.imread(segclasspath+'/'+maskname)
            newmask=np.zeros((mask.shape[0],mask.shape[1]),dtype=np.uint8)

            for i,row in enumerate(mask):
                for j,bgr in enumerate(row):
                    rgb=bgr[::-1]    
                    string_rgb=','.join(map(str,rgb))
                    newmask[i][j]=colorvec[string_rgb]
            
            cv2.imwrite(finalmaskdir+'/'+maskname ,newmask)
    print('Finished Copying masks')
    print('Total',len(os.listdir(finalmaskdir)),' images dataset')


###
colorvec={
"128,128,0":1,#fat
"0,0,128":0,#reticulin
"0,0,0":2,#cell
"0,128,0":2,#cell
"128,0,0":3#bone
}
segclasspath='job_25_dataset_2024_05_31_05_17_08_pascal voc 1.1/SegmentationClass/BATCH2-MF1-IMAGES'
JPEGimagespath='job_25_dataset_2024_05_31_05_17_08_pascal voc 1.1/JPEGImages/BATCH2-MF1-IMAGES'
ExclusionList=[12578,12579,12580,12581,12582]

finalCompletedir='integer-encoded-datasetB4'
finalmaskdir='integer-encoded-datasetB4/integer-encoded-masks'
finalimagedir='integer-encoded-datasetB4/integer-encoded-images'

# shutil.rmtree(finalCompletedir)
os.mkdir(finalCompletedir)
os.mkdir(finalmaskdir)
os.mkdir(finalimagedir)
saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir)
