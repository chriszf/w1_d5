from sys import argv

script, filename = argv

#open the file
txt = open(filename)
txt = txt.read()
#count how many of each letter using a loop or some sort

lower_text = txt.lower()

counter = [0]*26

	for x in lower_text:
		
#test if character is a letter (97-122)

#get value of the letter and subtract 97 to determine the position in the list

#count the letter (increment by 1)

	


#print count to screen in alphabetical order

#pipe contents to 'spark' program

#