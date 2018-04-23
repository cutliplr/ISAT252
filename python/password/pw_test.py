#test for password length
# import code for testing
from pw import checklength, hasUpper, isDigit, hasLower, hasSpec

def test_smoke():
	assert True == True
#create an instance of password
#check whether length is at least 9 characters
def test_length():
	assert checklength('lovedogs101') == True
	assert checklength('bob') == False
#check if password has an uppercase letter
def test_uppercase():
	assert hasUpper('GoDukes1998') == True
	assert hasUpper('iloveisatomg') == False
#check if password has a number
def test_numbers():
	assert isDigit('IlikeNoodles223') == True
	assert isDigit('NoYoudontugh') == False
def test_lowercase():
	assert hasLower('CopperBoom1!') == True
	assert hasLower('IAMYELLINGRN44') == False
def test_specialchar():
	assert hasSpec('HereIsmycode123!!') == True
	assert hasSpec('oKiMadethisright49') == False 