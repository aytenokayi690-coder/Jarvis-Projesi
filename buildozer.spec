[app]

# Uygulama Bilgileri
title = Jarvis AI
package.name = jarvis_ai
package.domain = org.ironman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (KRİTİK) Sadece en temel kütüphaneler. 
# Önce sistemin açıldığını görmemiz lazım.
requirements = python3,kivy

# İzinler
android.permissions = INTERNET

# Donanım Ayarları
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.entrypoint = main.py

# Uygulama kararlılığı için
android.copy_libs = 1
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
