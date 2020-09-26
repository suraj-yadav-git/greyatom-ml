FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install git
RUN apt-get -y install python3-pip
RUN apt-get -y install vim
RUN pip3 install flask
RUN mkdir surajddr
RUN cd surajddr
RUN git clone https://github.com/suraj-yadav-git/greyatom-ml.git
RUN cd greyatom-ml
RUN pip3 install -r /greyatom-ml/requirements.txt
RUN cd bin

CMD ["python3","/greyatom-ml/bin/service_summary.py"]
