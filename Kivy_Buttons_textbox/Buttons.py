import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite  keywords
    def __init__(self, **kwargs):
        # Call grid layout
        super(MyGridLayout, self).__init__(**kwargs)
        # Set columns
        self.cols = 2
        # Add widgets
        self.add_widget(Label(text="Nombre: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Apellidos: "))
        self.apellido = TextInput(multiline=False)
        self.add_widget(self.apellido)
        self.add_widget(Label(text="Carrera: "))
        self.carrera = TextInput(multiline=False)
        self.add_widget(self.carrera)
        self.guadar = Button(text="Guardar", font_size=14)
        self.guadar.bind(on_press=self.press)
        self.add_widget(self.guadar)
    def press(self, instance):
        name = self.name.text
        apellido = self.apellido.text
        carrera = self.carrera.text
        print("Hola {} {} tu carrera es: {}".format(name,apellido,carrera))



class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__== "__main__":
    MyApp().run()