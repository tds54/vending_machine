import sys
import sqlite3
from menu2 import Order
from edit3 import Edit
from endselect4 import Select

auto1 = Order()
auto2 = Edit()
auto3 = Select()

dbname = 'item_menu.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()


while True:
    item_menu = cur.execute('select * from item_menus')
    item_menu = list(item_menu)

    for i in item_menu:
        print(i[0], "金額：" + str(i[1]), "在庫：" + str(i[2]))

    try:
        print('--------------------')
        print("1:飲み物購入　2：自動販売機編集　3：終了")
        reaction = int(input("番号を選択してください："))

        if reaction == 1:
            auto1.cash()

        elif reaction == 2:
            auto2.edit()
            select = int(input("選択してください: "))
            if select == 1:
                auto2.addquantity()
            if select == 2:
                auto2.addmenu()
            if select == 3:
                auto2.deletemenu()
            if select == 4:
                auto2.endmenu()

        elif reaction == 3:
            print("購入を終了します。")
            sys.exit()

    except ValueError:
        print("入力された数値を適用することができません。")

    auto3.select()
