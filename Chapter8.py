# Chapter 8: Full Looping Assistant
def draw_sword(length=5):
    print("O" + "=" * length + ">")

def draw_mask():
    mask_art = [
        " ______",
        "| .  . |",
        "| ---- |",
        "|______|"
    ]
    for line in mask_art:
        print(line)

print("Welcome to the Fencing Art Assistant!")
drawn_items = []

while True:
    choice = input("Draw what? (sword/mask or exit): ").strip().lower()
    if choice in ("exit", "quit", ""):
        break
    elif choice == "sword":
        draw_sword()
        drawn_items.append("sword")
    elif choice == "mask":
        draw_mask()
        drawn_items.append("mask")
    else:
        print("I can only draw sword or mask.")

print("You drew:", ", ".join(drawn_items) if drawn_items else "nothing")
