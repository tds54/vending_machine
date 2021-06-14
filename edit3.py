import sqlite3

dbname = 'item_menu.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

item_price = cur.execute('select name, price from item_menus')
item_price = dict(item_price)

item_count = cur.execute('select name, count from item_menus')
item_count = dict(item_count)

class Edit:
    def edit(self):
        print('---------------------')
        print("1 飲み物個数追加")
        print("2 飲み物種類追加")
        print("3 飲み物種類削除")
        print("4 設定終了")

    def addquantity(self):
        aa = input("追加する商品の名前を入力してください：")

        if aa in item_price:
            bb = input("追加する商品の個数を入力してください：")
            cc = int(bb) + item_count[aa]

            conn.execute('update item_menus set count = (?) where name = (?)', [cc, aa])

            conn.commit()

        else:
            print("該当の商品がありません。")

    def addmenu(self):
        oo = input("追加する商品の名前を入力してください：")
        pp = int(input("追加する商品の値段を入力してください："))
        qq = int(input("追加する商品の個数を入力してください："))
        conn.execute('INSERT INTO item_menus(name,price,count) values(?,?,?)', [oo, pp, qq])

        conn.commit()
        print('---------------------')

        add_menu = cur.execute('select * from item_menus where name = (?)', [oo])
        add_menu = list(add_menu)

        for i in add_menu:
            print(i[0], "金額：" + str(i[1]), "在庫：" + str(i[2]) + "をメニューに追加しました。")

    def deletemenu(self):
        conn.execute('delete from item_menus where name = (?)', [input("削除する商品の名前を入力してください：")])

        conn.commit()

    def endmenu(self):
        print("設定を終了します。")
