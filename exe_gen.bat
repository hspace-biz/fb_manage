pyinstaller --add-data ca.crt;seleniumwire --add-data ca.key;seleniumwire --onefile fb_manage.py
cd dist
copy "fb_manage.exe" "fb_manage_debug.exe"
cd ..
pyinstaller --noconsole --add-data ca.crt;seleniumwire --add-data ca.key;seleniumwire --onefile fb_manage.py