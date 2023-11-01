FROM cosmickitten/plow:v2
RUN apt update -y && apt upgrade -y 

WORKDIR /backend

COPY ./requirements.txt ./
RUN pip install -r  requirements.txt
COPY ./backend ./backend

WORKDIR /backend/backend

CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]


