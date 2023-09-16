# ------------------------------------------------------------
#    This is the interactive menu for the wordlist generator
# ------------------------------------------------------------
import datetime

print('Wordlist Generator')
print('Based off the Bopscrk word generator')

# Global variables
minLength = input("Password Min Length[4]:~> ") or 4                   #Min Password Length
maxLength = input("Password max length[15]:~> ") or 15                 #Max Password Length

# Leet transformation option
while True:
    leet_transform = input("Do you want to make l33t transformations? [Y/N]:~> ").upper()
    if leet_transform == 'Y':
        l33tTransform = True
        break
    elif leet_transform == 'N':
        l33tTransform = False
        break
    else:
        print("Invalid Input. Please input Y or N")

# Case Transformation option
while True:
    case_transform = input("Do you want to make case transformations? [Y/N]:~> ").upper()
    if case_transform == 'Y':
        caseTransform = True
        break
    elif case_transform == 'N':
        caseTransform = False
        break
    else:
        print("Invalid Input. Please input Y or N")

# Word Combinations
wordCombinations = input("How many words do you want to combine at most?:~> ")

# Output file
outputFile = input("Output file [output.txt]:~> ")

# Check output file
outputFile = outputFile.strip()
if not outputFile.endswith('.txt'):
    outputFile += '.txt'

class GetInputs:
    def __init__(self):
        self.firstname = input("Targets Firstname?:~> ")            #Firstname
        self.surname = input("Targets Surname?:~> ")                #Surname
        self.lastname = input("Targets lastname?:~>  ")             #Lastname

        # Birthday input check
        while True:
            birthday = input("Targets DOB (MM/DD/YY):~> ")
            try:
                datetime.datetime.strptime(birthday, '%m/%d/%Y')
                break
            except ValueError:
                print("Invalid format. Please enter the DOB in the format (MM/DD/YYYY):~> ")
        self.birthday = birthday



        # Relevant words splitter
        relevant_words = input("Enter relevant words (comma-separated):~> ")
        self.relevantWords = [word.strip() for word in relevant_words.split(',')]

    def paramList(self):
        return [self.firstname, self.surname, self.lastname, self.birthday, self.relevantWords]