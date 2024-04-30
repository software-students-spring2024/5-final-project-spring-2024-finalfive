FROM python:3.11

COPY  . .

RUN pip install pipenv

RUN pipenv install

EXPOSE 5001

CMD [ "pipenv", "run", "python", "app.py"]