'''
Write a Python program that will prompt for input and then display a pig "saying" whatever text was provided by the user.
Place the input you receive from the user inside a speech bubble. 
Exapand or contract the speech bubble in order to make it fit around the input provided.

'''
#Prompt the user for what they would like to say and store it in user_input variable
user_input = input ("What would you like the pig to say?")

#Using the len() function store the length of the user's input into user_input_len
user_input_len = len(user_input)

print('                {}'.format('_' * user_input_len))
print('              < {} > '.format(user_input))
print('                {}'.format('_'*user_input_len))
print('               /')
print(' 	^..^ /')
print(  	'~(  ( oo )')
print( 	 '   ,, ,,')
