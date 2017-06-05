from kivy.app import App


#kivy.require("1.8.0")


'''
Importing a label.
It can be used as a label or a button.
'''
from kivy.uix.label import Label

'''
Inheriting from the App class
'''
class SimpleKivy(App):
    def build(self):
        return Label(text = "Hello World!")
        
        
if __name__ == "__main__":
    SimpleKivy().run()
    