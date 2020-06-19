import string, random #module that consists of all character such as lowercase, uppercase , number and special characters

#module that generate the strings in a random manner

def main(userInput): # a function to generate a password based on how many characters a user wishes to have

#character will be generated based on the length of the user input
    specialCharacter = [random.choice(string.punctuation) for character in range(userInput)] # a list of random special 
    wordLower = [random.choice(string.ascii_lowercase) for lower in range(userInput)] 
    wordUpper = [random.choice(string.ascii_uppercase) for upper in range(userInput)]
    numbers = [random.choice(string.digits) for number in range(userInput)]

    generatedPassword = ''.join(specialCharacter + wordLower + wordUpper + numbers) #The join() method provides a flexible way to create strings from iterable objects
    generatedPassword = ''.join(random.choice(generatedPassword) for value in range(userInput)) # a loop is then exucuted from a list to choose the random characters from the list
    return generatedPassword

print("Welcome to our Random password Generator")
print("Generating Random password with letters, digits and special characters of 12 characters")

question = int(input('Please enter the password length: ')) #we have a input function to ask the user to enter the length of the password he/she wishes to have generated
answer = main(question) # here we have the password function that has been passed with the question variable as the argument which is stored in a variable

if question < 12:
    print("The password cannot be returned, please enter a valid entry")
else:
    print("This is your password:", answer)
