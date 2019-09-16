'''
Create a program that will ask the user how far they wish to travel.
If they express a desire to travel less than 3 miles,
	Have the program tell them to walk.
If they desire to travel more than 3 miles but less than 300 miles 
	Have the program tell them to drive
In any instance where they want to travel 300 + miles tell them to fly
'''

user_input = input("How far would you like to travel?")

distance = int(user_input)

if (distance < 3):
	transportation = 'walking'

	#print("You should consider walking to your destination")

elif (distance > 3 and distance < 300):
	transportation = 'driving'
	#print("You should consider driving to your destination")

elif (distance > 300):
	transportation = 'flying'
	#print("You should consider taking a plane to your destination")

print("I suggest {} to your destination".format(transportation)) 