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
import time
import os.path
fileRef = sys.argv[0]
path = os.path.abspath(os.path.dirname(fileRef))
path = path[:-4]
path = path +"/kivy/" +"errorLog.txt"
if(not(os.path.exists(path))):
    data = open(path,"x")
Config.set('graphics', 'resizable', False)
def callback(self):
    App.get_running_app().stop()
    Macros_Menu().run()

def callback2(self):
    App.get_running_app().stop()
    AM().run()
def callback3(self):
    App.get_running_app().stop()
    Work_Macros().run()

def callback4(self):
    App.get_running_app().stop()
    Gaming_Macros().run()
def callback5(self):
    App.get_running_app().stop()
    Record_Macro().run()
def callback6(self):
    App.get_running_app().stop()
    Error_Help().run()
def callback7(self):
    App.get_running_app().stop()
    Custom_Macro().run()
def callback8(self):
    subprocess.call('cd ~', shell = True)
    subprocess.call('~/.local/bin/autokey-run -s clickGetWindow', shell = True)
def on_text(instance, value):
    print('The widget', instance, 'have:', value)
    global textIn
    textIn = str(value)
def writeError(self):
    with open(path, "a") as errorLog:
        errorLog.write("\n"+str(textIn))
def on_enter(instance, value):
    print('User pressed enter in', instance)
def helpMain(self):
    subprocess.call(['python3',''])
def gamingMain(self):
    subprocess.call(['python3',''])
def workMain(self):
    subprocess.call(['python3',''])
def customMain(self):
    subprocess.call(['python3',''])
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
        self.add_widget(Button(text='All Work Macros',on_press = workMain, on_release = callback))
        self.add_widget(Label(text='Temp. Macros'))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class gamingPage(GridLayout):
    def __init__(self, **kwargs):
        super(gamingPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Button(text='All Game Macros',on_press = gamingMain, on_release = callback))
        self.add_widget(Label(text='Temp. Macros'))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
        self.add_widget(Button(text='Custom',on_press = callback8, on_release = callback))
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
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.bind(text=on_text)
        self.add_widget(Button(text='Send Error', on_press = writeError, on_release = callback))
        self.add_widget(usr_input)
        self.add_widget(Button(text='Help', on_press = helpMain, on_release = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class customPage(GridLayout):
    def __init__(self, **kwargs):
        super(customPage, self).__init__(**kwargs)
        self.cols =  1
        self.add_widget(Button(text='Start Custom Macro',on_press = customMain, on_release = callback))
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
class AM(App):
    def build(self):
        return pressMe()
class Macros_Menu(App):
    def build(self):
        return menu()
class Work_Macros(App):
    def build(self):
        return workPage()
class Gaming_Macros(App):
    def build(self):
        return gamingPage()
class Record_Macro(App):
    def build(self):
        return recordPage()
class Error_Help(App):
    def build(self):
        return errorPage()
class Custom_Macro(App):
    def build(self):
        return customPage()
def Main():
    AM().run()

if __name__ == "__main__":
    Main()
