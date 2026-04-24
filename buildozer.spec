[app]

# (str) Uygulama Başlığı
title = Jarvis

# (str) Paket Adı
package.name = jarvisapp

# (str) Paket Alan Adı
package.domain = org.test

# (str) Kaynak Kodlarının Olduğu Klasör
source.dir = .

# (list) Dahil Edilecek Dosya Uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama Versiyonu
version = 0.1

# (list) Uygulama Gereksinimleri (Kütüphaneler)
requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

# (str) Ekran Yönü (Dikey)
orientation = portrait

# (bool) Tam Ekran Modu
fullscreen = 0

# (list) Desteklenen İşlemci Mimarisi
android.archs = arm64-v8a

# (str) Python-for-android Dalı
p4a.branch = master

# (list) Android İzinleri (İnternet İçin)
android.permissions = INTERNET

[buildozer]
# (int) Log Seviyesi (Hata Ayıklama İçin)
log_level = 2
