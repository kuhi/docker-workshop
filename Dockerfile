FROM mtr.devops.telekom.de/ai_incubator/python3.10:20230619

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
