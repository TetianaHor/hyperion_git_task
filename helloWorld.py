def custom_print(string, decorator):
    print(f"{decorator * 3} {string} {decorator * 3}")

text = input("Type something: ")
custom_print(text, '*')
