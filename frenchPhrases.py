# Keep your imports at the top. It's good practice as it tells anyone reading your code what the program relies on
from sys import argv, exit
from random import randint
import json

def play(data):
	"""Start the game with the list of sentences provided

	data -- list of sentences
	"""

	while True:
		sentencePick = randint(0, len(data) - 1) # Pick a random sentence index
		languages = list(data[sentencePick].keys()) # Dynamically pull out the list of languages for that sentence
		langPick = languages[randint(0, len(languages) - 1)] # Picks a random language

		languages.remove(langPick) # Remove langPick from the list of languages

		for lang in languages: # Loop over the remaining languages
			userAnswer = input('What is the ' + lang + ' translation of "' + data[sentencePick][langPick] + '"?\n> ')

			if userAnswer == data[sentencePick][lang]:
				print('Correct')
			else:
				print('Wrong, the answer was: "' + data[sentencePick][lang] + '"')
				exit(1)

def addSentence(path):
	"""Write a new sentence to a file

	path -- file to amend
	"""

	f = open(path, 'r') # Open file in read mode
	data = json.load(f) # Get the list of sentences
	f.close() # Close the file

	sentence = getSentence() # See function below

	data.append(sentence) # Append the list of sentences with the new sentence dictionary returned by getSentence

	f = open(path, 'w+') # Open and wipe the file
	f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))) # Write the amended list of sentences to the file
	f.close()
	exit(0)

def getSentence():
	"""Return a dictionary containing a sentence in different languages"""

	sentence = {}
	languageCount = int(input('How many languages?\n> '))

	for i in range(0, languageCount):
		language = input('Enter language nb ' + str(i + 1) + '\n> ')
		sentence[language] = input('What is the sentence for that language?\n> ')

	return sentence

if len(argv) > 2 and argv[1] == 'add': # If user entered 'python script add filename'
	addSentence(argv[2])
elif len(argv) > 1: # If user entered 'python script filename'
	data = json.load(open(argv[1])) # Assign the dictionary contained in the file to data
	play(data)
else:
	print('Syntax: [add] filename')
	exit(1)
