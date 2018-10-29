# Project Title

This project provides an interface to batch compare a group of images specified in csv file.

# Prerequisites
For each of the prerequisites, skip if it is already installed, otherwise go to the download website and follow instructions there to download and install the software according to your operating system.
Python (https://www.python.org/downloads/)
Scikit-Image (pip install scikit-image)
opencv-python (pip install opencv-python)
numpy (pip install numpy)
docker (https://docs.docker.com/v17.09/docker-for-windows/install/ or https://docs.docker.com/v17.09/docker-for-mac/install/)

### Instructions

Step 1. 
On host OS, run 'python ImageCompare.py <csv_file> <image_dir>'

Step 2.
Open docker client, navigate to unzipped root folder where you can find ImageCompare.py, run 'docker build -t ImageCompare .'

Step 3.
To test the docker image on windows with images on host system, make a folder 
(for example, test) under C:\Users and copy image files/csv file to that folder, 
then run 'docker run -v /c/Users/test:/data/test -t ImageCompare /data/test/<csv> /data/test/images'

Step 4.
Deploy on docker hub, run
'docker tag ImageCompare ImageCompare_v1'
'docker push <docker_user_name>/ImageCompare_v1'


#### Implementation Steps
First do some search to find out image compare code examples using skiimage and cv2. 
Then code ImageCompare.py according to requirements. 
Then create dockerfile to dockerize the python scripts.

  

  




