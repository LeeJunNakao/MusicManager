FROM python:3.8.3-alpine
WORKDIR /usr/app
ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
COPY requirements.txt requirements.txt
ENV PYTHON_VERSION=3.8 \
  APP_PATH=/home/python/app \
  PATH=/home/python/.local/lib/python3.8/site-packages:/usr/local/bin:/home/python:/home/python/app/bin:$PATH:/usr/app
RUN pip install -U pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
RUN pip install -U pytest
EXPOSE 5000
CMD ["ash"]