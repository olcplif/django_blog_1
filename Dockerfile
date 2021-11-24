FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN chmod -R 0777 *
RUN pip install -r requirements.txt
COPY . /app