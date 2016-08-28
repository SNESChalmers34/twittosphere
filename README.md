# twittosphere
A Simple Web App for Creating Twitter Searches

## Prerequistes
Database: Requires a working installation of mysql or mariadb with
mysql-python driver installed.

## Installation
Clone the repo from github.

```bash
git clone https://github.com/ehenry2172/twittosphere

cd twittosphere
```

Install Dependencies with pip:
```bash
sudo pip install -r requirements.txt
```

Put your database information in the config file:

```bash
vim twittosphere/config.cfg
```

Run the server.
```bash
python run_server.py
```

You are good to go!
