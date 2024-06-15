import curses

def draw_frame(stdscr, height, width):
    title = "DUNFINITY"

    for i in range(width):
    	stdscr.addstr(0, i, "-")
    	#stdscr.addstr(height - 2, i, "-")

    x = width // 2 - len(title) // 2
    stdscr.addstr(0, x, title)

def draw_prompt(stdscr, height, width):
	stdscr.addstr(height - 2, 0, "> ")

def main(stdscr):
	running = True

	while running:
		# clear screen
		stdscr.clear()

		# retrieve screen height and width
		height, width = stdscr.getmaxyx()

		draw_frame(stdscr, height, width)

		# stdscr.addstr(y, x, message)
		stdscr.addstr(2, 0, "welcome to dunfinity")
		stdscr.addstr(3, 0, "press q to quit")
		#stdscr.addstr(4, 0, ">>> ")

		draw_prompt(stdscr, height, width)

		# wait for user input
		stdscr.refresh()
		c = stdscr.getch()

		if c == ord('q'):
			running = False

if __name__=="__main__":
	# start the curses application
	curses.wrapper(main)
