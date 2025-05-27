# Chapter 10: Final Project
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

def run_assistant():
    print("Welcome to the Fencing Art Assistant!")
    print("You can draw a 'sword' or a 'mask'. Type 'exit' to quit.")
    drawn_items = []
    while True:
        choice = input("Draw what? ").strip().lower()
        if choice in ("exit", "quit", ""):
            break
        elif choice == "sword":
            draw_sword()
            drawn_items.append("sword")
        elif choice == "mask":
            draw_mask()
            drawn_items.append("mask")
        else:
            print("Sorry, I can only draw sword or mask.")
    if drawn_items:
        print("You drew:", ", ".join(drawn_items))
    else:
        print("Goodbye!")

run_assistant()
