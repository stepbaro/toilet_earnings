# -*- coding: utf-8 -*-
#Find out how much you earn on the toilet in work time!

currency = raw_input("Do you earn in %s or $") % p
p = unichr(163)

if currency == '/£':
	print "calculations will take place in %s Sterling" % p
else:
	print "calculations will take place in US$"

	wage()

#calculate earnings
def wage_calc():
	salary = raw_input("How much do you earn? %s") % currency
	days = raw_input("How many days a week do you work? ")
	hours = raw_input("How many hours a day do you work? ")
	

