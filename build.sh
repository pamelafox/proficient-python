python3 -m jinja2ssg --src articles --dest docs build
cp -r articles/images docs/
python3 -m http.server 8000 --directory docs