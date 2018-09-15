import re

sarcastic = open("sarcasm.txt", 'r')
listOfText = [comment.split("\n") for comment in sarcastic.readlines()]

notsarcastic = open("no_sarcasm.txt", 'r')
listOfText2 = [comment.split("\n") for comment2 in notsarcastic.readlines()]

for comment in listOfText:
	str = comment
	listOfSentences = sentenceMaker(str)
	sarcasticSentences = open("sarcasticSentences.txt", 'a+')
	for sentence in listOfSentences:
		sarcasticSentences.write(sentence) 

for comment2 in listOfText2:
	str = comment2
	listOfSentences2 = sentenceMaker(str)
	notSarcasticSentences = open("notSarcasticSentences.txt", 'a+')
	for sentence2 in listOfSentences2:
		notSarcasticSentences.write(sentence2)

def sentenceMaker(str):
	sentences = list()
	str.replace("'", "") 
	str.replace("@", "")
	str.replace("#", "")
	str.replace("^", "")
	str.replace("*", "")
	str.replace("%", "")
	str.replace("~", "")
	str.replace("$", "")
	str.replace("<", "")
	str.replace(">", "")
	
	if str.find(".") == -1 and str.find("?") == -1 and str.find("!") == -1:
		return [str]

	else:
		sentences = re.split("\!+ *|\.+ *|\?+ *",str)
		return sentences


