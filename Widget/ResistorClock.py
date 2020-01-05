#!python3

from datetime import datetime
import time
import appex, ui
import console
import os

colorCode=['#2B2B2B', '#994C00','#ED1A3D', '#FF8C00', '#FFD900', '#008000', '#0067C0',
'#A757A8', '#808080', '#E8F4E6']

class ClockView (ui.View):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		#self.bounds = (0, 0, 400, 200)
		self.flag= False
		clock_style = {'background_color': colorCode[0], 'tint_color': colorCode[0],'font': ('<System>', 30), 'corner_radius': 20}
		button_style = {'background_color': '#87cefa', 'tint_color': '#191970', 'font': ('<System-bold>', 20), 'corner_radius': 10}
		self.clock_numbers = [ui.Button(title=str(i), **clock_style) for i in range(6)]
		for b in self.clock_numbers:
			self.add_subview(b)
		self.button = ui.Button(action=self.button_tapped, title='表示', **button_style)
		self.add_subview(self.button)
		
		self.colons = [ui.Label(flex='wh', text=':', alignment=ui.ALIGN_CENTER, font = ('<System>', 30)) for i in range(2)]
		for colon in self.colons:
			self.add_subview(colon)
		
		self.display_view = ui.View()
		self.add_subview(self.display_view)
	def button_tapped(self, sender):
		self.flag = not self.flag
		
	def layout(self):
		bw = self.width / 7
		bh = self.height * 2  / 3
		frame = ui.Rect(2*bw, 0, 0.5*bw, bh-5)
		self.colons[0].frame = frame.inset(1,1)
		frame = ui.Rect(4.5*bw, 0, 0.5*bw, bh-5)
		self.colons[1].frame = frame.inset(1,1)
		
		frame = ui.Rect(0, bh, self.width, self.height - bh)
		self.button.frame = frame.inset(4,4)
		
		for i, b in enumerate(self.clock_numbers):
			frame = ui.Rect((i +0.5*int(i/2)) * bw, 0, bw, bh)
			b.frame = frame.inset(3, 3)
		self.display_view.frame = (0, 0, self.width, bh)
	def reload(self):
		t = datetime.now()
		t_list = []
		t_list.append(int(t.hour / 10))
		t_list.append(t.hour % 10)
		t_list.append(int(t.minute / 10))
		t_list.append(t.minute % 10)
		t_list.append(int(t.second / 10))
		t_list.append(t.second % 10)
		if self.flag == True:
			self.button.title = '非表示'
		else:
			self.button.title = '表示'
		for i, b in enumerate(self.clock_numbers):
			b.background_color = colorCode[t_list[i]]
			if t_list[i] in [3, 4, 9]:
				b.tint_color = colorCode[0]
			else:
				b.tint_color = colorCode[9]
			if self.flag == True:
				b.title = str(t_list[i])
			else:
				b.title = ''

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	widget_view = appex.get_widget_view()
	if widget_view is None or widget_view.name != widget_name:
		widget_view = ClockView()
		widget_view.name = widget_name
		appex.set_widget_view(widget_view)
		while True:
			widget_view.reload()
			time.sleep(1)

if __name__ == '__main__':
	main()
