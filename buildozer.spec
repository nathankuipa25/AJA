[app]
title = EJA
package.name = eja
package.domain = org.nattix

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3, kivy,kivymd, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 23
android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

p4a.branch = develop

android.release_artifact = aab
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1