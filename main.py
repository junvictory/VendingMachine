
#Vending Machine Item
products = {'Cola':5,'Sprite':5,'Orange':5,'Pocari':5,'Milkis':5}
products_price = {'Cola': 1000,'Sprite':1000,'Orange':900,'Pocari':700,'Milkis':800}

items = list(products.keys())


def productSet(select, product):
    if(select == 0): # product 갯수 확인
        return products[product]

    elif(select == 1): # product  판매
        print(str(products_price[product]) +" 원 입니다")
        input("투입 금액 ?")


    elif(select == 2):
        opt = input("(0)추가, (1) 수정 (2)삭제")
        if(int(opt) == 0):
            num = input ("갯수 : ")
            products[product] = products[product] + int(num)
            print(int(products[product]))


def logic(select):
    if (0 < int(select) < len(items) + 1):
        print(items[int(select) - 1])
        productSet(1, items[int(select) - 1])


    elif (int(select) == 100):
        print("Administrator User")
        showProducts()
        select = input("수정할 제품 넘버: ")
        productSet(2, items[int(select) - 1])
    else:
        print("No Item")

def showProducts():
    i = 1
    for item in items:
        print(str(i) + ". " + item + "  |" + str(products_price[item]) + " won")
        i = i + 1

def Welcome():
    showProducts()


print("Welcome Vending Machine")
showProducts()
print("////////////////")
select = input("Select Product : ")
logic(select)



# print(data.keys())
#
