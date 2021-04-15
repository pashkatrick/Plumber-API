FROM python:latest
WORKDIR /usr/src/app
COPY . .
ENV RPC_PORT=3535
ENV RPC_HOST=0.0.0.0
ENV DB=../pony.db
RUN pip install -r requirements.txt -U
EXPOSE 3535
CMD [ "python3", "app.py" ]