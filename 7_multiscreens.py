from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class LastScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

MultiScreen = Builder.load_string('''
ScreenManagement:
    
    MainScreen:
    AnotherScreen:
    LastScreen:
	
<MainScreen>:
    name: 'main'

    Button:
        on_release: app.root.current = 'other'
        text: 'This is the First Screen'
        font_size: 50
            
<AnotherScreen>:
    name: 'other'

    Button:
        on_release: app.root.current = 'last_screen'
        text: 'Second'
        font_size: 50   
        
<LastScreen>:
    name: 'last_screen'

    Button:
        on_release: app.root.current = 'main'
        text: 'Final screen! Here we go again!'
        font_size: 50  
''')

class MainApp(App):
    def build(self):
        return MultiScreen

if __name__ == "__main__":
    MainApp().run()