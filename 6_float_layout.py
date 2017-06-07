from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


Builder.load_string('''
<Button1>:
    size_hint: 0.1, 0.1
    color: 0,1,0,1 # RGB + transparency
    
<Button2>:
    size_hint: 0.1, 0.1
    color: 1,1,1,1

<FloatLayout>:
    Button1:
        pos_hint: {"x": 0, 'y':0.45}
        text: "Wojciech"
    
    Button2:
        pos_hint: {"x": 0.1, 'y':0}
        text: "Orzechowski"
    
    Button1:
        pos_hint: {"x": 0.45, 'y':0}
        text: "Github.com/arcyfelix"
        
    Button1:
    
        # Middle of the screen
        #pos_hint: {"x": 0.45, "y": 0.45} 
        pos_hint: {"x": 0.5 - 0.5 * self.size_hint[0], "top": 0.5 + 0.5 * self.size_hint[1]} 
        text: "He loves Sara!"
        italic: True
        bold: True
        
''')

# All the graphical data for the widget comes from the string loader
class Button1(Button):
    pass

class Button2(Button):
    pass

class WojciechGithub(App):
    def build(self):
        return FloatLayout()
		

if __name__ == "__main__":
    WojciechGithub().run()