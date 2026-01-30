import random
import string

symbols = list(string.punctuation)
numbers = list(map(str, [0,1,2,3,4,5,6,7,8,9])) #converts int element into str element or simply enclosed it with ""
letters = []

lowerCase_letters = list(string.ascii_lowercase) #contains all lowercase letters and put it inside a list
for letter in lowerCase_letters: #loop to itterate every element in the list
    letters.append(letter) #add elements to the letter list
upperCase_letters = list(string.ascii_uppercase) #contains all uppercase letters and put it inside a list
for letter in upperCase_letters:
    letters.append(letter)

print("Welcom to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

password_characters = []
for char in range (0, letters_count): #loop nth times using "range(start, end)"
    password_characters.append(random.choice(letters)) #randomly selects an element "random.choice()" and add it in the list "append()"

for char in range(0, symbols_count):
    password_characters.append(random.choice(symbols))

for char in range(0, numbers_count):
    password_characters.append(random.choice(numbers))
    
print(f"Possible Password Characters: {password_characters}")

password = [] #can be simplified using the random.shuffle()
for char in range(0, len(password_characters)):
    random_character = random.choice(password_characters)
    password.append(random_character)
    char_index = password_characters.index(random_character) #returns the index of passed element "index()"
    password_characters.pop(char_index) #removes the element based on the index

final_password = "" 
for char in password: #put every element into the string variable
    final_password += char
    
print(f"Your password is: {final_password}")



