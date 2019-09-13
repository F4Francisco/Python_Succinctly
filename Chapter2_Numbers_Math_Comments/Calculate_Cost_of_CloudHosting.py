'''
Write a Python Program that will display the answer to the following questions:

How much will it cost to operate one server per day?
How much will it cost to operate one server per month?
How much will it cost to operate twenty servers per day?
How much will it cost to perate twenty server per month?
How many days can i operate one server with $1,836?

COST of operation for ONE server PER HOUR = 1.02
'''

one_server_cost_per_hour = 1.02

#How much will it cost to operate one server per day?

one_server_cost_per_day = (1.02 * 24)

print("Cost to operate one server per day is : $ {:.2f}" .format(one_server_cost_per_day))

#How much will it cost to operate one server per month?
one_server_cost_per_month = (one_server_cost_per_day * 30)

print("Cost to operate one server per month is: $ {:.2f}" .format(one_server_cost_per_month))

#How much will it cost to operate twenty servers per day?
twenty_servers_cost_per_day = (one_server_cost_per_day * 20)
print("Cost to operate twenty servers per day : $ {:.2f}" .format(twenty_servers_cost_per_day))

#How much will it cost to perate twenty server per month?
twenty_servers_cost_per_month = (twenty_servers_cost_per_day * 30)
print("Cost to operate twenty servers per month : $ {:.2f}" .format(twenty_servers_cost_per_month))

#How many days can i operate one server with $1,836?
how_many_days_to_run = (one_server_cost_per_day % 1836)
print("You can operate one server with $1,836 for : {} days " .format(how_many_days_to_run))





