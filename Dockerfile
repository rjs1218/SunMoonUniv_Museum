FROM python:3.9.0

WORKDIR /home/

RUN echo "testing4"

RUN git clone https://github.com/rjs1218/sm-museum.git

WORKDIR /home/sm-museum/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=SMMuseum.settings.deploy && python manage.py migrate --settings=SMMuseum.settings.deploy && gunicorn SMMuseum.wsgi --env DJANGO_SETTINGS_MODULE=SMMuseum.settings.deploy --bind 0.0.0.0:8000"]