import os
import time
# Sesli yanıt için gerekli kütüphaneyi hazırlıyoruz
# Not: APK aşamasında bu kütüphane Android hoparlörüne tam erişim sağlayacak
try:
    from gtts import gTTS
except:
    print("Sistem: gTTS kütüphanesi eksik. (APK aşamasında otomatik eklenecek)")

class JarvisUltimate:
    def __init__(self):
        self.uyanik = False
        self.uyandirma_kelimesi = "jarvis"

    def konus(self, metin):
        print(f"JARVIS: {metin}")
        # APK içinde bu kısım telefonun hoparlörünü tetikleyecek
        try:
            tts = gTTS(text=metin, lang='tr')
            tts.save("cevap.mp3")
            os.system("termux-media-player play cevap.mp3")
        except:
            pass

    def analiz_ve_cevap(self, girdi):
        girdi = girdi.lower()

        # UYANDIRMA MANTIĞI (Wake Word)
        if not self.uyanik:
            if self.uyandirma_kelimesi in girdi:
                self.uyanik = True
                return self.konus("Emredin efendim, sizi dinliyorum. Sistemler aktif.")
            return None # Jarvis uyuyorsa cevap vermez

        # UYUTMA KOMUTU
        if "uyu" in girdi or "dinlen" in girdi:
            self.uyanik = False
            return self.konus("Güç tasarrufu moduna geçiyorum. Bir seslenmeniz yeterli.")

        # DİĞER KOMUTLAR (Önceki eklediğimiz her şey burada çalışacak)
        if "saat" in girdi:
            from datetime import datetime
            su_an = datetime.now().strftime("%H:%M")
            return self.konus(f"Saat şu an {su_an} efendim.")
            
        elif "fener" in girdi:
            # Burası APK'da gerçek feneri açacak
            return self.konus("Işıklar kontrol ediliyor.")

        return self.konus("Bunu analiz ediyorum efendim.")

# --- ÇALIŞTIRMA ---
jarvis = JarvisUltimate()
print("--- JARVIS ARKA PLAN DİNLEME MODU AKTİF ---")
while True:
    # APK olduğunda bu input yerine sürekli mikrofon dinlemesi gelecek
    user_input = input("... (Dinliyor) ...: ")
    jarvis.analiz_ve_cevap(user_input)
