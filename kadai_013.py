def calc_price(price, tax):
    total = price * (1 + tax/100)
    print(f"{total}円")    
calc_price(2000, 10)   