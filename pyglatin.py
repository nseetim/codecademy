# This script is the python version of the game you already know, dont know the name
pyg = 'ay' 

original = raw_input('Enter your word:')
"""
Check if the user actually entered a word and if the word entered contains any integer
if it does contain an integer then it prints a message as seen below
"""
if len(original) > 0 and original.isalpha(): 
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'please enter a word without integers and any other funny characters '
