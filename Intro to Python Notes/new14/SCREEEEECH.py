
def NameRepairing(name):
	#Make the first characater of name uppercase, assign it to fixedName 
	fixedName = name[0].upper()

	#from the second element of name
	for i in range(0,len(name)-1):
		#if the character of [i] in name is a space
		if name[i] ==' ':
			#making the character of [i+1] uppercase, adding it to fixedName, 
			fixedName  += name[i+1].upper()
		else:
			#making the character of [i+1] lowercase, adding it to fixedName
			fixedName += name[i+1].lower()

	#return fixedName
	return fixedName

    
def main():
	print("Enter a full name:")
	name =input()
	print("The repaired name: ", NameRepairing(name))

main()
