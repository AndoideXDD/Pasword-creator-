import string
from io import open
from time import sleep 
import keyboard
import pyautogui as pa 
from tqdm import tqdm
import psutil


lenghpasword = int(input("Put the lengh of the words in numbers: "))

# This part generete the paswords 

Alphabet = list(string.ascii_lowercase)
# This for change what it crraks (optional)
   #Alphabet = list(range(10))
# This for add what it crraks (optional)
# This line add numbers 
for number in list(range(10)):
	Alphabet.append(number)

# This line add upper letters
for letter in list(string.ascii_uppercase):
	Alphabet.append(letter)


# The number of all leters, numbers that can be at the pasword (because I use only the alphabet are 26) 
numberOfItems = len(Alphabet)




# Creates an object for generate possible paswords

class Generator():
	
	def __init__(self):
		

		# Save the things that can be at the pasword
		self.PASWORDSS = Alphabet
		# It is for calculate when the memory is full ech 10000 times
		self.CheckMemory = 0
		self.lenOfthePasword = 5
	#Cretes a function for the object that for each time is used calculates 
	#the possible paswords for the next lengh 
	def create(self):
		# This for save the pasewords whe are the data to much for the computer and is writen at a txt 
		# clening her data at the code so the RAM do not explode 
		NewPaswords = []
		# this is for generate the diferent txt that are neded 
		FilesOfPaswords = 1
		# tqdm for the bar of percentage at pip 
		# Add one lengh to the paswords 
		for oneCharacter in tqdm(self.PASWORDSS):
			for secondCharacter in Alphabet: 
				# It is neded this because chek the memory each time makes very slow the code 
				self.CheckMemory = self.CheckMemory + 1
				# Save the paswords generated 
				NewPaswords.append(str(oneCharacter)+str(secondCharacter))
				
			# if the memory is at more than 70 save the paswords at a txt 
			# It is neded (if self.CheckMemory >= 10000:) 
			# because chek the memory each time makes very slow the code 
			if self.CheckMemory >= 10000: 
				self.CheckMemory = 0 
				# psutil.virtual_memory()[2] gives the percentage of RAM used 
				if psutil.virtual_memory()[2] >= 70:
					# Creates the file 
					passwords_file = open(str(FilesOfPaswords)+str(lenghpasword)+"paswords.txt","w")

					# Here the data is saved at a txt
					for pasword in tqdm(NewPaswords):
						
						
						passwords_file.write(pasword)
					# Cleans the things
					NewPaswords = []
					passwords_file.close()
					self.CheckMemory = 0 
					# This is for create a new txt after because if not it will rewrite the same file 
					FilesOfPaswords = FilesOfPaswords + 1 

		self.PASWORDSS = NewPaswords

	def createDigitsBiggerThan5(self,fileName,firsthalf):



		#Now that we have a lot of data que will do it in base of files instead of the variable 

		def reedPaswords():
			
			# Reads the file 

			passwords_file = open(fileName,"r")

			#Gets the data and close it 

			AllPosiblePasswords = passwords_file.read()
			passwords_file.close()

			
			# The counter is for calculate the number of times that have pass with out get the pasword
			# When it arrives to the pasword lengh it is restarted
			counter = 0

			# This save the paswords individuali temporaly 

			Apassword = ""

			# Here is all paswords saved and returned

			Paswords = []

			# tqdm is for show the bar of percentage at the cmd (the consol)
			for leter in tqdm(AllPosiblePasswords):
				# The counter is for calculate the number of times that have pass with out get the pasword
				
				counter = counter + 1 
				# This save the paswords individuali temporaly 
				Apassword = Apassword + leter
				# When it arrives Apassword to the pasword lengh it is restarted and save the pasword
				if counter == self.lenOfthePasword:

					counter = 0
					
					Paswords.append(Apassword)

					Apassword = ""

			# this for the future updates 

			self.lenOfthePasword = self.lenOfthePasword +1

			# slpits in two the paswords 

			if firsthalf == True: 
					
				def split_list(a_list):
					half = len(a_list)/2
					half = int(half)
					return a_list[:half], a_list[half:]

				Paswords,ForNextLoop = split_list(Paswords) 

				ForNextLoop = []

			else:

				def split_list(a_list):
					half = int(half)
					half = len(a_list)/2
					return a_list[:half], a_list[half:]


				A,Paswords = split_list(Paswords) 

				A = []
			#returns the paswords (but half of them)
			return Paswords

		#_____________________________________________________________________________________________________________

		# This for save the pasewords whe are the data to much for the computer and is writen at a txt 
		# clening her data at the code so the RAM do not explode 
		self.PASWORDSS = reedPaswords()
		NewPaswords = []
		# this is for generate the diferent txt that are neded 
		FilesOfPaswords = 1
		# tqdm for the bar of percentage at pip 
		# Add one lengh to the paswords 
		for oneCharacter in tqdm(self.PASWORDSS):
			for secondCharacter in Alphabet: 
				# It is neded this because chek the memory each time makes very slow the code 
				self.CheckMemory = self.CheckMemory + 1
				# Save the paswords generated 
				NewPaswords.append(str(oneCharacter)+str(secondCharacter))
				
			# if the memory is at more than 70 save the paswords at a txt 
			# It is neded (if self.CheckMemory >= 10000:) 
			# because chek the memory each time makes very slow the code 
			if self.CheckMemory >= 10000: 
				self.CheckMemory = 0 
				# psutil.virtual_memory()[2] gives the percentage of RAM used 
				if psutil.virtual_memory()[2] >= 90:
					# Creates the file 
					print("\nCreating the file "+str(FilesOfPaswords)+str(lenghpasword)+"paswords.txt"+"\n" )
					passwords_file = open(str(FilesOfPaswords)+str(lenghpasword)+"paswords.txt","w")

					# Here the data is saved at a txt
					for pasword in tqdm(NewPaswords):
						
						
						passwords_file.write(pasword)
					# Cleans the things
					NewPaswords = []
					passwords_file.close()
					self.CheckMemory = 0 
					# This is for create a new txt after because if not it will rewrite the same file 
					FilesOfPaswords = FilesOfPaswords + 1 






		# This is for save the paswords at self.PASWORDSS

		self.PASWORDSS = NewPaswords



generate = Generator()


# This create the paswords with the lengh that we want	
if lenghpasword<=5:
	for PasswordsLengh in range(int(lenghpasword)-1):
		generate.create()
	
if lenghpasword>5:

	print("This much data for do it at one so you need to expand the especific file you want\n")


	anwer = input("Do you created the files ? If you have them put Y if not put N: ")
	if anwer=="Y":

		fileNAme = input("\nWhich file do you want to use for crete the paswords?\n")
		print("Reading the file ... \n")
		for PasswordsLengh in range(int(lenghpasword)-5):
			generate.createDigitsBiggerThan5(fileNAme,True)
			generate.createDigitsBiggerThan5(fileNAme,False)


	if anwer=="N": 

		for PasswordsLengh in range(4):
			generate.create()
            
        
    
 




print("Is done in :  ")

# This part save the paswords that are left 
NameofThefile = str(lenghpasword) + "passwords" + ".txt"
passwords_file = open(NameofThefile,"w")

for pasword in tqdm(generate.PASWORDSS):
	passwords_file.write(str(pasword))