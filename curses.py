import curses
import curses.textpad as textpad
from curses import wrapper
    screen.clear()

    screen.refresh()

    win = curses.newwin(1, height -1, width, 0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)


    banner = '~-> cryptolizard textchannel <-~'
    screen.addstr(0, int(width / 2 - 16), banner, curses.color_pair(3))
    screen.addstr(0, width - 16, 'connected=true', curses.color_pair(4))



    screen.addstr(index, 0, "[friend] << hello, whats up?", curses.color_pair(2))


    while (True):
        field = textpad.Textbox(win)
        field.edit(exit_on_enter)
        text = field.gather().replace('$ ', '', 1)
        screen.addstr(index, 0, "[friend] >> " + text, curses.color_pair(1))
        win.clear()
        win.addstr(0, 1, "$ ", curses.color_pair(3))
        index += 1
        add_test_message(screen, index)
        index += 1

        screen.refresh()
