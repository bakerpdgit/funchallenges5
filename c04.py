# String manipulation
# Made by Ryan Stubbs

word = input("Enter a word: ")

print(f"Your word is {word}.") # this is called an f string and is very handy for printing variables

pos = int(input("Enter an index: "))

char = word[pos] # this line accesses the character in the word at the specified position, note that the first position is position 0!

#### Task 1 - use an f string to print out (in clear English) the position entered and the character at that position

vowels = 0
for i in range(len(word)):
    char = word[i]
    #### Task 2 - modify this print statement to instead print the index along with the character, in the format "Index 0: a"
    print(char)

    ### Task 3 - currently only 'a's and 'e's are counted; modify so that any vowel is counted
    if char == "a" or char == "e":
        vowels += 1

print(f"There are {vowels} vowels in your word.")


# Extension

# What if you want a section of characters from your string. Experiment with the following code and try to understand what is happening!
# You will want to comment the code above. You can do this by highlighting the lines and pressing Ctrl + forward slash on your keyboard


word = "pythoniscool"
print(word[2:4])
print(word[:3])
print(word[1:])
print(word[::2])
print(word[::-1])