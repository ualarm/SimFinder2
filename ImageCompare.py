import sys
import os
import time
from skimage.measure import compare_ssim as ssim
import cv2

def compareImagePair(image1, image2):
   im1 = cv2.imread(image1)
   im2 = cv2.imread(image2)
   return (1.0-ssim(im1, im2, multichannel=True))
   
def main(argv):
   #print("First argument: " + argv[0])
   #print("Second argument: " + argv[1])
   count = 0;
   output_csv = argv[0].replace(".csv", "_output.csv")
   with open(output_csv, "w") as outs:
      outs.write("image1,image2,similarity,elapsed\n") 
      with open(argv[0], "r") as ins:
        for line in ins:
            count += 1
            if( count > 1 ):
                images = line.rstrip().split(",")
                image1 = argv[1] + os.sep + images[0]
                image2 = argv[1] + os.sep + images[1]
                if( os.path.isfile(image1) and os.path.isfile(image2) ):
                    start = time.clock()
                    sim = compareImagePair(image1, image2)
                    elapse = time.clock() - start
                    outs.write(images[0]+","+images[1]+","+'%4.3f' % sim +","+'%4.3f' % elapse +"\n")
                else:
                    print("File not found at line " + str(count))
                    continue
        
if __name__ == '__main__':
    main(sys.argv[1:])
