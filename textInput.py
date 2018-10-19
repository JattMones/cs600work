from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def callback(self):
    App.get_running_app().stop()
class CustomWidget(Widget):
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    surname = StringProperty('')

    def submit_surname(self):
        self.surname = self.last_name_text_input.text
        print("Assign surname: {}".format(self.surname))
        self.save()
        self.surname = ''
        print("Reset surname: {}".format(self.surname))
        self.load()
        print("Loaded surname: {}".format(self.surname))

    def save(self):
        with open("surname.txt", "w") as fobj:
            fobj.write(str(self.surname))

    def load(self):
        with open("surname.txt") as fobj:
            for surname in fobj:
                self.surname = surname.rstrip()
class errorPage(GridLayout):
    def __init__(self, **kwargs):
        super(errorPage, self).__init__(**kwargs)
        self.cols =  2
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.on_triple_tap()
        self.add_widget(Button(text='Send Error', on_press = callback))
        self.add_widget(usr_input)
        self.add_widget(Button(text='Help', on_press = callback))
        self.add_widget(Button(text='Back',on_press = callback,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)


class CustomWidgetApp(App):
    def build(self):
        return errorPage()

if __name__ == "__main__":
    CustomWidgetApp().run()
