python3 -m jinja2ssg --src articles --dest publish build
cp -r articles/images publish/images
python3 -m http.server 8000 --directory publish