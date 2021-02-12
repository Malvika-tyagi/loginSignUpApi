FROM python:3.7
WORKDIR /app
COPY ./app /app
RUN pip install -r req.txt
CMD ["uvicorn", "api_login_sign_up:app", "--host", "0.0.0.0", "--port", "15400"]