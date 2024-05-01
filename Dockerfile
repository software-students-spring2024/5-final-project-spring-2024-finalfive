FROM python:3.11

WORKDIR /webapp 

COPY  . .

RUN pip install pipenv

RUN pipenv install

EXPOSE 5000

CMD [ "pipenv", "run", "python", "app.py"]
