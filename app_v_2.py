#Version.Final
import time

#Vending Machine Item
products = {'Cola':0,'Sprite':5,'Orange':5,'Pocari':5,'Milkis':5}
products_price = {'Cola': 1000,'Sprite':1000,'Orange':900,'Pocari':700,'Milkis':800}
items = list(products.keys())

product_price_min = min(products_price.values())

#machine cash
cash = {'ca1000':0,'ca500':10,'ca100':10}

cash_price = (cash['ca1000']*1000) +(cash['ca500']*500)+(cash['ca100']*100)

#machine card
card_price = 0

#machine all price
all_price =cash_price+card_price

#machine Money
money = {'cash': cash_price, 'card': card_price, 'temp_cash': 0}

block = "                           \n"

def showProducts():
    items = list(products.keys())
    i = 1
    for item in items:
        print(str(i) + ". " + item + "  |" + str(products_price[item]) + " won 판매 여부: "+ availability(item))
        i = i + 1

def admin():
    print(block * 10)
    print("[----------관리자----------]")
    adminView()
    adminMenu()

def adminView():
    cash_price = (cash['ca1000'] * 1000) + (cash['ca500'] * 500) + (cash['ca100'] * 100)

    ad_products_view()
    print("[------현재 매출 현황------]")
    print("총 금액: " +str(cash_price+money['card'])+ " won")
    print("현금: "+str(cash_price) + " won")
    print("카드: "+str(money['card']) + " won")
    ad_cash_view()

def ad_products_view():
    items = list(products.keys())
    i = 1
    for item in items:
        print(str(i) + ". " + item + "  |" + str(products_price[item]) + " won  갯수: " + str(products[item]))
        i = i + 1

def ad_cash_view():
    print("[--------현금 현황---------]")
    print("1000원: " + str(cash['ca1000']))
    print("500원: " + str(cash['ca500']))
    print("100원: " + str(cash['ca100']))

def adminMenu():
    select = int(input("(1) Cash (2)Products (3)Exit (숫자만 입력바랍니다.)"))
    if(select == 1):
        print('[---현금 보충---]')
        mo_select = input("(1)500원 (2)100원 (3)Exit (숫자만 입력바랍니다.)")
        if(int(mo_select) == 1):
            cash['ca500'] += int(input("500원 갯수:"))
            ad_cash_view()
            print(block*2)
        elif(int(mo_select) == 2):
            cash['ca100'] += int(input("100원 갯수:"))
            ad_cash_view()
            print(block * 2)
        elif (int(mo_select) == 3):
            ad_cash_view()
        adminMenu()

    elif(select == 2):
        print('[-----제품-----]')
        pro_select = input("(1) 제품추가 (2)제품수정 (3)제품삭제" )
        if(int(pro_select) == 1):
            new_products_name = input("[1]제품 이름을 입력하시오: ")
            new_products_price = int(input("[2]제품 가격을 입력하시오: "))
            new_products_quantity = int(input("[3]제품 수량을 입력하시오: "))
            products[new_products_name] = new_products_quantity
            products_price[new_products_name] = new_products_price
            print("Save 저장 되었습니다")
            print(block*2)
            ad_products_view()
        elif(int(pro_select) == 2):
            ad_products_view()
            edit_pro = input("추가할 제품 선택: ")
            products[product_select(edit_pro)] += int(input(product_select(edit_pro)+" 갯수를 입력: "))
            ad_products_view()
        elif(int(pro_select) ==3):
            ad_products_view()
            edit_pro = input("삭제할 제품 선택: ")
            del products[product_select(edit_pro)]
            ad_products_view()
        adminMenu()
    elif(select == 3):
        print(block*10)
        payment_select()

#판매가능 여부
def availability(item):
    if(products[item] >0):
        return "O"
    else:
        return "X"

#select받은 item이 무엇인지
def product_select(pro_select):
    items = list(products.keys())
    if (0 < int(pro_select) < len(items) + 1):
        return items[int(pro_select) - 1]
    elif(int(pro_select) == 100):
        print("[-----반환-----]")
        cash_calculator(money['temp_cash'])
        payment_select()

    else:
        print("[-----제품이 없습니다----]")
        print("[-----반환-----]")
        cash_calculator(money['temp_cash'])
        payment_select()

#초기화
def pay_default():
    money['temp_cash'] = 0

# 0일때는 처음 1 일때는 중간
def pay_cash(select):
    if(int(select) == 0):
        print("현금을 넣어 주세요 (9900원 이하 까지 가능)")
        in_ca_1000 = int(input("1000 원 몇개: "))
        in_ca_500 = int(input("500 원 몇개: "))
        in_ca_100 = int(input("100 원 몇개: "))
        if ((in_ca_1000 * 1000) + (in_ca_500 * 500) + (in_ca_100 * 100) > 9900):
            print("[-----반환-----] 최대금액 초과")
            payment_select()
        else:
            cash['ca1000'] += in_ca_1000
            cash['ca500'] +=  in_ca_500
            cash['ca100'] +=  in_ca_100
            money['temp_cash'] += (in_ca_1000 * 1000) + (in_ca_500 * 500) + (in_ca_100 * 100)

            if(product_price_min <= money['temp_cash']):
                print("------ 현재 투입 금액 : " + str(money['temp_cash']) + "------")
                showProducts()
                print("[100 번 입력시 반환]")
                cash_logic(money['temp_cash'], product_select(int(input("[-----선택-----]제품을 선택 해주세요: "))))

            elif(product_price_min > money['temp_cash']):
                print("[-----반환-----] 최소금액 미만 ")
                cash_calculator(money['temp_cash'])

    elif(int(select) == 1):
        if (product_price_min <= money['temp_cash']):
            print("------ 현재 투입 금액 : " + str(money['temp_cash']) + "------")
            showProducts()
            print("[100 번 입력시 반환]")
            cash_logic(money['temp_cash'], product_select(int(input("[-----선택-----]제품을 선택 해주세요: "))))

        elif (product_price_min > money['temp_cash']):
            print("[-----반환-----] 최소금액 미만 ")
            cash_calculator(money['temp_cash'])
            payment_select()

def cash_logic(in_money,item):
    product_price_min = min(products_price.values())
    if(in_money >= products_price[item]):
        if(availability(item) == "X"):
            print("[-----제품이 품절입니다----]")
            cash_logic(in_money, product_select(int(input("[-----선택-----]제품을 선택 해주세요: "))))
        else:
            products[item] = products[item] - 1
            money['temp_cash']  = in_money - products_price[item]
            if(money['temp_cash'] >= product_price_min):
                pay_cash(1)
            else:
                cash_calculator(money['temp_cash'])
                payment_select()

    elif(in_money < products_price[item]):
        print("[--------잔액 부족---------]")
        pay_cash(0)

    else:
        cash_calculator(money['temp_cash'])
        payment_select()

def cash_calculator(out_money):
    re = (cash['ca500']*500)+ (cash['ca100']*100)
    res_cas = (out_money//500)-cash['ca500']

    if(res_cas>=0):
        res500 = cash['ca500']
        res100 = ((out_money-(res500*500)))//100

    elif(res_cas <0):
        res500 = out_money//500
        res100 = (out_money-(res500*500))//100

    cash['ca500'] = cash['ca500'] -res500
    cash['ca100'] = cash['ca100'] -res100

    print("[반환 금액]500원: "+str(res500)+" | 100원: "+str(res100))

def pay_card():
    print("카드를 인식시켜 주세요(time.sleep(2))")
    time.sleep(2)
    print("[---------인식완료----------]")
    showProducts()
    card_logic(product_select(int(input("[-----선택-----]제품을 선택 해주세요: "))))

def card_logic(item):
    if (availability(item) == "X"):
        print("[-----제품이 품절입니다----]")
        card_logic(product_select(int(input("[-----선택-----]제품을 선택 해주세요: "))))
    else:
        products[item] = products[item] - 1
        card_calculator(products_price[item])

def card_calculator(set_money):
    money['card'] += int(set_money)
    print('[카드 결제]결제 완료!')
    payment_select()

# 결제 선택
def payment_select():
    pay_default()
    print(block*10)
    print("------Welecom Vending Machine------")
    showProducts()
    print("[-----결제-----]결제 방법을 선택해 주세요   " + str(product_price_min))
    pay_select= input("(0)현금 (1)카드")
    if(int(pay_select) == 0):
        pay_cash(0)
    elif(int(pay_select) == 1):
        pay_card()
    elif(int(pay_select)==1004):
        admin()

payment_select()


