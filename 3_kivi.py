from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget

#from kivy.lang import Builder
#Builder.load_file('simple_kv_script3.kv')

# All the graphical data for the widget is stored in file 3_kivi.kv
class Widgets(Widget):
    pass
	

class simple_kv_script3(App):
    def build(self):
        return Widgets()
		

if __name__ == "__main__":
    simple_kv_script3().run()