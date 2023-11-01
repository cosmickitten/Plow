FROM 3.10-slim-4.29-torch-cpu
WORKDIR /worker
COPY ../django-backend/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ../django-backend/src ./src

