import yaml
import numpy as np
from preprocessor import ProcessDoc

class SummarizeDoc:

    def __init__(self):
        with open('../config/config.yml', 'r') as fl:
            self.config = yaml.load(fl)

    def loadDoc(self, filePath):
        with open(filePath, 'r', encoding='utf-8') as fl:
            text = fl.read()
        return text

    def splitSentences(self, text):
        sentences = text.split('.')
        return sentences

    def groupSentences(self, sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent

    def findSentLength(self, text):
        return text.split()

    def findSentLengthArray(self, sentences):
        return [self.findSentLength(sent) for sent in sentences]

    def findTopSentence(self, sentLengths, sentences, n):
        sortedIdx = np.argsort(sentLengths)
        topIdx = sortedIdx[-n:]
        topSentences = [sentences[i] for i in topIdx]
        return topSentences

    def preprocess(self, text):
        preProcessObj = ProcessDoc()
        filteredText = preProcessObj.removeSpclChar(text)
        filteredText = preProcessObj.convertToLower(filteredText)
        return filteredText

    def findSummary(self):
        filePath = self.config['data_path']['train_data']
        text = self.loadDoc(filePath)
        filteredText = self.preprocess(text)
        sentences = self.splitSentences(filteredText)
        firstSent, restOfSent = self.groupSentences(sentences)
        sentLengths = self.findSentLengthArray(restOfSent)
        topSentences = self.findTopSentence(sentLengths, restOfSent, self.config['sentence_num'])
        allSentences = [firstSent] + topSentences
        summary = ' '.join(allSentences)
        return summary

"""
Use:
summarizeObj = SummarizeDoc()
summary = summarizeObj.findSummary()
"""