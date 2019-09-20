
def display_info (list_of_cities_and_zip):
	#Loop and display the list
	for (cities,zips) in list_of_cities_and_zip:
		print("The ZIP code for {0} is {1}".format(cities,zips))
# Create a list of tuples containing city names and their zip codes.
list_of_cities_and_zip = [("Short Hills, NJ" , '07078'),
						  ("Fairfax Station, VA" , '22039'),
						  ("Weston, CT" , '06883'),
						  ("Great Falls, VA" , '22066')]
display_info(list_of_cities_and_zip)