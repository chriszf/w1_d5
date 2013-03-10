from sys import argv

script, filename = argv

#open the file
txt = open(filename)
txt = txt.read()
#count how many of each letter using a loop or some sort

lower_text = txt.lower()

counter = [0]*26

for i in lower_text:	
	#get ord value of the letter
	intValue = ord(i)

	#test if character is a letter from a-z (97-122)
	if intValue >= 97 and intValue <= 122:
	#subtract 97 to determine the position in the list
		indexNum = intValue - 97
		count = counter[indexNum]
		counter[indexNum] = count + 1


#print count to screen in alphabetical order
for i in counter:
	print i

#pipe contents to 'spark' program

