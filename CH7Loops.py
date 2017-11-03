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

