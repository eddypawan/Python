sentence = input("Enter a sentence: ")

# Initialize counters
char_count = 0
word_count = 0
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

# Loop through each character in the sentence
for char in sentence:
    if char.isalpha():
        char_count += 1
        if char.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
    elif char.isdigit():
        char_count += 1
        digit_count += 1
    elif char != " ":
        char_count += 1
        special_count += 1

# Count the number of words
word_count = len(sentence.split())

# Calculate percentages
uppercase_percent = (uppercase_count / char_count) * 100
lowercase_percent = (lowercase_count / char_count) * 100
digit_percent = (digit_count / char_count) * 100
special_percent = (special_count / char_count) * 100

# Print out the results
print("Number of characters (excluding spaces):", char_count)
print("Number of words:", word_count)
print("Percentage of uppercase letters: {:.0f}%".format(uppercase_percent))
print("Percentage of lowercase letters: {:.0f}%".format(lowercase_percent))
print("Percentage of digits: {:.0f}%".format(digit_percent))
print("Percentage of special characters: {:.0f}%".format(special_percent))
sentence = input("Enter a sentence: ")

# Initialize counters
char_count = 0
word_count = 0
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

# Loop through each character in the sentence
for char in sentence:
    if char.isalpha():
        char_count += 1
        if char.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
    elif char.isdigit():
        char_count += 1
        digit_count += 1
    elif char != " ":
        char_count += 1
        special_count += 1

# Count the number of words
word_count = len(sentence.split())

# Calculate percentages
uppercase_percent = (uppercase_count / char_count) * 100
lowercase_percent = (lowercase_count / char_count) * 100
digit_percent = (digit_count / char_count) * 100
special_percent = (special_count / char_count) * 100

#new

# Print out the results
print("Number of characters (excluding spaces):", char_count)
print("Number of words:", word_count)
print("Percentage of uppercase letters: {:.0f}%".format(uppercase_percent))
print("Percentage of lowercase letters: {:.0f}%".format(lowercase_percent))
print("Percentage of digits: {:.0f}%".format(digit_percent))
print("Percentage of special characters: {:.0f}%".format(special_percent))
