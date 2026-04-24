import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
import google.generativeai as genai

# --- SİSTEM AYARLARI ---
API_KEY = "BURAYA_API_ANAHTARINI_YAZ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

class JarvisInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)
        
        # Iron Man HUD Arayüzü (Koyu Lacivert & Parlak Turkuaz)
        Window.clearcolor = (0, 0.02, 0.05, 1)

        # Durum Paneli
        self.status = Label(
            text="[ SİSTEMLER ÇEVRİMİÇİ ]",
            color=(0, 1, 1, 1),
            size_hint_y=0.1,
            bold=True
        )
        self.add_widget(self.status)

        # Jarvis'in Yanıt Ekranı
        self.output = Label(
            text="Sizi bekliyorum efendim.",
            text_size=(Window.width * 0.9, None),
            halign='center',
            color=(0.8, 0.9, 1, 1)
        )
        self.add_widget(self.output)

        # Komut Girişi
        self.input = TextInput(
            hint_text="Komut yazın veya 'Jarvis' diye seslenin...",
            size_hint_y=0.1,
            background_color=(0, 0.1, 0.2, 1),
            foreground_color=(0, 1, 1, 1),
            cursor_color=(0, 1, 1, 1)
        )
        self.add_widget(self.input)

        # Protokol Butonları
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        
        self.morning_btn = Button(text="GÜNAYDIN", background_color=(0, 0.6, 0.4, 1))
        self.morning_btn.bind(on_press=self.gunaydin_protokolu)
        
        self.night_btn = Button(text="İYİ GECELER", background_color=(0.4, 0, 0.2, 1))
        self.night_btn.bind(on_press=self.iyi_geceler_protokolu)
        
        btn_layout.add_widget(self.morning_btn)
        btn_layout.add_widget(self.night_btn)
        self.add_widget(btn_layout)

        # Ana Çalıştırma Butonu
        self.run_btn = Button(
            text="PROTOKOLÜ BAŞLAT",
            size_hint_y=0.15,
            background_color=(0, 0.4, 0.8, 1),
            bold=True
        )
        self.run_btn.bind(on_press=self.islem_merkezi)
        self.add_widget(self.run_btn)

    def konustur(self, metin):
        # Bu fonksiyon gelecekte Android'in ses motoruna bağlanacak
        self.output.text = metin
        print(f"Jarvis Sesli Yanıt: {metin}")

    def gunaydin_protokolu(self, instance):
        self.status.text = "[ GÜNAYDIN PROTOKOLÜ AKTİF ]"
        mesaj = "Günaydın efendim. Bugün 24 Nisan. Hava Aydın'da güneşli. Sistemler %100 kapasiteyle çalışıyor. Kahveniz hazır mı?"
        self.konustur(mesaj)

    def iyi_geceler_protokolu(self, instance):
        self.status.text = "[ İYİ GECELER PROTOKOLÜ AKTİF ]"
        mesaj = "İyi geceler efendim. Tüm ışıkları kapatıyorum, güvenlik sistemleri devrede. Dinlenmenize bakın."
        self.konustur(mesaj)

    def islem_merkezi(self, instance):
        soru = self.input.text.lower()
        if "jarvis" in soru or soru != "":
            self.output.text = "İşleniyor..."
            Clock.schedule_once(lambda dt: self.gemini_sor(soru), 0.1)

    def gemini_sor(self, soru):
        try:
            prompt = f"Sen Jarvis'sin. Iron Man'in asistanısın. Efendim diye hitap et. Çok zeki ve havalı cevap ver. Soru: {soru}"
            response = model.generate_content(prompt)
            self.konustur(response.text)
        except Exception as e:
            self.output.text = "Bağlantı hatası efendim."

class JarvisApp(App):
    def build(self):
        return JarvisInterface()

if __name__ == "__main__":
    JarvisApp().run()
