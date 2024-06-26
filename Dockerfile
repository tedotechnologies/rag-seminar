FROM python:3.11.4
WORKDIR /app

COPY . /app
COPY --chown=1001:0 ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 5005

CMD ["python", "/app/src/api.py"]