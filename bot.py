import praw

reddit = praw.Reddit(user_agent='Sarcastic Bot 0.0.1',
                     client_id='faECGlYFVehRgA', client_secret="yjIXpYK9aIifMNvJO_GdKiXszRY",
                     username='NotSarcasticBot', password='FODOR1')
 
withS = open("sarcasm.txt", "ab+")
withoutS = open("no_sarcasm.txt","ab+")

for comment in reddit.subreddit('all').stream.comments():
	s = comment.body
	asciiStr = s.encode('ascii', 'ignore')

	if asciiStr.find(" /s") >= 0 or asciiStr.find(" \\s") >= 0:
		index1 = asciiStr.find(" /s")
		index2 = asciiStr.find(" \\s")
		if (index1 < 0):
			index = index2
		elif (index2 < 0):
			index = index1
		else:
			if (index1 < index2):
				index = index1
			else:
				index = index2
				
		
		asciiStr = asciiStr[:index]
		withS.write(asciiStr)
		withS.write("\n")
	else:
		withoutS.write(asciiStr)
		withoutS.write("\n")


withS.close()
withoutS.close() 

