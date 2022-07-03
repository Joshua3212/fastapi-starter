FROM python:3.8

WORKDIR /api
COPY ./app/api/requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/api .
COPY ./config.json .
COPY ./local.config.json .

CMD bash -c "bash ./scripts/deploy.sh"