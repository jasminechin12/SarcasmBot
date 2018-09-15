def topLargest(num, str):
	wordList = str.split()
	biggestWords = list()
	
	max = ""


	while (len(wordList) < num):
		wordList.append("")



	while len(biggestWords) <  num:

		for word in wordList:
			if len(word) >= len(max):
				max = word

		wordList = [w.replace(max, "") for w in wordList]
		biggestWords.append(max)
		max = ""

	return biggestWords
