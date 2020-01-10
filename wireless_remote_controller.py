import ui
import console
import webbrowser

on_url = []
off_url =[]
on_url.append("http://") #TODO
off_url.append("http://") #TODO

on_url.append("http://") #TODO
off_url.append("http://") #TODO


width, height = ui.get_screen_size()

class ButtonView(ui.View):
	def __init__(self, frame):
		self.bg_color = 'white'
		self.btn_name =['DeskLight', 'GeneralLight', 'BothLight']
		button_style = {'background_color': '#ffff', 'tint_color': '#ffffff', 'font': ('<System>', 50), 'corner_radius': 30}
		self.button = [ui.Button(name=self.btn_name[i], title='オフ', action=self.button_tapped, **button_style) for i in range(3)]
		for b in self.button:
			self.add_subview(b)
		self.btn_status = [0, 0]
		self.display_view = ui.View(frame=self.bounds)
		self.add_subview(self.display_view)
		self.labels = [ui.Label(flex='wh', text=':', alignment=ui.ALIGN_CENTER, font = ('<System-bold>', 50)) for i in range(2)]
		for label in self.labels:
			self.add_subview(label)
	def layout(self):
		global width
		frame = ui.Rect(10, 250, width-20, 120)
		self.button[0].frame = frame.inset(1,1)
		self.button[0].background_color = (0, 0, 255)
		frame = ui.Rect(10, 450, width-20, 120)
		self.button[1].frame = frame.inset(1,1)
		self.button[1].background_color = (255, 0, 0)
		frame = ui.Rect(10, 50, width-20, 120)
		self.button[2].frame = frame.inset(1,1)
		self.button[2].background_color = '#7fffc8'
		self.button[2].tint_color = 'black'
		self.button[2].title = "退室・就寝"
		
		frame = ui.Rect(10, 170, width-20, 80)
		self.labels[0].frame = frame.inset(1,1)
		self.labels[0].text = 'デスクライト'
		frame = ui.Rect(10, 370, width-20, 80)
		self.labels[1].frame = frame.inset(1,1)
		self.labels[1].text = '照明'

	def button_tapped(self,sender):
		if sender.name in self.btn_name[0:1+1]:
			i = 0 if sender.name == self.btn_name[0] else 1
			if self.btn_status[i]  == 0:
				sender.title = "オン"
				webbrowser.open(off_url[i])
				self.btn_status[i] = 1
			elif self.btn_status[i]  == 1:
				sender.title = "オフ"
				webbrowser.open(on_url[i])
				self.btn_status[i] = 0
			console.hide_output()
		elif sender.name in self.btn_name[2]:
			button = [sender.superview[self.btn_name[j]] for j in range(2)]
			for j, b in enumerate(button):
				b.title="オン"
				webbrowser.open(off_url[j])
				self.btn_status[j] = 1
			console.hide_output()

w, h = ui.get_screen_size()
v = ButtonView(frame=(0,0, w, h))
v.present('')
