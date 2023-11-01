FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir "transformers[torch]==4.26"
WORKDIR /worker
COPY ../django-backend/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ../django-backend/src ./src

