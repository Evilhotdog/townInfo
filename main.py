import csv
def createList():
	#take the csv file and convert it to a list of lists
	with open("townInfo.csv","r") as read_obj:
		csv_reader = csv.reader(read_obj)
		townInfoList = list(csv_reader)
	return (townInfoList)
def find():
	townInfoList = createList()
	a = False
	while a == False:
		noOfResults=0 #sentry variable
		#establish the variable the user wants to search by
		selection = str(input("What do you want to search by? Town, county, population, or area? \n")).lower()
		for header in range(len(townInfoList[0])):
			#print (header)
			if (selection).title() == townInfoList[0][header]:
				#print (str(header)+" is correct")
				a = True
				break
		else:
			#Notify user that thing that they are searching by is invalid	
			print ("No such term found. Please try again.") #Notify user that thing that they are searching by is invalid	
	whatInfo = input("What "+selection+" are you looking for? ").title()#asks for search term, regardless of what user is searching by
	for eachItem in range (len(townInfoList)):
		if whatInfo == townInfoList[eachItem][header]:
			noOfResults = noOfResults+1 #works out number of entries by number of times search term has found result
			print ("Entry "+str(noOfResults)+": ")#marks each result numerically
			for i in range(len(townInfoList[0])): #used len(townInfo[0]) instead of 4 so that array can be expanded without changing code. You could add a fifth value onto each mini-array with no change to code necessary and everything would still function
				print (str(townInfoList[0][i])+": "+str(townInfoList[eachItem][i]))#single line of code gives description (whether the data presented is town name, county name, etc) for all cases, instead of putting it into four seperate lines]
	if noOfResults == 0:
		print ("Sorry, no results found.")

def add():
	cont = "No"
	townInfoList = createList()
	#print (townInfoList)
	while cont not in ["Yes","Y"]:
		newTown = []
		for i in townInfoList[0]:
			newTown.append(str(input(i+": ")).title())
		cont = input("Is this correct? \n"+str(newTown)+"\n").title()
		if cont in ["Yes","Y"]: 
			with open ('townInfo.csv','a') as write_obj:
				seperator = ","
				write_obj.write(seperator.join(newTown)+"\n")
			
def full():
	townInfoList = createList()
	for i in townInfoList[1:]:
		print("")
		for j in i:
			print (j)


goAgain = "Yes"
while goAgain in ["Yes","Y"]:
	while True:
		selection2 = int(input("What would you like to do? 1 to find an entry. 2 to add an entry. 3 to print the whole table \n"))
		#makes me wish python had switch statements
		if selection2 == 1:
			find()
			break
		elif selection2 == 2:
			add()
			break
		elif selection2 == 3:
			full()
			break
		else:
			print ("That is not a valid selection. Please try again. ")
	goAgain = input("Would you like to go again?\n").title()
print ("Thank you for using townInfo!")

