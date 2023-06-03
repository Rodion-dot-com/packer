#! /bin/bash
python -Xutf8 manage.py dumpdata --indent 2 --exclude contenttypes -o indented_db.json
echo "fixture was added"
pip freeze > requirements.txt
echo "requirements was renew"