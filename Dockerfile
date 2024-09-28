FROM python:alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80
ENV NAME=YTVideoDownloader

CMD ["python", "downloader.py"]