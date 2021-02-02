import random
from os import system, name

# Change this to True if you want to use names instead of numbers to assign people to pods
# Change to False to just use numbers that you assign to members
NAMED = False

# Other variable stuffs
names = list()
pods = list()
pod = 0

# Clear terminal
# (Windows)
if name == 'nt': 
    system('cls') 
# (Mac/Linux)
else: 
    system('clear') 

print("=== DRG Group divider ===\n")
participants = input("How many people total? ")

try:
    int(participants)
except:
    print("\nInvalid number\n")
    exit(-1)

if NAMED:
    for i in range (int(participants)):
        names.append(input("Enter name: "))
else:
    for i in range (int(participants)):
        names.append(str(i + 1))

while(len(names)):
    remaining = len(names)

    # If 4 or less, make 1 pod
    if remaining <= 4:
        pods.append(names)
        # Clear names to exit loop gracefully
        names = list()

    # Special case of 3/3/3: make a pod of 3 and let the next part deal with the 6
    elif remaining == 9:
        pods.append(list())
        for i in range(3):
            choice = random.randint(0, remaining-1)
            pods[pod].append(names.pop(choice))
            remaining -= 1

    # If less than 7, divide as evenly as possible
    elif remaining < 7:
        pods.append(list())
        num = remaining // 2
        for i in range (num):
            choice = random.randint(0, remaining-1)
            pods[pod].append(names.pop(choice))
            remaining -= 1

    # Otherwise, add 4 random members
    else :
        pods.append(list())
        for i in range(4):
            choice = random.randint(0, remaining-1)
            pods[pod].append(names.pop(choice))
            remaining -= 1

    pod += 1

# Make numerical member lists easier to read
if not(NAMED):
    for i in range(pod):
        pods[i].sort(key=lambda x: int(x))

# Print the results nicely
for i in range(pod):
    print("\nPod " + str(i+1) + ":")
    print(*pods[i], sep=", ")
print()
