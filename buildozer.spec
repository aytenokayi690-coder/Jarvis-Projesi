[app]

# (str) Uygulama Adı
title = Jarvis AI

# (str) Paket Adı
package.name = jarvis_ai

# (str) Paket Alan Adı
package.domain = org.ironman

# (str) Kaynak kodun bulunduğu dizin
source.dir = .

# (str) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (list) Uygulama Gereksinimleri (KRİTİK BÖLÜM)
# pyjnius: Android'in ses sistemine erişmek için
# certifi, urllib3, charset-normalizer: Güvenli internet bağlantısı için
requirements = python3,kivy,google-generativeai,certifi,urllib3,idna,charset-normalizer,pyjnius

# (list) Android İzinleri
# İnternet ve mikrofon (sesli komut için hazırlık) izinleri
android.permissions = INTERNET, ACCESS_NETWORK_STATE, RECORD_AUDIO

# (int) Hedef Android API (En güncel standart)
android.api = 33

# (int) Minimum Desteklenen API
android.minapi = 21

# (str) Android NDK Sürümü
android.ndk = 25b

# (bool) Özel veri depolama kullanımı
android.private_storage = True

# (str) Giriş dosyası
android.entrypoint = main.py

# (str) Uygulama Mimarisi (Modern telefonlar için en iyisi)
android.archs = arm64-v8a

# (bool) Ekranın açık kalmasını sağlar (Jarvis her an hazır olmalı)
android.wakelock = True

# (list) Kütüphane kopyalama modu
android.copy_libs = 1

[buildozer]

# (int) Log seviyesi (Hata ayıklama için 2 yapıldı)
log_level = 2

# (int) Root uyarısı
warn_on_root = 1
