# sorted.py
# More on the sorted function

# Sort the words from a sentence
sentence = "I like turtles, especially purple ones"
# Notice words aren't sorted correctly!
print(sorted(sentence.split()))

# Now they are
# Note the key= at the end
print(sorted(sentence.split(), key=str.upper))

