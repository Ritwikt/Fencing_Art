# Chapter 9: Debug and Style
# Added error handling and style improvements
try:
    draw_sword()
except NameError:
    print("Oops! draw_sword not defined. Did you forget to define it?")
