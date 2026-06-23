FROM python:3.12.13
RUN apt update
RUN pip install scikit-learn==1.4.2
RUN pip install diffprivlib==0.6.6
COPY server.py /home/
COPY client.py /home/
COPY ruido.py /home/
CMD bash
