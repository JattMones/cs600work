from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols =  3
        self.add_widget(Button(text=''))
        self.add_widget(Button(text='Option 1'))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text='Option 2'))
        self.add_widget(Button(text='', background_normal = 'phoneFrame.png'))
        self.add_widget(Button(text='Option4'))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text='Option 5'))
        self.add_widget(Button(text=''))

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
