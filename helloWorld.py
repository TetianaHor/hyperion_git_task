def custom_print(string, decorator):
    '''Custom print function'''
    print(f"{decorator * 3} {string} {decorator * 3}")

decoration_list = {0: '*', 1: '\"', 2: '_', 3: '$'}
# Ask user to type some text
text = input("Type something: ")
# Ask user to choose a decoration symbol
print("You can select one of those options as a decoration symbol")
for index, symbol in decoration_list.items():
    print(f"{index} for {symbol}")
symbol_key = input("Choose a string decoration symbol: ")
# Print out a decorated string
if symbol_key.isdigit() and int(symbol_key) in decoration_list:
    custom_print(text, decoration_list[int(symbol_key)])
else:
    print("Wrong key")
