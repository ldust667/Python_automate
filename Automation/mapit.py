
import webbrowser, sys, pyperclip

#this script will open a web browser to google maps with the address entered as an arguement when called or the address stored on the clipboard

sys.argv # [mapit.py, '870', 'Valencia', 'St.']

# check if commandline arguments passed
if len(sys.argv) > 1:
	# joins all of them into value seperated by space
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://google.com/maps/place/' + address)
