import re

class ProcessDoc:
    """
    Module for preprocessing articles
    """
    def __init__(self):
        pass

    def removeSpclChar(self, text):
        """
        Remove special characters

        Input:
            text: string
        Output:
            modifiedText: string
        """
        filteredText = re.sub(',|;|#|$', text, '')
        return filteredText

    def convertToLower(self, text):
        return text.lower()

processObj = ProcessDoc()