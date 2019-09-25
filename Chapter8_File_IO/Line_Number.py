'''
Try creating a program that opens file.txt. Read each line of the file and then prepend it with a line number
'''
#Including Exception
try:
	with open ('file.txt') as file_name:
		line_num =  1
		for line in file_name:
			print('{0} : {1}'.format(line_num,line))
			line_num += 1
except:
	file_name = []
	print(len(file_name))

