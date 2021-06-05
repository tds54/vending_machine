import os
import sys
import sqlite3

dbname = 'item_menu.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

while True:
    item_menu = cur.execute('select * from item_menus')
    item_menu = list(item_menu)

    item_dict = cur.execute('select name, price from item_menus')
    item_dict = dict(item_dict)

    item_count = cur.execute('select name, count from item_menus')
    item_count = dict(item_count)

    for i in item_menu:
        print(i[0], "金額：" + str(i[1]), "在庫：" + str(i[2]))

    try:
        print('--------------------')
        print("1:飲み物購入　2：自動販売機編集　3：終了")
        reaction = int(input("番号を選択してください："))

        if reaction == 1:
            print('--------------------')
            order = input("メニューを入力してください:")

            if order in item_dict:
                price = item_dict[order]
                print("値段は" + str(price) + "円です。")

                while True:
                    piece = int(input("購入する個数を入力してください："))
                    print('--------------------')

                    if item_count[order] < piece:
                        print("在庫が足りません。入力をやり直してください")

                    else:
                        conn.execute('update item_menus set count = count - (?) where name = (?)', [piece, order])

                        conn.commit()

                        total_price = price * piece
                        print("値段は" + str(total_price) + "円です。")

                        money = int(input('投入金額を入力してください:'))
                        change = money - int(total_price)
                        break

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

        if reaction == 2:
            while True:
                print('---------------------')
                print("1 飲み物個数追加")
                print("2 飲み物種類追加")
                print("3 飲み物種類削除")
                print("4 設定終了")

                try:
                    select = int(input("選択してください: "))
                    if select == 1:

                        aa = input("追加する商品の名前を入力してください：")

                        if aa in item_dict:
                            bb = int(input("追加する商品の個数を入力してください："))

                            conn.execute('update item_menus set count = count + (?) where name = (?)', [bb, aa])

                            conn.commit()
                            break

                        else:
                            print("該当の商品がありません。")

                    elif select == 2:
                        conn.execute('INSERT INTO item_menus(name,price,count) values(?,?,?)',
                                     [input("追加する商品の名前を入力してください："),
                                      int(input("追加する商品の値段を入力してください：")),
                                      int(input("追加する商品の個数を入力してください："))])

                        conn.commit()
                        print('---------------------')

                        item_menu = cur.execute('select * from item_menus')
                        item_menu = list(item_menu)

                        for i in item_menu:
                            print(i[0], "金額：" + str(i[1]), "在庫：" + str(i[2]))

                    elif select == 3:
                        conn.execute('delete from item_menus where name = (?)', [input("削除する商品の名前を入力してください：")])

                        conn.commit()

                    elif select == 4:
                        print("設定を終了します。")
                        break

                    else:
                        print('---------------------')
                        print("入力が間違えています。最初からやり直してください。")

                except ValueError:
                    print('---------------------')
                    print("入力が間違えています。最初からやり直してください。")

        if reaction == 3:
            print("購入を終了します。")
            sys.exit()

    except ValueError:
        print("入力された数値を適用することができません。")

    while True:
        try:
            print("初期画面に戻りますか？")
            print("1:はい  2:いいえ")
            reaction1 = int(input())

            if reaction1 == 1:
                os.system('cls')
                break

            elif reaction1 == 2:
                print("購入を終了します。")
                sys.exit()

            else:
                print("入力が間違っています。")
                print("入力をやり直してください。")

        except ValueError:
            print("入力が間違っています。")
            print("入力をやり直してください。")
