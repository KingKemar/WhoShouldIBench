FROM python:3


WORKDIR /usr/wsib
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 2222
