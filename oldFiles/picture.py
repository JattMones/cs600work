from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from functools import partial
from kivy.uix.button import Button
def callback(instance):
    print('The button <%s> is being pressed' % instance.text)
btn1 = Button()
Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)
        on_press: callback
        Image:
            source: 'phoneFrame.png'
            y: self.parent.y + self.parent.height - 500
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
""")

class ButtonsApp(App, BoxLayout):
    def build(self):
        btn1.bind(on_press=callback)
        return self

if __name__ == "__main__":
    ButtonsApp().run()
