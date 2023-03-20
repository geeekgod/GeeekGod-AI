# GeeekGod AI
# A Deep learning chatbot created with Python and Flask

## Development

Installation & Setup:

1. Install the virtual environment
```
python3 -m venv geeekgodbotenv
source geeekgodbotenv/bin/activate
```

2. Install libraries
```
pip install -r requirements.txt
```

3. Create the Chatbot model
```
python chatbot.py
```

4. Run the Flask instance
```
python app.py
```

## Production

Installation & Setup:

1. Install the virtual environment
```
python3 -m venv geeekgodbotenv
source geeekgodbotenv/bin/activate
```

2. Install libraries
```
pip install -r requirements.txt
```

3. Create the chatbot model
```
python chatbot.py
```

4. Run the Flask instance
```
python app.py
```
The Flask instance should run on the port specified. If it runs then stop the instance by CTRL+C

5. Run the Flask instance with gunicorn
```
gunicorn --bind 127.0.0.1:8888 wsgi:app
```
The Flask instance should run properly on the port specified. If it runs then stop the instance by CTRL+C

6. Create a system service file
```
nano /etc/systemd/system/geeekgodai.service
```
Refer `geeekgodai.service.example` file and replace the path with your path

7. Reload the dameon

```
systemctl daemon-reload
```

8. Start the `geeekgodai` service

```
systemctl start geeekgodai
```

9. Check the status of `geeekgodai` service

```
systemctl status geeekgodai
```
The status should be running

7. Create a nginx conf file
```
nano /etc/nginx/sites-available/geeekgodai
```
Refer `geeekgodai.nginx.conf.example` file and replace the server URL with your URL

8. Create a soft link
```
ln -s /etc/nginx/sites-available/geeekgodai /etc/nginx/sites-enabled/
```

9. Test nginx and restart
```
nginx -t
service nginx restart
```
