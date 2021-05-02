FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /server
ADD . /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt