FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "cover_letter_gen/app.py", "--server.port=8501", "--server.address=0.0.0.0"]