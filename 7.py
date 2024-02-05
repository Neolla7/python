"""Дано:кофейный автомат, который может готовить напитки на выбор:
- латте стоит 10$
- кофе стоит 7$
- какао стоит 8$
Клиент пополнил автомат на 5+2+1$
Программа: показывает сколько у клиента на счету и предлагает выбрать напиток из списка.
Если денег на счету недостаточно - вывести соответсвующее сообщение
Если достаточно - написать, что заказ принят и вывести сколько остаток на счету"""

cash_credit = input("please, enter a cash to automat: ")

if cash_credit.isdigit():
    cash_credit = int(cash_credit)
else:
    print("Wrong input")
    exit()

latte_price = 10 
cofee_price = 7
cacao_price = 8
drinks = ["latte", "coffee", "cacao"]

print("available drinks:")
print(f"latte: {latte_price}$ - press 1 \ncoffe: {cofee_price}$ - press 2 \ncacao: {cacao_price}$ - press 3")

print(f"your cash credit: {cash_credit}$") 

choice_drinks = int(input("please, choose a drink: "))

if choice_drinks == 1:
    if cash_credit >= latte_price:
        cash_credit -= latte_price
    else:
        print ("you dont have enough money, looser)")
    
elif choice_drinks == 2:
    if cash_credit >= cofee_price:
        cash_credit -= cofee_price 
    else:
        print ("you dont have enough money, looser)")

elif choice_drinks == 3:
    if cash_credit >= cacao_price:
        cash_credit -= cacao_price
    else:
        print ("you dont have enough money, looser)")

else:
    print("Wrong choice")
    exit()

print(f"your {drinks[choice_drinks - 1]} is prepared")
print(f"Please, take your rest {cash_credit}$")