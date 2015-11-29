#################################################
#This is a text based game to try to rob a bank #
#November 23, 2015                              #
#I played too much GTA V at this time           #
#Author: Lambdah    Date:Nov28  Ver: 1.0        #
#################################################

# First element is money and the rest will be items that append in the array
backpack = [0] 
robbed = False

def start(backpack):
	print "You have just got out of prison, and have released out of prison."
	print "It's hard finding work now because all employers look at your criminal past and fire you."
	print "Debt is owed to some evil mobsters that wouldn't bat an eye if you were to disappear."
	print "The only option now is to rob places until you have $1 million."
	car(day_night(True),backpack) # sets the cycle to start off as night

def day_night(wait):
# This function deals with the day and night cycle of the game
# night is true and day is false
	if wait == True:
		cycle = "night"
		return cycle
	else:
		cycle = "day"
		return cycle
	
def add_item(cash, item):
	item_added = backpack
	items = False
	if item_added[0] > 0 and item is not None:
		item_added.append(item)
		print "%s added to your inventory." % item
		item_added[0] += cash
		items = True
	elif cash:
		item_added[0] += cash
		print "$%d is added to your wallet" % cash
	else:
		print "You cannot afford this."
	return items
	
def die(why):
	# The kill function.
	print "%s Game over." % why
	raw_input("")
	exit(0)
	
def car(cycle, backpack):
	# Location character always returns to
	print "There's several locations you can drive to:"
	print "1. Gun store\n2. Bar\n3. Bank\n4. Hacker\n5. Convenience Store"
	print "You can also ask for tooltip help, items or wait."
	while True:
		print "\nYou are in your car at %stime. What to do..." % (cycle)
		choice = raw_input("> ")
		if "gun" in choice or choice == "1":
			gun_store(cycle, backpack)
			
		elif choice == "item" or choice =="items":
			print "\nThe items you got are:"
			for item in backpack:
				print item
		elif "wait" in choice:
			print "\nTime itself ticks away."
			if cycle == "night":
				car(day_night(False), backpack)
			else:
				car(day_night(True), backpack)
		elif "location" in choice:
			print "Places to go:"
			print "1. Gun store\n2. Bar\n3. Bank\n4. Hackers\n5. Convenience Store"
			print robbed
		elif choice == "exit":
			die("exit")
		
		elif choice == "4" or "hacker" in choice:
			hackers(cycle, backpack)
		elif choice == "2" or "bar" in choice:
			bar(cycle, backpack)
		elif choice == "5" or "store" in choice:
			convenience_store(cycle, backpack)
		elif choice == "3" or "bank" in choice:
			bank(cycle, backpack)
			
			
def gun_store_stock(gun_stock):
#outputs the guns that are in stock
	count = 1
	for guns in gun_stock:
		print str(count) + ". $",
		for item in guns:
			print item,
		count += 1
		print "\n",
	
def gun_store(cycle,backpack):
# The gun store to be able to purchase guns
	gun_stock = [[500,"Handgun"], [150, "Metal Flashlight"], [50, "Bear Mace"]] # first item in the second array is the cost of the item
	list = []
	if cycle == "night":
		print "The gun store is closed.\nCome back when it's daytime.\nYou go back to your car.\n"
	elif cycle == "day":
		print "You enter the gunstore. What do you want to purchase?\n"
		print "Our current items in stock are:\n"
		gun_store_stock(gun_stock)
		while True:
			print "Type \"car\" to go back to your vehicle."
			purchase = raw_input("> ")
		
			if purchase == "handgun" or purchase == "1":
				x = add_item(-500, "Handgun")
				if x == True:
					gun_stock.pop(0)	
		
			elif "flashlight" in purchase or "metal" in purchase or purchase == "2":
				x = add_item(-150, "Metal Flashlight")
				if x == True:
					gun_stock.pop(1)
					
			elif "bear" in purchase or purchase == "3":
				x = add_item(-50, "Bear Mace")
				if x == True:
					gun_stock.pop(2)
				
			elif purchase == "gunstock":
				gun_store_stock(gun_stock)
			
			elif purchase == "car" or purchase == "return":
				car(cycle, backpack)
		
			else:
				print "I didn't catch that. Inputting \"gunstock\" will make show our stock."
				
def bar(cycle, backpack):
#Visiting the bar, gets the ladies ID to break in the bank.
	if cycle == "night":
		cowlick = True
		information = False
		print "You enter the bar. The smells of cigarettes, and wide screen TVs are everywhere."
		while True:
			print "Where do you head?\n1. To the wash room\n2. To the empty table\n3. Towards the girl with an empty stool beside her\n4. Back to the car."

			decision = raw_input("> ")
			if decision == "washroom" or decision == "1":
				print "You head towards the washroom, and add some water to your hair to calm down that cowlick."
				cowlick = False
			elif "table" in decision or decision == "empty table" or decision == "2":
				print "You sit at the empty table.\nThe waitress approaches you casually and asks what you want?\n\t1. You order a beer\n\t2. Offer the waitress some money for information about the girl."
				choice = raw_input("> ")
				if (choice == "beer" or choice == "1") and backpack[0] > 0:
					add_item(-50, None)
					print "You get completely drunk, and waste the night away on beers(You forgot your an alcoholic)."
					car(day_night(True), backpack)
				elif (choice == "2" or "information" in choice) and backpack[0] > 0:
					add_item(-150, None)
					information = True
					print 'The waitress says "That girl sitting over there works as a teller for the bank, always complaining about customers.\nShe usually sits by herself every night and unwinds with a sangria."'
				else:
					print "You do not have enough money, honey."
			elif decision == "girl" or decision == "3":
				print "You sit beside her."
				if cowlick is False and information is True:
					print "You order her a sangria and she thought your attractive enough to keep her company.\nYou two talk all night and she ends up walking to the washroom.\nYou go through her purse.\nYou get her employee ID at the bank.\nYou quickly put away the phone and can commence the break in to the bank, remember though her name is \"Kelly\"."
					add_item(-300, "Employee ID")
					car(day_night(False), backpack)
				else:
					print "'Don't you look like a pretty boy?' she said sarcastically"
					die("She does not care much for unkept men or men that does not know what women want")
			elif "car" in decision or decision == 4:
				car(cycle, backpack)
				
	else:
		print "Bar is not open"
	
def hackers(cycle, backpack):
#Have to talk to the hacker to get some extra cash if you have none, also he gets the safe combination.
	if cycle == "day":
		print "You approach the house of the computer hacker.\nYou hear a sudden noise from the intercom \"What's the password\""
		password = raw_input("> ")
		if "" in password:
			print "Ha, there was no actual password. I already knew it was you from the cameras."
			if "Employee ID" not in backpack:
				print "Well come in, we have big plans for this bank.\nThere's a certain lady certain lady at a bar, you have to woo to get the banks information.\nI already found out which safe they use and its serial ID but I need you to get her name, and ID.\nCan you do that for me? Good.\n"
				if backpack[0] == 0:
					add_item(300, None)
					print "This should help you out.\nYou return back to your car."
				else:
					print "You return to your car."
			elif "Employee ID" in backpack:
				print "Very good, we have the necessary information to start the job.\nLet us start by getting the combination.\nI am phoning the manufacturing, quick what is her name?"
				name = raw_input("> ")
				if "kelly" in name or "Kelly" in name:
					print "Very good I got the combination. It is 95-21-8-36 go to the bank and rob it, Remember it.\nDo not forget to bring some sort of weapon to incapcitate the bank employees."
				else:
					die("The bank managed to track your information and imprison you.")
	else:
		print "No one answers. You should come back during the day."
		
def convenience_store(cycle, backpack):
#Gets some much needed extra cash if you have the right weapons.
	global robbed
	if robbed == False:
		if cycle == "night":
			print "You can rob the store at night if you have a metal flashlight in your backpack.\n1. Rob the store\n2. Return back to the car"
			decision = raw_input("> ")
			if "Metal Flashlight" in backpack and ("rob" in decision or "1" in decision):
				print "You rob the store and manage to steal $1000"
				add_item(1000, None)
				robbed = True
				return robbed
			else:
				print "Some equipment is required to rob. You go back to the car."
		elif cycle == "day":
			print "You can rob the store with your bear mace or handgun.\n1. Rob the store\n2. Return back to the car"
			decision = raw_input("> ")
			if "rob" in decision or "1" in decision:
				if "Handgun" in backpack:
					print "You manage to rob $700"
					add_item(700, None)
					robbed = True
					print robbed
					return robbed
				elif "Bear Mace" in backpack:
					print "You manage to rob $400"
					add_item(400, None)
					robbed = True
					return robbed
				else:
					die("You failed to rob the store. You end up going to jail.")
			elif "car" in decision or decision == 2:
				print "You go back to the car."
			else:
				print "You will need some equipment to rob. You go back to your car."
	else:
		die("You never return back to the crime scene.")
		
def safe_combination():
	print "Input the combination for the safe, one input at a time."
	input_combo = []
	for combo in range(0,4):
		combo = int(raw_input("> "))
		input_combo.append(combo)
	return input_combo
	
def bank(cycle, backpack):
#Breaking into the bank for the ultimate goal
	combination = [95, 21, 8, 36]
	if cycle == "night":
		if "Metal Flashlight" in backpack and "Bear Mace" in backpack:
			print "You sneak in the bank, mace the security guard."
			combo = safe_combination()
			if combo == combination:
				add_item(1000000, None)
				print "You got enough money to pay off those mobsters. Excellent."
				raw_input("")
				exit(0)
			else:
				die("The alarm was tripped and you got caught.")
		else:
			print "You will need a flashlight and something to incapcitate the security guard. Do not kill him though."
	elif cycle == "day":
		if "Handgun" in backpack:
			print "You wave your gun at the employees and make them move into the corner."
			combo = safe_combination()
			if combo == combination:
				add_item(50000, None)
				die("The silent alarm was tripped, you still manage to take away some money but not the entire loot.")
			else:
				die("The silent alarm was tripped, and you took too long to get the money.")
		else:
			print "You will need some at least a gun to start robbing the bank."
				
start(backpack)