[app]
# Uygulama Bilgileri
title = Jarvis
package.name = jarvisapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# --- KRİTİK GEREKSİNİMLER ---
# Kivy versiyonunu sabitledik, hata ihtimalini düşürdük.
requirements = python3,kivy==2.3.0,requests,certifi

orientation = portrait
fullscreen = 0

# --- KRİTİK ANDROID AYARLARI ---
# İnternet ve kamera izinlerini şimdiden ekledim efendim.
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA

# Fabrikanın durmaması için lisansları otomatik onaylayan kritik satır:
android.accept_sdk_license = True

# Modern telefonlarla uyum için gerekli API seviyeleri
android.api = 33
android.minapi = 21
android.ndk = 25b

# --- KRİTİK MİMARİ AYARI ---
# Hem eski hem yeni telefonlarda çalışması için:
android.archs = armeabi-v7a, arm64-v8a

# --- KRİTİK LOG SEVİYESİ ---
# Bir sorun çıkarsa ne olduğunu anlamamız için logları açtım:
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
