'''

'''

#Create an empty list to store lines from unsorted list
animals = []
#Exception
try:
	#Open and automatically close the unsorted list file
	with open('unsorted_animals.txt') as unsorted_list:
		#loop through the list and add each line to the animals empty list
		for lines in unsorted_list:
			animals.append(lines)
		#.Sort() function sorts strings and intergers
		animals.sort()
except:
	#If 0 is returned the file does not exist. 
	print(len(unsorted_list))

#Exception
try:
	#Create a new text file for the sorted list, use the 'write' mode 
	with open('sorted_animals.txt','w') as sorted_list:
		#Loop throught the list "animals" 
		for animal in animals:
			#write each animal from the list into the new file 
			sorted_list.write(animal)
except:
	#If 0 is returned the file does not exist.
	print(len(sorted_list))

