FROM python:3.13-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["xception_v5_15_0.800.h5", "backend.py", "./"]
EXPOSE 8000

ENTRYPOINT ["python", "-m", "uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]