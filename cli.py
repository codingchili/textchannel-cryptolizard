import curses
import curses.textpad as textpad
from curses import wrapper

def main(screen):
    height, width = screen.getmaxyx()
    index = 1
	
    screen.clear()

    win = curses.newwin(1, width, height-1, 0)
    header = curses.newwin(1, width, 0, 0)
    content = curses.newwin(height -2, width, 1, 0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    banner = '~-> cryptolizard textchannel <-~'
    header.addstr(0, int(width / 2 - 16), banner, curses.color_pair(3))
    header.addstr(0, width - 16, 'connected=true', curses.color_pair(4))
    header.refresh()

    win.addstr(0, 1, "$ ", curses.color_pair(3))
    win.refresh()
    field = textpad.Textbox(win)

    while (True):	
        field.edit(exit_on_enter)
        text = field.gather().replace('$ ', '', 1)
        content.addstr(index, 0, "[friend] >> " + text, curses.color_pair(1))
        content.refresh()
        
        win.clear()
        win.addstr(0, 1, "$ ", curses.color_pair(3))
        win.refresh()
        index += 1
        #add_test_message(content, index)
        #screen.getch()
        #_help(content)

def _help(content):
    content.clear()
    index = 1
    content.addstr(index, 0, "commands!", curses.color_pair(3))
    index += 1
    content.addstr(index, 0, "commands!", curses.color_pair(3))
    index += 1
    content.addstr(index, 0, "commands!", curses.color_pair(3))
    index += 1
    content.addstr(index, 0, "commands!", curses.color_pair(3))
    index += 1
    content.addstr(index, 0, "commands!", curses.color_pair(3))
    content.refresh()

def exit_on_enter(key):
	if key == 10 or key == 13:
		key = 7
	return key

def add_test_message(content, index):
    content.addstr(index, 0, "[friend] << hey hey.", curses.color_pair(2))
    content.refresh()
        


wrapper(main)

