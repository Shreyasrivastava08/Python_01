
#divisible by 3 and 5
for i in range(1, 101):
    if (i % 3 == 0) ^ (i % 5 == 0):  # XOR ensures only one condition is true
        print(i, end=" ")

#reverse
sentence = "Python is fun"
word = ""
words = []


for ch in sentence:
    if ch == " ":
        words.append(word)
        word = ""
    else:
        word += ch
words.append(word)

#
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

#pattern printing
def pattern(n):
   for i in range(1, n+1, 2):
      spaces = (n-i)//2
      print(" " *spaces + "*" * i)
pattern(5)

#count consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Example
text = "hello world"
print("Number of consonants:", count_consonants(text))

#number guessing game

key = 8

while True:
    guess = int(input("Guess the number: "))
    if guess == key:
        print("Correct! You guessed it :)")
        break
    else:
        print("Wrong try again :/")