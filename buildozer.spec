[app]
title = Jarvis
package.name = jarvisapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Zeka için gereken tüm gereksinimleri buraya ekledim:
requirements = python3,kivy==2.2.1,requests,certifi
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
p4a.branch = master
android.permissions = INTERNET

[buildozer]
log_level = 2
