

def display_fact (facts):
	 #Display eaxh person (key) and intresting fact (value)
	for fact in facts:
 		print ('{0} : {1}'.format(fact,facts[fact]))

#Create a Dictionary of people (key) and an intresting fact (value)

facts = {'Jeff' : 'Was born in France ',
		 'David' : 'Was a mascot in college',
		 'Anna' : 'Has arachnophobia ' }

display_fact(facts)

#Alter a facr about one of the pople on the list

facts['David'] = 'Can juggle'

#Add an extra person and corresponding fact to the list
facts['Dylan'] = 'Has a pet hedgehog'


#For space between both calles
print()

#Display the newly created list of people and facts
display_fact(facts)