from kivy.app import App


#kivy.require("1.8.0")



# Importing a label.
# It can be used as a label or a button.
from kivy.uix.label import Label

# Importing a grid layout.
from kivy.uix.gridlayout import GridLayout

#Import text input module.
from kivy.uix.textinput import TextInput

# New class LoginScreen needs to inheret from GridLayout 
class LoginScreen(GridLayout): 
    def __init__(self, **kwargs):
        # Allowing multiinheritance
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1 # Columns
        
        # Adding a label / text
        self.add_widget(Label(text = "Username:"))
        # Adding a text input
        self.username = TextInput(multiline = False)
        # Using the text input
        self.add_widget(self.username)
        
        self.add_widget(Label(text = "Password:"))
        # Parameter password = True
        # will make the text being covered as *'s
        self.password = TextInput(multiline = False, password = True)
        self.add_widget(self.password)
'''
Inheriting from the App class
'''
class SimpleKivy(App):
    def build(self):
        return LoginScreen()
        
           
        
if __name__ == "__main__":
    SimpleKivy().run()
    