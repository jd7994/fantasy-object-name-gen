FROM python:3.8
WORKDIR /app
COPY . .
EXPOSE 5000
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "app.py"]