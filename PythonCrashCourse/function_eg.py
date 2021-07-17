# ******************** Function **********************************

def greet_user():
	print("Hello")

# Call Function
greet_user()

# Pass argument to the function

def greet_user_again(username):  # username is parameter
	print("Hello username")

#Call function by passing argument

greet_user_again('john')

# ******************* Positional Parameters ****************************

def describe_pet(pet_type, pet_name):
	print(f"I have {pet_type} whose name is {pet_name}")

# ************* call funtion with two argument *********************
describe_pet('Dog', 'Sheru')

# ***************** Keyword arguments *********************************

def my_pet(pet_type='dog', pet_name='Rani'):
	print(f"I have another {pet_type} whose name is {pet_name}")

# call my_pet()

my_pet()

# ****************** Using Default Values **********************************
def another_pet(pet_name, pet_type='dog'):
	print(f"I have another {pet_type} whose name is {pet_name}")

another_pet('Kallu')
another_pet(pet_name='Dona', pet_type='cat')


def make_shirt(size, print_message='Enconrraged'):
	print(f"Please make shirt of size {size} and print message {print_message}")


make_shirt('medium')
make_shirt(size='medium', print_message="Happy Happy")

def make_more_shirts(size, message='I Love Python'):
	if size == 'Large' or size == 'Medium':
		print(f"Make shirt of size {size} and print Message {message}")

	else:
	    print(f"Make shirt of size {size} and print Message {message}")

make_more_shirts(size='Medium')
make_more_shirts(size='small', message='Do the Home Work')

# **************  Return Values *******************
#The return statement takes a value from inside a function and sends it back to the line that called the function

def get_formated_name(first_name, last_name):
	full_name= first_name +' ' + last_name
	return full_name

musician=get_formated_name('jimi', 'hendrix')
print("My favourite Musician is", musician.title())


# ************************ Making Argument Optional ***************************
def get_full_name(first_name, last_name, middle_name=''):
	full_name=first_name +' '+ middle_name + ' ' + last_name
	return full_name

singer=get_full_name('kishori', 'amonkar')
print(singer)

musician=get_full_name('john', 'lee', 'hooker')
print(musician.title())


def Get_Full_Name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name +' '+ middle_name + ' ' + last_name
	else:

		full_name = first_name +' '+ last_name
	return full_name.title()


batsman=Get_Full_Name('sachin', 'tendulker')
print(batsman)

cricketer=Get_Full_Name('sachin', 'tendulker', 'ramesh')
print(cricketer)

# ************************* Return Dictionary *********************************

def build_person(first_name, last_name, age=''):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age

	return person
tabla_player=build_person('zakir', 'Hussain', '70')
print(tabla_player)


# ************* Using Function with While Loop ****************

# while True:
# 	fname=input("Enter Your First Name: ")
# 	lname=input("Enter Your Last Name: ")

# 	formated_name=get_formated_name(fname, lname)
# 	print(f"Hello {formated_name}")



def describe_cities(country, city):
	city_description=country+','+' '+city
	return city_description

city_details=describe_cities('India', 'Mumbai')
print(city_details)


#Return Dictionary

def make_album(artist_name, album_title, no_tracks=''):
	album={'artist': artist_name, 'title': album_title}
	if no_tracks:
		album['number_of_tracks']=no_tracks
		return album
	else:
		return album

my_album=make_album('lata', 'Old is Gold', 20)
print(my_album)
my_album=make_album('kishor', 'All time hit Duet')
print(my_album)


# *************************** Pass a List to Function *******************

def greet_users(names):

	for name in names:
		msg="Hello" + ' ' + name.title()
		print(msg)

usernames=['suresh', 'ramesh', 'jitu']
greet_users(usernames)


def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing Models:" + current_design)
		completed_models.append(current_design)

unprinted_designs=['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]
print_models(unprinted_designs, completed_models)


def show_completed_models(completed_models):
	for item in completed_models:
		print(item + "Model is printed")

show_completed_models(completed_models)


def show_singers(singers):
	for singer in singers:
		print(singer.title())

singers=['lata', 'rafi', 'kishor', 'mukesh']
show_singers(singers)


def make_great(singers):
	for singer in singers:
		if singer == 'lata':
			greatness='No one like her'
			print(singer + ' ' + greatness)
			singers.append(greatness)

		elif singer == 'rafi':
			greatness='The versatile singer'
			print(singer + ' ' + greatness)
			singers.append(greatness)


		elif singer == 'kishor':
			greatness='All time hit singer'
			print(singer + ' ' + greatness)
			singers.append(greatness)

		elif singer == 'mukesh':
			greatness='The great singer'
			print(singer + ' ' + greatness)
			singers.append(greatness)



	show_singers(singers)



greatness_of_singer=[]
singers=['lata', 'rafi', 'kishor', 'mukesh']
make_great(singers[:])

## Passing Arbitrary Arguments
'''
Sometimes you won’t know ahead of time how many arguments a function needs to accept
python store *parameter as tupple
'''
def make_pizza(*toppings):

	#print(toppings)
	for each in toppings:
		print(each)

make_pizza('paperoni')
make_pizza('mushrooms', 'green paper', 'extra cheese')

# **************Mixing Positional and Arbitrary Arguments***************


def make_piza_with_size(size, *toppings):
	print("\nMaking a " + str(size) + "-inch size piza with following Toppings:")
	for each in toppings:
		print("- " + each )

make_piza_with_size(12, 'mushrooms', 'green paper', 'extra cheese')

# ************************************8 Using Arbitrary Keyword Arguments *********************************

"""
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function. In this case, you can write functions that accept as many key-value
pairs as the calling statement provides.
The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs it
receives into this dictionary. Within the function, you can access the namevalue
pairs in user_info just as you would for any dictionary.
"""

def build_profile(first, last, **user_info):
	# Create a blank dictionary
    profile={}

#	we add the first and last names to
#	this dictionary because we’ll always receive these two pieces of information
#	from the user.
    profile['first_name'] = first
    profile['last_name'] = last

#	loop through the additional key-value pairs in the
#   dictionary user_info and add each pair to the profile dictionary

    for key, value in user_info.items():
	    profile[key] = value

    return profile

user_profile=build_profile('Deepak', 'Manjarekar', location='Malvan', company='Grampanchayay', project='wadachapat')
print(user_profile)

# eg1
def make_sandwitch(sandwitch_type, **ingredeants):
	toppings={}
	toppings['sandwitch'] = sandwitch_type
	for key, value in ingredeants.items():
		toppings[key] = value

	return toppings


sandwithch=make_sandwitch('vegsandwitch', tomato='red', onion='white', cheeze='italian')

print(f"Order details {sandwithch}")

