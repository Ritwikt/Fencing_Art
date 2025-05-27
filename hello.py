print("Hello, world2!")
assistant_name = "Fencing Art Assistant"
user_name = "Friend"
print("Welcome to the " + assistant_name + "!")
print("Hello, " + user_name + "! Let's create some ASCII art.")

choice = input("What would you like to draw? (sword/mask) ")
#print (choice.lower())
choice = choice.lower()
if choice == "sword":
    print("Great choice! (Sword drawing coming soon...)")
elif choice == "mask":
    print("Awesome! (Mask drawing coming soon...)")
else:
    print("Sorry, I can only draw a sword or a mask.")
