from datetime import datetime
import random
from random import randint
import names

# generate random name
def get_name():
	name = names.get_full_name()
	return name

# generate random birthday
def get_birthdate():
	year = random.choice(range(1950, 2001))
	month = random.choice(range(1,13))
	day = random.choice(range(1,29))
	birth_date = str(month)+"/"+str(day)+"/"+str(year)
	return birth_date

# generate random PHN
def get_PHN():
	PHN = randint(100000000,999999999)	# inclusive at both ends
	return PHN


def create_namelist():
	name_list = []

	for index in range(20):
		name = get_name()
		name_list.append(name)
	return name_list
	#print(name_list)


def create_birthdatelist():
	birthdate_list = []

	for index in range(20):
		birthdate = get_birthdate()
		birthdate_list.append(birthdate)
	return birthdate_list
	#print(birthdate_list)


def create_PHNlist():
	PHN_list = []

	for index in range(20):
		PHN = get_PHN()
		PHN_list.append(PHN)
	return PHN_list
	#print(PHN_list)


def create_query():
	name_list_length = randint(3,7)
	birthdate_list_length = randint(1,3)
	PHN_list_length = randint(2,4)

	name_list = []
	birthdate_list = []
	PHN_list = []

	for index in range(name_list_length):
		name = get_name()
		name_list.append(name)
	print(name_list)

	for index in range(birthdate_list_length):
		birthdate = get_birthdate()
		birthdate_list.append(birthdate)
	print(birthdate_list)

	for index in range(PHN_list_length):
		PHN = get_PHN()
		PHN_list.append(PHN)
	print(PHN_list)

