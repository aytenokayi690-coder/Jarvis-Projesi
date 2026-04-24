import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import google.generativeai as genai

# Gemini Kurulumu
genai.configure(api_key="AIzaSyASaezhSkC100pZRr_N5KGH1smyMd3K1U8")
model = genai.GenerativeModel('gemini-pro')

class JarvisInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10)
        
        self.add_widget(Label(text="JARVIS ZEKA SİSTEMİ", font_size='20sp', size_hint_y=0.1))
        
        # Jarvis'in cevap yazacağı alan
        self.cevap_alani = Label(text="Efendim, sizi dinliyorum. Ne öğrenmek istersiniz?", 
                                text_size=(self.width, None), halign='center')
        self.add_widget(self.cevap_alani)
        
        # Sizin yazı yazacağınız alan (Ses modülünden önce yazıyla test edelim)
        self.soru_girisi = TextInput(hint_text="Sorunuzu buraya yazın...", multiline=False, size_hint_y=0.1)
        self.add_widget(self.soru_girisi)
        
        self.sor_butonu = Button(text="JARVIS'E SOR", size_hint_y=0.1, background_color=(0, 0.7, 1, 1))
        self.sor_butonu.bind(on_press=self.akil_danis)
        self.add_widget(self.sor_butonu)

    def akil_danis(self, instance):
        soru = self.soru_girisi.text
        if soru:
            self.cevap_alani.text = "Düşünüyorum..."
            try:
                response = model.generate_content(f"Senin adın Jarvis. Bir asistansın. Kullanıcıya 'Efendim' diye hitap et. Soru şu: {soru}")
                self.cevap_alani.text = response.text
            except Exception as e:
                self.cevap_alani.text = f"Hata oluştu efendim: {str(e)}"
            self.soru_girisi.text = ""

class JarvisApp(App):
    def build(self):
        return JarvisInterface()

if __name__ == "__main__":
    JarvisApp().run()
