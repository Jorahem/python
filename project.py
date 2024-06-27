import getpass

print("Rock, Paper, Scissors")
print("Enter R for Rock, P for Paper, S for Scissors")

first_player = input("Enter the first player's name: ")
second_player = input("Enter the second player's name: ")

p1_command = getpass.getpass(f"{first_player}, enter your command: ").strip().lower()
p2_command = getpass.getpass(f"{second_player}, enter your command: ").strip().lower()

if (p1_command == "r" and p2_command == "p"):
    print(f"{second_player}, you win")
elif (p1_command == "p" and p2_command == "r"):
    print(f"{first_player}, you win")

elif (p1_command == "s" and p2_command == "r"):
    print(f"{second_player}, you win")
elif (p1_command == "r" and p2_command == "s"):
    print(f"{first_player}, you win")

elif (p1_command == "s" and p2_command == "p"):
    print(f"{first_player}, you win")
elif (p1_command == "p" and p2_command == "s"):
    print(f"{second_player}, you win")

elif (p1_command == p2_command):
    print("It's a tie!")

else:
    print("Invalid input. Please enter R, P, or S.")
