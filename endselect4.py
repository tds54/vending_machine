import os
import sys

class Select:
    def select(self):
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
