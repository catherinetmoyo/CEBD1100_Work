currency_details = {
    "USD": {
        "symbol": "$",
        "name": "US Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "USD",
        "name_plural": "US dollars"
    },
    "CAD": {
        "symbol": "CA$",
        "name": "Canadian Dollar",
        "symbol_native": "$",
        "decimal_digits": 2,
        "rounding": 0,
        "code": "CAD",
        "name_plural": "Canadian dollars"
    }
}

# get me the symbol for canadian dollar
# get me the code for US dollar
print("The symbol of canadian dollar is " + currency_details["CAD"]["symbol"])
print("The code of US dollar is " + currency_details["USD"]["code"])

