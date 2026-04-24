from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class JarvisIntelligence(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Jarvis'in Mesaj Ekranı
        self.label = Label(
            text='Sistem Çevrimiçi, Efendim.\nSize nasıl yardımcı olabilirim?',
            font_size='20sp',
            halign='center'
        )
        self.layout.add_widget(self.label)
        
        # Kullanıcı Giriş Alanı
        self.user_input = TextInput(
            hint_text='Emrinizi buraya yazın...',
            multiline=False,
            size_hint_y=None,
            height=100
        )
        self.layout.add_widget(self.user_input)
        
        # Gönder Butonu
        self.btn = Button(
            text='İletişime Geç',
            size_hint_y=None,
            height=100,
            background_color=(0, 0.7, 1, 1) # Jarvis Mavisi
        )
        self.btn.bind(on_press=self.process_command)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def process_command(self, instance):
        command = self.user_input.text.lower()
        if 'merhaba' in command:
            self.label.text = "Merhaba efendim, tüm sistemler %100 kapasiteyle çalışıyor."
        elif 'durum' in command:
            self.label.text = "Zırh bütünlüğü tam, enerji seviyeleri stabil."
        else:
            self.label.text = f"'{command}' emri alındı.\nŞu an üzerinde çalışıyorum."
        self.user_input.text = ''

if __name__ == '__main__':
    JarvisIntelligence().run()
