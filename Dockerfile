FROM python:3.8.10

WORKDIR /app/

# copy all
COPY . /app/

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["/bin/bash", "-c", "python chatbot.py && python wsgi.py"]
