import curses

def main(stdscr):
	# clear screen
	stdscr.clear()

	# retrieve screen height and width
	height, width = stdscr.getmaxyx()

	# display a message
	message = "hello, curses!"
	x = width // 2 - len(message) // 2
	y = height // 2
	stdscr.addstr(y, x, message)

	# wait for user input
	stdscr.refresh()
	stdscr.getch()

if __name__=="__main__":
	# start the curses application
	curses.wrapper(main)
