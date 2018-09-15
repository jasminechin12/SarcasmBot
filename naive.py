sarcastic = open("sarcasm.txt", "r+")                         #open sarcastic text file                                                                                                       
sarcasticlist=[comment.split("\n")for comment in sarcastic.readlines()]
for comment in sarcasticlist:
	wordcountsarc = len(comment.split())

notsarcastic = open("no_sarcasm.txt", "r+")            #open notsarcastic text file                                                                                                            
notsarcasticlist = [comment.split("\n") for comment in notsarcastic.readlines()]
for comment in notsarcasticlist:
	wordcountnot = len(comment.split())                                      #this counts all the words in the sarcastic text file                                                                   

sarc = dict()                                                                                       #this creates the dictionary called sarc containing words used in sarcastic strings                                                        
for comment in sarcasticlist:
	for word in comment:                                                  #for each word in the text sarcastc                                        
		if word in sarc:
			sarc[word] = sarc[word] + 1                             #it will increment the number of that word in the dictionary                                   
		else:                                                                           #otherwise                                                               
			sarc[word] = 1                                      #it will create that word and give it the value 1                          

notsarc = {}                                                                                                                                                                                    
for comment in notsarcasticlist:
	for word in comment:                                                                                                                                                          
		if word in dict.notsarc():                                                                                                                                                              
			notsarc[word] = notsarc[word] + 1                                                                                                                                               
		else:                                                                                                                                                                                   
			notsarc[word] = 1                                                                                                                                                               
while 1:                                                                                        #infinite loop                                                                                  
	final = 0
	stringenter = input("Enter your string: ")                     #user input of string
	stringwords = stringenter.split()                               #split user inputted string                                                                                             
	print(stringwords)
	final = 0                                                                               #create number final                                                                            
	for word in stringwords:
		count = wordcountsarc                                                                                                                                                                
		print(count)
		while count > 0:
			if word in sarc:                                         #check if word is in sarc dictionary                                                                            
				final = final + sarc[word]                              #if so, add to value for final                                                                         
			count = count - 1
		count = wordcountnot
		while count > 0:	
			if word in notsarc:                                        #check if word is in not sarc dictinct value                   
				final = final - notsarc[word]                   #if so, subtract value of 1 from final
			count = count - 1                                                                                  
	while final>0:                                                                                                                                                                             
		print("this statement is sarcastic")                                                                                                                                            
		final = 0
	while final<0:                                                                                                                                                                             
		print ("this statement is not sarcastic")      
		final = 0
	while final == 0:
		print("We cannot determine if this statement is sarcastic. Please try again.")
		final =1
