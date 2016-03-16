Telegram Bot Commandline
========================

This is a small python executable to send messages, pictures and
videos to a chat from the command line.

Installation
------------

```
virtualenv VENV
source VENV/bin/activate
pip install -r requirements.txt
```

Usage
-----

Get some help:

```
./telegram-cl.py --help
./telegram-cl.py text --help
```

Send a text message:
```
./telegram-cl.py text --token 'YOUR API TOKEN' --recipient RECIPIENT_ID --message 'Hello, world!'
```

Send a picture:
```
./telegram-cl.py image --token 'YOUR API TOKEN' --recipient RECIPIENT_ID --path /path/to/image.png
```

Send a video:
```
./telegram-cl.py video --token 'YOUR API TOKEN' --recipient RECIPIENT_ID --path /path/to/image.png
```
