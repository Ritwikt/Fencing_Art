# Chapter 4: Functions
def draw_sword():
    blade = "=" * 5
    print("O" + blade + ">")

def draw_mask():
    print(" ______")
    print("| .  . |")
    print("| ---- |")
    print("|______|")

choice = input("What would you like to draw? (sword/mask) ")
if choice.lower() == "sword":
    draw_sword()
elif choice.lower() == "mask":
    draw_mask()
else:
    print("Sorry, I can only draw a sword or a mask.")
