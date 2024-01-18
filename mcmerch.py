import sys

def parseArgument():
    arguments = {
        "price": int(sys.argv[1])
        "quantity": 1
        "province": "ON"
    }

    return arguments

def taxRate(province):
    tax = {
        "ON": 0.13
    }
    return tax

def mcmerchCalculator():
    arguments = parseArgument()
    tax = taxRate(province)
    print(arguments['price'] * arguments["quantity"] * (tax+1)

mcmerchCalculator()