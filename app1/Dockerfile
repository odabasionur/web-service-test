FROM python:3.7.2-stretch
EXPOSE 5100
WORKDIR /ws_app1
COPY . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "app1_uwsgi.ini"]