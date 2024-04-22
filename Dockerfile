FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "cover_letter_gen/app.py"]