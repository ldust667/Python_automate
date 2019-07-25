import webbrowser, sys, pyperclip

sys.argv # [mapit.py, '870', 'Valencia', 'St.']

# check if commandline arguments passed
if len(sys.argv) > 1:
	# joins all of them into value seperated by space
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://google.com/maps/place/' + address)
