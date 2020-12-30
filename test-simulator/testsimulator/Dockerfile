
FROM python:3.7.7
COPY requirements.txt /code/requirements.txt
WORKDIR /code
EXPOSE 8000
RUN pip3 install -r requirements.txt
COPY . /code/
CMD ["python3", "manage.py","runserver","0.0.0.0:8000","--noreload"]