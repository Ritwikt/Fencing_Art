# Chapter 5: Lists for ASCII Art
def draw_mask():
    mask_art = [
        " ______",
        "| .  . |",
        "| ---- |",
        "|______|"
    ]
    for line in mask_art:
        print(line)

draw_mask()
