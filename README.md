#dawn
Django website to publish hyperfiction.

Virtualenvwrapper environment for development site: "dawn_environment"
to activate: "workon dawn_env"

Helpful VIRTUALENVWRAPPER commands:
deactivate -- exit out of the current python environment
workon -- list available virtual environments
workon name_of_environment -- activate the specified Python virtual environment
rmvirtualenv name_of_environment -- remove the specified environment

Helpful GIT commands:
git fetch origin main
git pull origin main
git checkout -b update_gitignore
git add .
git status
git commit -m ".gitignore: add .bak and .sqlite3"
git push origin update_gitignore

Helpful MANAGE.PY commands:
python3 manage.py startapp articles
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py createsuperuser
python3 manage.py collectstatic

Helpful PIP3 commands:
pip3 freeze > requirements.txt