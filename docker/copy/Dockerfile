FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install git
RUN apt-get -y install python3-pip
RUN apt-get -y install vim
RUN pip3 install flask
RUN mkdir surajddr
RUN git clone https://github.com/suraj-yadav-git/greyatom-ml.git
WORKDIR greyatom-ml
RUN pip3 install -r requirements.txt
ENV JAVA_HOME /usr/local
COPY dummy.txt surajddr/dummy.txt
WORKDIR bin
CMD ["python3","service_summary.py"]
