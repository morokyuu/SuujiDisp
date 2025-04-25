def render_tiles(count):
    tens = count // 10
    ones = count % 10

    print(f"\n現在の数: {count}")
    print("10のタイル（）:", "" * tens)
    print("1のタイル（）:", "" * ones)


def main():
    count = 0
    while True:
        render_tiles(count)
        cmd = input("\n+で増やす, -で減らす, qで終了 > ")

        if cmd == '+':
            count += 1
        elif cmd == '-':
            if count > 0:
                count -= 1
            else:
                print("0未満にはできません")
        elif cmd == 'q':
            print("終了します。")
            break
        else:
            print("無効な入力です。+ か - か q を入力してください。")


if __name__ == "__main__":
    main()
