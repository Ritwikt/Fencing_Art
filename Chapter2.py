# Chapter 2: If/Else for Sword or Mask
choice = input("What would you like to draw? (sword/mask) ")
if choice.lower() == "sword":
    print("O=====>")
elif choice.lower() == "mask":
    print(" ______\n| .  . |\n| ---- |\n|______|")
else:
    print("Sorry, I can only draw a sword or a mask.")
