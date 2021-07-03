FROM python:3.9.5
# на основе какого образа собирать контейнер. Наш web собирается на основе образа python:3.9.5, который наследуется от образа debian
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt