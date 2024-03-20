FROM python:3.9
WORKDIR /code
RUN pip install --no-cache-dir --upgrade fastapi uvicorn
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

