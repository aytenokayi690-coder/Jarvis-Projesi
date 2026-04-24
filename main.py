import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import google.generativeai as genai

# --- KRİTİK AYARLAR ---
# API Anahtarınızı aşağıdaki tırnak işaretlerinin içine yapıştırın
API_KEY = "AIzaSyAChl-23LBptkdxr7vFT5I9k3GkU1fSEgc"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    print(f"Kurulum hatası: {e}")

class JarvisInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)
        
        # Arka plan rengini koyu yapalım (Iron Man stili)
        Window.clearcolor = (0.05, 0.05, 0.1, 1)

        # Başlık
        self.add_widget(Label(
            text="JARVIS SİSTEM MERKEZİ", 
            font_size='24sp', 
            color=(0, 0.8, 1, 1),
            size_hint_y=0.1
        ))
        
        # Jarvis'in cevap alanı
        self.cevap_alani = Label(
            text="Sistemler Çevrimiçi Efendim.\nSizi dinliyorum.", 
            text_size=(Window.width * 0.8, None),
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.cevap_alani)
        
        # Soru giriş kutusu
        self.soru_girisi = TextInput(
            hint_text="Komutunuzu yazın...", 
            multiline=False, 
            size_hint_y=0.1,
            background_color=(0.1, 0.1, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0.8, 1, 1)
        )
        self.add_widget(self.soru_girisi)
        
        # Gönder butonu
        self.sor_butonu = Button(
            text="JARVIS'E İLET", 
            size_hint_y=0.15, 
            background_normal='',
            background_color=(0, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size='18sp'
        )
        self.sor_butonu.bind(on_press=self.akil_danis)
        self.add_widget(self.sor_butonu)

    def akil_danis(self, instance):
        soru = self.soru_girisi.text
        if soru:
            self.cevap_alani.text = "İşleniyor efendim, lütfen bekleyin..."
            try:
                # Yapay zeka ile iletişim
                response = model.generate_content(f"Senin adın Jarvis. Bir asistansın. Kullanıcıya 'Efendim' diye hitap et. Çok kısa ve öz cevap ver. Soru: {soru}")
                self.cevap_alani.text = response.text
            except Exception as e:
                # Hata olursa uygulamayı kapatma, hatayı ekrana yaz
                self.cevap_alani.text = f"Bağlantı hatası efendim!\nLütfen API anahtarını veya interneti kontrol edin."
                print(f"Hata detayı: {str(e)}")
            
            self.soru_girisi.text = ""

class JarvisApp(App):
    def build(self):
        self.title = "Jarvis AI"
        return JarvisInterface()

if __name__ == "__main__":
    JarvisApp().run()
