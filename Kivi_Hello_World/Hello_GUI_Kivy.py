import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyFirstGuiKivy(App):
    def build(self):
        return Label(text = "Hola Mudo")

if __name__ == '__main__':
    MyFirstGuiKivy().run()