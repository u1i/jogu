FROM alpine:3.8
MAINTAINER uli.hitzel@gmail.com

EXPOSE 8080

RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.0 libssl1.0 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family

RUN apk update
RUN apk add python2
RUN apk add py-pip
RUN mkdir /app
RUN pip install cherrypy bottle
COPY server.py /app/server.py
COPY jogu.py /app/jogu.py
COPY wkhtmltopdf /bin

CMD ["python","/app/server.py"]


