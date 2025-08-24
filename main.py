from datetime import datetime
from datetime import timedelta

from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.uix.pickers import MDDatePicker
from kivymd.toast import toast

kv ='''
MDFloatLayout:
	md_bg_color: [0.7725490196078432, 0.792156862745098, 0.9137254901960784, 1]
		
	MyLayout:
		pos_hint: {"center_x":.5,"center_y":.5}
		size_hint: .80,.30
		#elevation:1		
		radius: 9,9
		md_bg_color:0.7019607843137254, 0.5333333333333333, 1.0, 1
		
		MyLayout:
			pos_hint: {"center_x":.5,"center_y":.80}
			size_hint: .80,.10
			md_bg_color: 'white'
			radius: 2,2
			elevation:1
			
			TextInput:
				id: user_dob
				halign: 'center'
				disabled: True
				pos_hint: {"center_x":.5,"center_y":.5}
				multiline: False
				background_color: 0,0,0,0
				size_hint: .90,None
				height: self.minimum_height
				hint_text: "DOB(yy/mm/dd)"
				font_size: "20dp"
				cursor_width: '2sp'
				cursor_color: 0.5,0.5,0.5,0.5
				padding: 2
				
			MDIconButton:
				icon: 'calendar'
				on_release: app.show_date_picker()
				
				pos_hint: {"center_x":.95,"center_y":.5}
				theme_text_color: 'Custom'
				ripple_scale: 0
				text_color: app.theme_cls.primary_color
		
		MyLayout:
			pos_hint: {"center_x":.5,"center_y":.5}
			size_hint: .80,.10
			md_bg_color: 0,0,0.2,0.2
			radius: 3,3
			
			MDLabel:
				id: output
				text: 'Your age here!'
				bold: True
				halign: 'center'
				pos_hint: {"center_x":.5,"center_y":.5}
		
		MDRaisedButton:
			text: 'GET AGE'
			elevation: 0.1
			pos_hint: {"center_x":.5,"center_y":.30}
			on_release: app.get_age()
					
<MyLayout@MDFloatLayout+CommonElevationBehavior>
'''
class Eji(MDApp):		
	def build(self):
		self.theme_cls.primary_palette = "Teal"
		return Builder.load_string(kv)
	
	def on_save(self, instance, value, date_range):
		self.DOB = (value)
		self.root.ids.user_dob.text = str(value)
		
	def on_cancel(self):
		pass
	
	def show_date_picker(self):

		date_dialog = MDDatePicker(title = "SELECT DOB",title_input="INPUT DOB")

		date_dialog.bind(on_save=self.on_save)

		date_dialog.open()
		
	def get_dob(self):
		
		try:
			date = str(self.DOB)
			date = date.split('-')
			year = int(date[0])
			month = int(date[1])
			day = int(date[2])
			
			dob = datetime(year,month,day)
			
			return dob
		except AttributeError:
			toast('')#to avoid two toasts at once!
	
	def get_age(self):
		try:
			
			NOW = datetime.today()
			dob = self.get_dob()
			AGE = round(((NOW - dob).days)/365)
			
			self.root.ids.output.text=f'{AGE} Y/O'
		
		except TypeError:
			toast('Please provide DOB!')


if __name__ == '__main__':
	Eji().run()