#4.Match all the phone numbers in usa

#Checking the modifications on GIT hub

def phone_match(phone):
	pat =re.compile('(^\([1-9][0-9][0-9]\)\\s?[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9])')
	result = pat.match(phone)
	print result 

a = raw_input("Please, enter your  phone")#(408) 984-5561 or (408)984-5561
phone_match(a)
