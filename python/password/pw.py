#first test for password generator program, starting with letters, punctuation and digis

def checklength(pw):
	return len(pw) >=9

def hasUpper(inputString):
	return any(char.isupper() for char in inputString)

def isDigit(inputString): 
	return any(char.isdigit() for char in inputString)

def hasLower(inputString): 
	return any(char.islower() for char in inputString)

def hasSpec(inputString):
	return any(char.hasspec() for char in inputString)

