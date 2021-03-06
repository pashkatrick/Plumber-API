FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -U
EXPOSE 3535
ENTRYPOINT [ "python3", "app.py"]
