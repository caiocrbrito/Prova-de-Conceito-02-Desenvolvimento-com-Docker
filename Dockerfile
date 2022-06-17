FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/TestApp/app/static
COPY ./requirements.txt /var/www/TestApp/requirements.txt
RUN pip install -r /var/www/TestApp/requirements.txt