'''
Create a Python program that will capture and display a person's grocery shopping list.
Make it so the programwill continually prompt the user for another item until the point where they enter a blank item. After all the items
have been entered, try displaying the shopping list back to the user.
'''


grocery_list = []
finished = False

while not finished:
	item = input("Enter an item for your grocery list. Press <ENTER> when done : ")

	if len(item) == 0:
		finished = True
	else:
		grocery_list.append(item)
		print("Item has been added")

print()
print("Your Grocery List")
print("-" * 18)
for item in grocery_list:
	print(item)



