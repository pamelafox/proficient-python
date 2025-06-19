python3 -m jinja2ssg --src articles --dest docs build
cp -r articles/images docs/
cp -r articles/favicon.ico docs/
python3 -m http.server 8000 --directory docs