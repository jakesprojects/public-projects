import random
import time

window_size = '40x40'
whitespace_level = 10
fps = 8
char_sets = ['ktk']

def newpage():
    print "[2J[;H"

char_dict = {'jpn':range(12353,12439)+range(0x30a0, 0x3100)+range(0x4e00, 0x4f00),
'ktk':range(0x30a0, 0x3100),
'standard':range(32,128),
'all':range(0x10000),
'prof':['TEST','DOES IT WORK?']}

chars = []
for char_set in char_sets:
	for char in char_dict[char_set]:
		if type(char) == int:
			chars.append(unichr(char))
		else:
			chars.append(char)


window = window_size.split('x')

window_w = int(window[0])
window_l = int(window[1])
rows = []
while True:
	newpage()
	row = ''
	for num in range(window_w):
		row += ' '*random.randint(0,whitespace_level) + random.sample(population=chars,k=1)[0] + ' '*random.randint(0,whitespace_level)
	row = row[:window_w]
	rows.insert(0,row)
	for row in rows:
		print row
	if len(rows) >= window_l:
		del rows[len(rows)-1]
	time.sleep(1/float(fps))
