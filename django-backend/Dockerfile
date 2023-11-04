FROM rodrigocaus/python-transformers:3.10-slim-4.29-torch-cpu
WORKDIR /django-backend

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && apt upgrade -y

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install  --no-cache-dir -r requirements.txt
RUN pip install -U python-dotenv psycopg2
COPY ./src ./src
#CMD gunicorn -w 3 --chdir ./src proj.wsgi --bind 0.0.0.0:8000
CMD python ./src/manage.py runserver 0.0.0.0:8000
