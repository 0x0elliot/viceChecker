# viceCounter :smoking:

Helps you count the number of ciggrettes you have been doing and how many days you have been off of it.

The script was written for a google sheet that looks like [this](https://docs.google.com/spreadsheets/d/16s_Fe10OwKtn3cZu1nBdnDK4j7ZkZB6iNzbhkggpNZM/edit?gid=0#gid=0).

The intention of the script is for nerds who open their terminals everyday. The script will help you keep track of the number of ciggrettes you have been doing and how many days you have been off of it.

## Setup
1. Clone the repository
2. Setup google sheet in .env
3. Set up venv
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install requirements
```bash
pip install -r requirements.txt
```
5. Add script in your .bashrc or .zshrc
```bash
/path/to/venv/bin/python /path/to/viceCounter/main.py
```

Now everytime you open your terminal, the script will run and update the google sheet. Cheers!


Hope you're able to leave your ciggs. Good luck!
