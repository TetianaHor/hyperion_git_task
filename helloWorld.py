def custom_print(string, decorator):
    '''Custom print function'''
    print(f"{decorator * 3} {string} {decorator * 3}")

# Ask user to type some text and a symbol
text = input("Type something: ")
symbol = input("Choose a string decoration symbol: ")
# Print out a decorated string
custom_print(text, symbol)
