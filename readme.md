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
