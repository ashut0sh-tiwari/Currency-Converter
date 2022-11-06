'''CURRENCY CONVERTER'''

#opening and reading the file data
with open('currency exchange.txt') as f:
    data = f.readlines()

#creating a empty dictionary and adding data by using loop with split function on file data  
currencyDict = {}
for d in data:
    parsed = d.split("-")
    currencyDict[parsed[0]] = parsed[1]
#main function
print("Welcome to Currency Converter")
amount = int(input("Enter your amount:\n"))
print("Select the currency you want to convert this amount into")
# usinglist comprehension for printing data
[print(item) for item in currencyDict.keys()] 
currencyExchange = input("Enter the currency \n")
#using float to convert string into decimal integers
print(f"{amount} INR is equal to {amount * float(currencyDict[currencyExchange])} {currencyExchange}")
