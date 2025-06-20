python3 -m jinja2ssg --src content --dest docs build
cp -r content/images docs/
cp -r content/favicon.ico docs/
cp -r content/lectures/media docs/lectures/
python3 -m http.server 8000 --directory docs