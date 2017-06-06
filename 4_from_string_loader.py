from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_string('''
<Widgets>:
    Button:
        size: 100, 100
        pos: 0, 0
        text: "Wojciech"
        color: 1, 1, 0, 1
        

    Button:
        size: 100, 100
        pos: 100, 0 # 0,0 is the left bottom corner!
        text: "Orzechowski"
        color: 1, 0, 0, 1 # RGB + transparency
        	

    Button:

        size: 200, 100
        pos: 200,0
        text: "Github.com/arcyfelix"
        color: 1, 0, 0, 1
        
        
    Button:

        size: 200, 100
        
        # Middle of the screen
        pos: (0.5 * (root.width - self.width)), (0.5 * (root.height - self.height)) 
        text: "He loves Sara!"
        color: 1, 1, 1, 1
        
        
        
''')

# All the graphical data for the widget comes from the string loader
class Widgets(Widget):
    pass
	

class WojciechGithub(App):
    def build(self):
        return Widgets()
		

if __name__ == "__main__":
    WojciechGithub().run()