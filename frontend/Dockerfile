FROM python:latest

WORKDIR /app

COPY . /app
RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "/app/frontend.py"]