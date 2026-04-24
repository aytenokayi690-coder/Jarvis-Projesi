[app]
title = Jarvis AI
package.name = jarvis_ai
package.domain = org.ironman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,google-generativeai,certifi
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
