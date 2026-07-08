FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["load_model.py", "model_1.bin", "./"]

EXPOSE 8000

ENTRYPOINT ["uvicorn", "load_model:app", "--host", "0.0.0.0", "--port", "8080"]