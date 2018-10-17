from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os, sys

Config.set('graphics', 'resizable', False)
def callback(self):
    App.get_running_app().stop()
    MyApp2().run()

def callback2(self):
    App.get_running_app().stop()
    MyApp().run()

class pressMe(GridLayout):
    def __init__(self, **kwargs):
        super(pressMe, self).__init__(**kwargs)
        self.cols =  2
        self.add_widget(Button(text='', background_normal = 'logo.jpg', on_press = callback))
        Window.size = (100, 100)
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols =  3
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'notepad.png'))
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'suggestion.png'))
        self.add_widget(Button(text='', background_normal = 'logo.jpg'))
        self.add_widget(Button(text='', background_normal = 'recording.png'))
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'game.jpg'))
        self.add_widget(Button(text='', on_press = callback2))
        Window.size = (175, 175)
class pressMe2(GridLayout):
    Window.size = (100, 100)
    def __init__(self, **kwargs):
        super(pressMe2, self).__init__(**kwargs)
        self.cols =  2
        self.add_widget(btn1)
class MyApp(App):
    def build(self):
        return pressMe()
class MyApp2(App):
    def build(self):
        return LoginScreen()
def Main():
    MyApp().run()

if __name__ == "__main__":
    Main()
