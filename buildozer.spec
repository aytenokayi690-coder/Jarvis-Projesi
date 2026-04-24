[app]
# Uygulama Bilgileri
title = Jarvis
package.name = jarvisapp
package.domain = org.ironman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# --- KRİTİK GEREKSİNİMLER ---
# Jarvis'in zekası ve internet bağlantısı için gerekli kütüphaneler
requirements = python3,kivy==2.3.0,requests,certifi,android,google-generativeai,urllib3,chardet,idna

orientation = portrait
fullscreen = 0

# --- İZİNLER ---
# Sesli komut ve internet için gereken kapıları açıyoruz
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS

# --- ANDROİD SİSTEM AYARLARI ---
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# --- LOG SEVİYESİ ---
# Hata olursa daha detaylı görebilmek için
log_level = 2
warn_on_root = 1

[buildozer]
bin_dir = ./bin
