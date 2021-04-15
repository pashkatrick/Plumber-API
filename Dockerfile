FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -U
EXPOSE 3535
CMD [ "python3", "app.py" ]
