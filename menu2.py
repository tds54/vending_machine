import sqlite3

dbname = 'item_menu.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

item_price = cur.execute('select name, price from item_menus')
item_price = dict(item_price)

item_count = cur.execute('select name, count from item_menus')
item_count = dict(item_count)


class Order:
    def cash(self):
        print('--------------------')
        order = input("メニューを入力してください:")

        if order in item_price:
            price = item_price[order]

            if item_count[order] == 0:
                print("在庫がありません。入力をやり直してください")

            else:
                print("値段は" + str(price) + "円です。")
                piece = int(input("購入する個数を入力してください："))
                print('--------------------')

                if item_count[order] < piece:
                    print("在庫が足りません。入力をやり直してください")

                else:
                    diff1 = int(item_count[order]) - int(piece)
                    conn.execute('update item_menus set count = (?) where name = (?)', [diff1, order])

                    conn.commit()

                    total_price = price * piece
                    print("値段は" + str(total_price) + "円です。")

                    money = int(input('投入金額を入力してください:'))
                    change = money - int(total_price)

                    while True:
                        if total_price > money:
                            print('投入金額が不足しています。')
                            print(str(-change) + '円足りません。')
                            money = money + int(input('投入金額を追加入力してください:'))
                            change = money - int(total_price)

                            if total_price > money:
                                print('投入金額が不足しています。')
                                print(str(-change) + '円足りません。')
                                money = money + int(input('投入金額を追加入力してください:'))
                                change = money - int(total_price)

                        else:
                            print(order + "を" + str(piece) + "個購入しました。")
                            print("お釣りは￥" + str(change) + "です。")
                            break

        else:
            print("該当の商品がありません。")
