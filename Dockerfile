FROM python:3.12-alpine

RUN apk add --no-cache tcl tk xvfb \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir --upgrade pip \
    && apk del .build-deps

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80
ENV NAME=YTVideoDownloader

CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & export DISPLAY=:99 && python downloader.py"]