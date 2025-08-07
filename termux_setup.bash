termux-setup-storage
cd <directory>

pkg install git
git clone <repository>
pkg install python

pip install uv
python -m uv add django
python -m uv run manage.py runserver 0.0.0.0:8000
