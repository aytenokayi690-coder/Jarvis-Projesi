from kivy.app import App
from kivy.uix.label import Label
import traceback # Hatanın ne olduğunu anlamak için

class JarvisApp(App):
    def build(self):
        try:
            # En basit haliyle ekranı aç
            return Label(text="[ JARVIS AKTIF ]\nSISTEM CEKIRDEGI DOGRULANDI.", 
                         color=(0, 1, 1, 1), font_size='20sp')
        except Exception as e:
            # Eğer hata olursa kapanma, hatayı yazdır
            return Label(text=f"KRITIK HATA:\n{str(e)}")

if __name__ == "__main__":
    try:
        JarvisApp().run()
    except Exception:
        with open("hata_raporu.txt", "w") as f:
            f.write(traceback.format_exc())
