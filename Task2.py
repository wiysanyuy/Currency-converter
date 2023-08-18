#stage1
amount = float(input("Enter the amount: "))
curency_code = input("Enter the curency code: ")
#stage2 
def convertion_curency(amount, curency_code):
    convertion_rate = {"GBP":1.64, "AED":4.234, "USD":620,"ZWD":3.46,"CHF":4.644}
    if curency_code not in convertion_rate:
        return "Error: invalid curency code"
    converted_amount = amount * convertion_rate[curency_code]
    return converted_amount
#stage3.
converted_amount = convertion_curency(amount, curency_code)
#print("converted amount is:",converted_amount)
curency_symbol ={"GBP":'£', "AED":'₽', "USD":'$', "ZWD":'₣', "CHF":'₻'}
if curency_code not in curency_symbol:
    print("please input the correct curency code")
else:
    curency_symbol = curency_symbol.get(curency_code, curency_code)
    print("the oreginal amount was:", amount, curency_symbol)
    print("the converted amount is:", converted_amount, curency_symbol)
#curency_symbol = curency_symbol.get(curency_code, curency_code)
#print("the converted amount is:", converted_amount, curency_symbol)


    
        