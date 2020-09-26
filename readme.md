Modular structure
Use of modules, classes and functions

path, config should be written in a seperate config files.

Empirical logic to find summary 
Split the sentence and use first sentence and find the top 3 sentences with maxm num of words among the rest
Document summarisation
	- preprocessor.py
		Class ProcessDoc
			fucntions
			- special char
			- token
			- stopword removal
	- summarizer.py
		Class SummarizeDoc
			fucntions
            - readDoc
            - loadConfig
			- splitter
			- firstSentExtractor
			- findNumWords
			- findTop3Sent
			- sentenceCombiner

Commands :
ssh -i /drives/c/Users/saz2n/Downloads/ga1209.pem ubuntu@52.66.31.98
sudo git clone https://github.com/saz2nitk/ga1909.git
sudo apt-get install python3-venv
sudo python3 -m venv gaenv

On the local

git add .
git commit -m "message"
git push origin master

On the server

git pull origin master

git clone repourl ----> once in the lifetime 
git pull origin master --> for every next time

sudo gaenv/bin/pip3 install -r ga1909/requirements.txt
gaenv/bin/python3 ga1909/bin/summaryservice.py
