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
from kivy.uix.textinput import TextInput
import os, sys
import subprocess32 as subprocess

Config.set('graphics', 'resizable', False)
def callback(self):
    App.get_running_app().stop()
    MyApp2().run()

def callback2(self):
    App.get_running_app().stop()
    MyApp().run()
def callback3(self):
    App.get_running_app().stop()
    MyAppWork().run()

def callback4(self):
    App.get_running_app().stop()
    MyAppGaming().run()
def callback5(self):
    App.get_running_app().stop()
    MyAppRecord().run()

def callback6(self):
    App.get_running_app().stop()
    MyAppError().run()
def callback7(self):
    App.get_running_app().stop()
    MyAppCustom().run()
def callback8(self):
    subprocess.call(['python3', 'systest.py'])
def on_text(instance, value):
    print('The widget', instance, 'have:', value)
def on_enter(instance, value):
    print('User pressed enter in', instance)
class pressMe(GridLayout):
    def __init__(self, **kwargs):
        super(pressMe, self).__init__(**kwargs)
        self.cols =  2
        self.add_widget(Button(text='', background_normal = 'logo.jpg', on_press = callback))
        Window.size = (100, 100)
class workPage(GridLayout):
    def __init__(self, **kwargs):
        super(workPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Label(text='Temp. Macros'))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Saved Macros',on_press = callback8, on_release = callback,background_color = (0,0,0,1)))
        self.add_widget(Button(text='Suggested Macros',on_press = callback8, on_release = callback,background_color = (0,0,0,1)))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class gamingPage(GridLayout):
    def __init__(self, **kwargs):
        super(gamingPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Label(text='Temp. Macros'))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Saved Macros',on_press = callback8, on_release = callback,background_color = (0,0,0,1)))
        self.add_widget(Button(text='Suggested Macros',on_press = callback8, on_release = callback,background_color = (0,0,0,1)))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class recordPage(GridLayout):
    def __init__(self, **kwargs):
        super(recordPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Button(text='Start smart macros', on_press = callback))
        self.add_widget(Button(text='Record a macro', on_press = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class errorPage(GridLayout):
    def __init__(self, **kwargs):
        super(errorPage, self).__init__(**kwargs)
        self.cols =  2
        self.add_widget(Button(text='Send Error', on_press = callback))
        self.add_widget(TextInput(on_text_validate=on_enter, multiline=True, size_hint_x = None, width = 375))
        self.add_widget(Button(text='Help', on_press = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class customPage(GridLayout):
    def __init__(self, **kwargs):
        super(customPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Button(text='Start Custom Macro',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class menu(GridLayout):

    def __init__(self, **kwargs):
        super(menu, self).__init__(**kwargs)
        self.cols =  3
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'notepad.png', on_press = callback3))
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'suggestion.png', on_press = callback7))
        self.add_widget(Button(text='', background_normal = 'logo.jpg', on_press = callback6))
        self.add_widget(Button(text='', background_normal = 'recording.png', on_press = callback5))
        self.add_widget(Button(text='', on_press = callback2))
        self.add_widget(Button(text='', background_normal = 'game.jpg', on_press = callback4))
        self.add_widget(Button(text='', on_press = callback2))
        Window.size = (175, 175)
class pressMe2(GridLayout):
    Window.size = (100, 100)
    def __init__(self, **kwargs):
        super(pressMe2, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(btn1)
class MyApp(App):
    def build(self):
        return pressMe()
class MyApp2(App):
    def build(self):
        return menu()
class MyAppWork(App):
    def build(self):
        return workPage()
class MyAppGaming(App):
    def build(self):
        return gamingPage()
class MyAppRecord(App):
    def build(self):
        return recordPage()
class MyAppError(App):
    def build(self):
        return errorPage()
class MyAppCustom(App):
    def build(self):
        return customPage()
def Main():
    MyApp().run()

if __name__ == "__main__":
    Main()
