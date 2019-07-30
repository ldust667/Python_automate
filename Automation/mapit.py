
import webbrowser, sys, pyperclip

#this script will open a web browser to google maps with the address entered as an arguement when called or the address stored on the clipboard

sys.argv # [mapit.py, '870', 'Valencia', 'St.']

# check if commandline arguments passed
if len(sys.argv) > 1:
	# joins the words with spaces into variable
	address=' '.join(sys.argv[1:])
else:
	#If argument is not entered python uses the PC clipboard
	address=pyperclip.paste

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://google.com/maps/place/' + address)
