import curses
from sys import exit
from functools import partial


# handle selection in display menu
def display_menu(stdscr, attr, start_display_idx, selected_row_idx):
    stdscr.erase()

    options = attr["options"]
    stdscr.addstr(0, 0, attr["message"])

    if isinstance(options, dict):
        display_options = list(options.keys())[start_display_idx:start_display_idx + curses.LINES - 1]

    else:
        display_options = options[start_display_idx:start_display_idx + curses.LINES - 1]

    for idx, option in enumerate(display_options):
        x = 0
        y = 1 + idx
        info = ''

        # extra check for tree
        if isinstance(option, tuple):
            info = f"{option[0]:<11}"
            option = option[1]

        if start_display_idx + idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, f">> {info}{option}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, f"   {info}{option}")

    stdscr.refresh()


# handle selection in display menu
def menu_input(stdscr, attr):
    options = attr["options"]
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    selected_row_idx = 0
    start_display_idx = 0

    display_menu(stdscr, attr, start_display_idx, selected_row_idx)

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            print("Process ending received exit action (q)")
            exit()

        elif key == curses.KEY_UP:
            if selected_row_idx > 0:
                selected_row_idx -= 1
                if selected_row_idx < start_display_idx:
                    start_display_idx -= 1

        elif key == curses.KEY_DOWN:
            if selected_row_idx < len(options) - 1:
                selected_row_idx += 1
                if selected_row_idx >= start_display_idx + curses.LINES - 1:
                    start_display_idx += 1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if isinstance(options, dict):
                option = list(options.keys())[selected_row_idx]
                return option, options[option]
            else:
                return selected_row_idx, options[selected_row_idx]

        display_menu(stdscr, attr, start_display_idx, selected_row_idx)


# root menu function
def menu(attr):
    return curses.wrapper(partial(menu_input, attr=attr))
