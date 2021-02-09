def username(email):
	uname = email[:email.index("@"):]

	return uname

def domain(email):
	dom = email[email.index("@")+1:]

	return dom