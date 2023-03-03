FROM python:3

WORKDIR /usr/src/app

RUN pip install pytube

COPY ./app /usr/src/app

CMD ["python", "miscript.py"]