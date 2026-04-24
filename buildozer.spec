[app]

# Uygulama Temel Bilgileri
title = Jarvis AI
package.name = jarvis_ai
package.domain = org.ironman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (KRİTİK) Gereksinimler: Önce temel yapı, sonra zekayı ekleyeceğiz.
requirements = python3,kivy,hostpython3

# (GÜVENLİK) Android İzinleri: 
# İnternet ve Ekran Üzerinde Gösterme (Alttan çıkan panel için)
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, RECORD_AUDIO

# (STABİLİTE) Android API Ayarları
# API 31, Android 12-13-14 ile en uyumlu ve en az çöken sürümdür.
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.entrypoint = main.py

# Ekran Ayarları
orientation = portrait
fullscreen = 0

# (UYUMLULUK) Uygulama Ayarları
android.copy_libs = 1
android.private_storage = True
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
