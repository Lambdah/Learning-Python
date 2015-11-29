def start():
	print "You enter a bar. It looks very dark and digusting and some cockroaches run along the floor. What do you do?"
	print "1. You head towards the washroom."
	print "2. Approach the pretty lady at the bar."
	print "3. Sit at the table lonely as you can be."
	
	direction = decision()
	return direction

def washroom():
	print "You head towards the washroom."
	print "When you enter the lights flicker, and the smell of urine is in the room."
	print "What do you do?"
	
	print "1. You enter into the bathroom stall."
	print "2. Just wash your hands."
	
	direction = decision()
	return direction
	
def bathroom_stall():
	print "You are in the bathroom stall, and you sit on the toilet."
	print "You got cold feet, and never leave until the bar closes."
	
def wash_hands():
	print "You wash your hands, tidy up your hair, and head back."
	start()
	
def pretty_lady():
	print "You sit beside her. What do you do?"
	print "1. Buy her a drink"
	print "2. Try to start up a conversation"
	print "3. Just sit and say nothing"
	
	direction = decision()
	return direction
	
def buy_drink():
	print "You purchase her a drink. Martini shaken not stirred she drinks similar to James Bond."
	print "You strike up a conversation, and it goes well."
	print "Seems like your getting lucky tonight."

def conversation():
	print "She's aloof to why you trying to talk to her."
	table()
	
def table():
	print "You sit, nothing happens and the night ends. You go home."

def decision():
	
	while True:
		print "Please, enter your decision",
		decide = raw_input(": ")
		if decide.isdigit():
			return decide
	
	
		
beginning = start()

if beginning == "1":
	decision1 = washroom()
	if decision1 == "1":
		bathroom_stall()
	elif decision1 == "2":
		wash_hands()
	else:
		print "You got confused and just stand there."
elif beginning == "2":
	decision2 = pretty_lady()
	if decision2 == "1":
		buy_drink()
	elif decision2 == "2":
		conversation()
	else:
		table()
else:
	decision3 = table()