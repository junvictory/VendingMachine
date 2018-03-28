import time


#Vending Machine Item
products = {'Cola':0,'Sprite':5,'Orange':5,'Pocari':5,'Milkis':5}
products_price = {'Cola': 1000,'Sprite':1000,'Orange':900,'Pocari':700,'Milkis':800}

items = list(products.keys())


def productSet(pu_select, item):
    if(pu_select == 0): # product 갯수 확인
        if (availability(item) == "O"):
            print(str(products_price[item]) + " 원 입니다")
            input("투입 금액 ?")
        else:
            print("판매불가 다시 선택해 주세요")
            welcome()

    elif(pu_select == 1): # product  판매
        if (availability(item) == "O"):
            print("판매되었습니다.")
            welcome()





    # elif(select == 2):
    #     opt = input("(0)추가, (1) 수정 (2)삭제")
    #     if(int(opt) == 0):
    #         num = input ("갯수 : ")
    #         products[item] = products[item] + int(num)
    #         print(int(products[item]))


def logic(pu_select,pro_select):
    if (0 < int(pro_select) < len(items) + 1):
        print(items[int(pro_select) - 1])
        productSet(pu_select, items[int(pro_select) - 1])
    else:
        print("No Item")

def showProducts():
    i = 1
    for item in items:
        print(str(i) + ". " + item + "  |" + str(products_price[item]) + " won 판매 여부: "+ availability(item))
        i = i + 1

#판매가능 여부
def availability(item):
    if(products[item] >0):
        return "O"
    else:
        return "X"


def calculator(pu_select):





def main():
    select = input("현금(0) 카드(1) 선택해 주세요:")
    if(int(select) == 0):
        print("현금 결제")
        welcome(0)

    else:
        print("카드를 인식시켜 주세요")
        time.sleep(2)
        print("인식 되었습니다")
        welcome(1)






# 0일 경우 현금 1일 경우 카드 구매
def welcome(pu_select):
    print("Welcome Vending Machine")
    showProducts()
    print("////////////////")
    pro_select = input("Select Product : ")
    logic(pu_select,pro_select)




main()
# print(data.keys())
#
