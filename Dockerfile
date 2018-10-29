# start from base
FROM python:3.5

COPY ImageCompare.py ./
COPY test /data/test
RUN pip install --upgrade pip
RUN pip install scikit-image
RUN pip install opencv-python
RUN pip install numpy

ENTRYPOINT ["python", "ImageCompare.py"]