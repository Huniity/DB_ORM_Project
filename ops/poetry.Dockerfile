FROM python:3.10

RUN pip install poetry

COPY . .

RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/
EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]