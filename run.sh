kill -9 $(lsof -t -i:8888 -sTCP:LISTEN)
gunicorn server:app --bind 127.0.0.1:8888
