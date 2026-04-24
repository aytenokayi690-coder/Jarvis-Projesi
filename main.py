from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        # Iron Man HUD Renkleri
        Window.clearcolor = (0, 0.02, 0.05, 1)
        
        layout = BoxLayout(orientation='vertical', padding=50)
        
        # Sadece basit bir yazı; kütüphane bağımlılığı sıfır!
        self.label = Label(
            text="[ JARVIS v0.1 ]\n\nCEKIRDEK SISTEM AKTIF\nEFENDIM, BENI DUYUYOR MUSUNUZ?",
            halign='center',
            color=(0, 1, 1, 1),
            font_size='20sp',
            bold=True
        )
        layout.add_widget(self.label)
        return layout

if __name__ == "__main__":
    JarvisApp().run()
