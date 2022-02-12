import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QSize

class _Key(QPushButton):
	def __init__(self, widget, color, w):
		super().__init__(widget)
		self.setFixedSize(QSize(w, 24))
		self.color = color
		self.setStyleSheet("border-radius : 5; border : 1px solid black; background-color: %s; " % color)
  
	def change_color(self, color):
		print("change to color", color)
		self.color = color
		self.setStyleSheet("border-radius : 5; border : 1px solid black; background-color: %s; " % color)
  
xda1 = '#fafafa'
xda2 = '#fffcfc'
xda3 = '#faf5f5'
xda4 = '#fae8ea'
xda5 = '#ffffd6'
# xda6 = '#e6d1d3'
xda9 = '#c6e1f7'
xda_colors = [xda1, xda2, xda3, xda4, xda5, xda9]

# settings
key_size = 24
WS = [15, 15, 14, 14, 10] # key count for each row
sizes = [[key_size for _ in range(num_key_in_row)] for num_key_in_row in WS]
colors = [[xda3 for _ in range(num_key_in_row)] for num_key_in_row in WS]
 
sizes[0][-2] = key_size*2

sizes[1][0] = key_size*1.5
sizes[1][-2] = key_size*1.5

sizes[2][0] = key_size*1.75
sizes[2][-2] = key_size*2.25

sizes[3][0] = key_size*2.25
sizes[3][-3] = key_size*1.75

sizes[4][0] = key_size*1.25
sizes[4][1] = key_size*1.25
sizes[4][2] = key_size*1.25
sizes[4][3] = key_size*6.25

colors[0][0] = xda9

colors[0][-4] = xda2 # comma
colors[0][-3] = xda2 # comma

colors[0][-2] = xda9
colors[0][-1] = xda4

for i in range(1,11):
	colors[0][i] = xda4
	

colors[1][0] = xda4

colors[1][-4] = xda2 # comma
colors[1][-3] = xda2 # comma

colors[1][-2] = xda2 # \
colors[1][-1] = xda4



colors[2][0] = xda9

colors[2][4] = xda4
colors[2][7] = xda4

colors[2][-4] = xda2 # comma
colors[2][-3] = xda2 # comma

colors[2][-2] = xda4 # enter
colors[2][-1] = xda4


colors[3][0] = xda4

colors[3][-6] = xda2 # comma
colors[3][-5] = xda2 # comma
colors[3][-4] = xda2 # comma

colors[3][-3] = xda4
colors[3][-2] = xda9 # dir
colors[3][-1] = xda4


colors[4][0] = xda4
colors[4][1] = xda4
colors[4][2] = xda4
colors[4][3] = xda2 # space
colors[4][4] = xda4 
colors[4][5] = xda4
colors[4][6] = xda4

# dir
colors[4][7] = xda9
colors[4][8] = xda9
colors[4][9] = xda9
 
def window():
	app = QApplication(sys.argv)
	# widget basic setting
	widget = QWidget()
	widget.setWindowTitle("Keyboard Color Scheme")
	widget.setStyleSheet("background-color: black;")
	widget.setGeometry(50,50,500,180)

	space = 0
	for y, line in enumerate(sizes):
		tw = 50
		for x, width in enumerate(line):
			b = _Key(widget, colors[y][x], width)
			b.pressed.connect(keyboard_clicked(b))
			# b.setText(str(x)+','+str(y))
			b.move(tw, 25+y*(key_size+space))
			tw += width + space
   
	space = 2
	for i in range(len(xda_colors)):
		b = _Key(widget, xda_colors[i], key_size)
		b.pressed.connect(palette_clicked(xda_colors[i]))
		b.move(450,25+i*(key_size+space))

	widget.show()
	sys.exit(app.exec_())

def count_key():
	color_count = {'xda1':[],'xda2':[], 'xda3':[], 'xda4':[], 'xda9':[]}
 
	for y, rcs in enumerate(colors):
		for x, c in enumerate(rcs):
			if colors[y][x] == xda1: color_count['xda1'].append(sizes[y][x]/key_size)
			if colors[y][x] == xda2: color_count['xda2'].append(sizes[y][x]/key_size)
			if colors[y][x] == xda3: color_count['xda3'].append(sizes[y][x]/key_size)
			if colors[y][x] == xda4: color_count['xda4'].append(sizes[y][x]/key_size)
			if colors[y][x] == xda9: color_count['xda9'].append(sizes[y][x]/key_size)
   
	print(color_count)
	print()
	print('xda2:',sorted(color_count['xda2']))
	print('xda4:',sorted(color_count['xda4']))
	print('xda9:',sorted(color_count['xda9']))
	print()
	[print(k,":", len(i)) for k, i in color_count.items()]
 
def keyboard_clicked(b):
	def func():
		b.change_color(mouse_color)
		print("keyboard_clicked clicked")
	return func

def palette_clicked(xda_color):
	def func():
		global mouse_color
		mouse_color = xda_color
		print("mouse color: %s" % mouse_color)   
	return func
   
if __name__ == '__main__':
   window()