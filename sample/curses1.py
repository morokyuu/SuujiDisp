import curses

def main(stdscr):
    curses.curs_set(0)  # カーソル非表示
    stdscr.clear()

    total = 0
    input_str = ''

    while True:
        stdscr.clear()

        height, width = stdscr.getmaxyx()

        # 左側：現在値
        left_text = f"現在値: {total}"
        stdscr.addstr(2, 2, left_text)

        # 右側：入力中の値
        right_text = f"入力値: {input_str}"
        stdscr.addstr(2, width - len(right_text) - 10, right_text)

        stdscr.refresh()

        key = stdscr.getch()

        # 数字キー入力
        if ord('0') <= key <= ord('9'):
            input_str += chr(key)

        # バックスペース対応（Windows/Linuxで異なる）
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            input_str = input_str[:-1]

        # Enterキーで確定
        elif key in (curses.KEY_ENTER, 10, 13):
            if input_str.strip():
                try:
                    value = int(input_str)
                    total += value
                except ValueError:
                    pass  # 数値以外は無視
            input_str = ''

        # q で終了
        elif key == ord('q'):
            break

curses.wrapper(main)
