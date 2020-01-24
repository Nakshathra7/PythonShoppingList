import json

menuOption = None

menuText = '''
1. Add Item
2. Print List
3. Remove Item by Number
4. Save List to File
5. Load List from File
6. Exit
'''

print(menuText)

shopeeList = []


while menuOption != 6:
	try:
		menuOption = input("Enter Selection\n")
	except Exception as e:
		print("Could not process." + str(e))

	if menuOption == '1':
		print("Add Item")
		try:
			count = int(input("Enter the Shopping List Item Count : "))
			duplicate = None
			if duplicate == None:
				for i in range(0, count):
					print("Enter Item ", i + 1, ":")
					try:
						item = (input())
						
					except Exception as e:
						print("Enter Valid Input ", str(e))
					if shopeeList.count(item) > 0:
						print('Item Already Exists in List. Enter New Item')
						duplicate = 1
						break
					else:
						shopeeList.append(item)

				print("Shopping Item List is ", shopeeList)
		except Exception as e:
			print("Enter Valid Input ", str(e))

	elif menuOption == '2':
		print("Print Shopping List:")
		i = 0
		sortShopeeList = sorted(shopeeList)
		while i < len(sortShopeeList):
			print(i+1,sortShopeeList[i])
			i += 1

	elif menuOption == '3':
		print("Remove Item by Number")
		sortShopeeList = sorted(shopeeList)
		print(sortShopeeList)
		while i < len(sortShopeeList):
			print(i + 1, sortShopeeList[i])
			i += 1
		removeCount = int(input("Enter the Shopping Item Number for Removal : "))
		shopeeList.remove(sortShopeeList[removeCount-1])
		sortShopeeList.remove(sortShopeeList[removeCount - 1])
		print("Updated Shopping List Item: ",shopeeList)

	elif menuOption == '4':
		print("Save List to File")
		with open('shoplistfile.txt', 'w') as filehandle:
			json.dump(sortShopeeList, filehandle)
	elif menuOption == '5':
		print("Load List from File")
		with open('shoplistfile.txt', 'r') as filehandle:
			sortShopeeList = json.load(filehandle)
		print(sortShopeeList)
	elif menuOption == '6':
		print("Exit")
		break
	else:
		print("Your Selection was not recognized")
		break