ver = int(input("任意の整数を入力してください>> "))
if ver < 0:
    print("正の数字を入力してください")
else:
    if (ver % 5 == 0 and ver % 3 == 0):
        print("FizzBuzz")
    elif (ver % 3 == 0):
        print("Fizz")
    elif (ver % 5 == 0):
        print("Buzz")
    else:
        print(ver)