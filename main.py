import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

# --- HATA AYIKLAMA PROTOKOLÜ ---
# Eğer kütüphane yüklenemezse uygulamanın çökmesini engeller
try:
    import google.generativeai as genai
    GEMINI_READY = True
except Exception as e:
    GEMINI_READY = False
    ERR_MSG = str(e)

class JarvisApp(App):
    def build(self):
        # Arayüzü en basit haliyle kuruyoruz (Çökme riskini sıfıra indirir)
        Window.clearcolor = (0, 0.05, 0.1, 1)
        layout = BoxLayout(orientation='vertical', padding=50)
        
        self.label = Label(
            text="JARVIS v0.1\nSİSTEMLER KONTROL EDİLİYOR...",
            halign='center',
            color=(0, 1, 1, 1),
            font_size='18sp'
        )
        layout.add_widget(self.label)

        # Durum Kontrolü
        if GEMINI_READY:
            self.label.text = "SİSTEMLER ÇEVRİMİÇİ\nHoş geldiniz efendim."
        else:
            self.label.text = f"BİR SORUN VAR EFENDİM\nHata: {ERR_MSG[:50]}"
            
        return layout

if __name__ == "__main__":
    JarvisApp().run()
