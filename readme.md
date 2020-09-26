spyder pycharm VsCode Atom Not jupyter

We should use function -- Resuable

never use keywords as function name, variable name dont use single letter variable name Variable names and function name which conveys the meaning of it

This makes our code more Readable

technical debt

Code should always contain documentation

Docstring to each function, class, modules Avoid inline comments as much as possible

Maintainable

Explainability -- how easy it is to understand the code -- machine learni

Scalability -- vertical scalability -- add ram and harddisk to the same laptop -- horizontal scalability --- add a new laptop

Assume 4GB 1 TB 4 core cpu+ GPU ML model with 10000 data ML 1m data We need to scale or infra

Modular structure Use of modules, classes and functions

path, config should be written in a seperate config files.

Empirical logic to find summary Split the sentence and use first sentence and find the top 3 sentences with maxm num of words among the rest Document summarisation ga1909 /bin - preprocessor.py Class ProcessDoc fucntions - special char - token - stopword removal - summarizer.py Class SummarizeDoc fucntions - readDocs - loadConfig - splitter - groupSentence - findNumWords - findTop3Sent - sentenceCombiner

relative path

local --push---git repo ---pull -- aws instance-- deploy

git init ----> only once git add . git commit -m "first commit" git remote add origin "https://github.com/saz2nitk/ga1909.git" --> once git push origin master

git add . git commit -m "first commit" git push origin master

SOAP REST fundamental principle of db

CRUD C- Create R- Readable U update D- Delete

REST GET- Read PUT - Update POST - Create DELETE - Delete HEAD

Framework Python

Flask - Most popular Django - popular Bottle - One page design FastAPI - NEw

ssh -i /drives/c/Users/saz2n/Downloads/ga1209.pem ubuntu@52.66.31.98 sudo git clone https://github.com/saz2nitk/ga1909.git sudo mkdir sajjad cd sajjad sudo apt-get install python3-venv sudo python3 -m venv gaenv

On the local

git add . git commit -m "message" git push origin master

On the server

sudo git pull origin master

git clone repourl ----> once in the lifetime git pull origin master --> for every next time

sudo gaenv/bin/pip3 install -r ga1909/requirements.txt gaenv/bin/python3 ga1909/bin/summaryservice.py

Virtualization tools ORacle VirtualBox VMWare Hyper-V --- windows 10 enterprise or home premium

These are complete VM

Dockers -- Mini VM they follow minimalistic architecture

We want applications to be OS independent

dockerhub.com install docker in aws ec2

linux -- link windows -- 7 or 10 home basic -- docker toolbox windows 10 home premium or enterprise -- docker desktop virtualization should be enabled

repo -- local repo (ec2) remote repo (dockerhub) sudo docker images --> list all images in local(ec2) repo sudo docker search ubuntu --? search all docker images with the word 'ubunut' in the remote repo dockerhub.com sudo docker pull ubuntu

containers sudo docker ps -a ---> list all active containers sudo docker run -it ubuntu bash --- It always create a new container

Create a container named flaskservice from ubunut image Within container install python3 Install git Install the libraries Pull the code Run

sudo docker run --name flaskservice2 -it ubuntu bash apt-get update apt-get install git apt-get install python3 apt-get install python-pip mkdir sajjad cd sajjad git clone https://github.com/saz2nitk/ga1909.git cd ga1909 pip3 install -r requirements.txt cd bin python3 summaryservice.py

How to create your own docker image

Create a file called as 'Dockerfile'

Within this Dockerfile we are going to write the commands to be executed

Dockerfile

FROM [base OS or image]

RUN [Any command which needs to executed only once (during build time) i.e. installations and settings]

CMD [Any command which needs to executed during run time]

sudo docker build -t dummyflaskimage .