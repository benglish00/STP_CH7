#Chapter 7 Loops
# For-Loops - to iterate through an iterable
name = "Ted"

#for loops easy
for character in name:
    print(character)
shows = ["GOT","TWD","Narcos"]
for show in shows:
    print(show)
people = {"Prandtl":"Fluids", "Tesla":"Electricity", "Hubble":"Physics"}
for scientist in people:
    print(scientist)
    print(people[scientist])

# for loop with an index
i=0
for show in shows:
    new = shows[i]
    new = new.upper()
    shows[i] = new
    i += 1
print(shows)

# enumerate to set for-loop
for i, show in enumerate(shows):
    new = shows[i]
    new = new.lower()
    shows[i] = new
print(shows)

# for loops with range
for i in range(3,6):
    print(i)

# WHILE LOOPS
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New year!")

while True:
    print("Hello, World!")
    break

#Continue Statement
for i in range (1,6):
    if i == 3:
        continue
    print(i)

# Challenge 1: Print each item in the following list
tvshows = ["TWD", "The Sopranos", "Rome", "GOT", "Breaking Bad"]
for shows in tvshows:
    print(shows)

# Challenge 2: Print each number from 25 to 50
for i in range(25,51):
    print(i)

#Challenge 3: Print each item from the tvshows list and their index
for i, show in enumerate(tvshows):
    print("{}. {}.".format(i,show))

#Challange 4. Write infinite loop with q to break
num = 55
while True:
    guess = input("Guess a number between 0 and 100. Type q to quit. ")
    if guess == "q":
        break
    try:
        guess = int(guess)
    except ValueError:
        continue

    if guess > num:
        print("Guess lower!")
    elif guess < num:
        print("Guess higher!")
    else:
        print("You got it!")
        break

# Challenge 5. Multiply all the numbers in two lists and make a 3rd list
A = [4, 8, 19, 148]
B = [1, 9, 33, 83]
C = list()
for i, numA in enumerate(A):
    for j, numB in enumerate(B):
        C.append(A[i]*B[j])
        print(C)
