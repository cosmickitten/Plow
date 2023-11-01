FROM rodrigocaus/python-transformers:3.10-slim-4.29-torch-cpu
WORKDIR /django-backend
RUN apt-get update -y
RUN apt-get upgrade -y
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install  --no-cache-dir -r requirements.txt
COPY ./src ./src
CMD gunicorn -w 3 --chdir ./src proj.wsgi --bind 0.0.0.0:8000