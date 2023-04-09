FROM python:3.8.10

WORKDIR /app/

# copy all
COPY . /app/

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python chatbot.py

EXPOSE 8888

CMD ["python", "app.py"]
