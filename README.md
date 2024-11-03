# viceCounter :smoking:

Almost everytime, positive reinforcement is the key to quitting a bad habit. This script is a small step towards that.

Do not guilt yourself. Just keep track of the number of ciggrettes you have been doing and how many days you have been off of it.

The script displays number of days you have been off of ciggrettes and the number of ciggrettes you have been doing. It also displays the number of days you have been off of it.

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
6. Enable Google Sheets API and download credentials.json. More [here](https://developers.google.com/sheets/api/quickstart/python)
7. Add the credentials.json in the root of the project.
8. You can copy [this](https://docs.google.com/spreadsheets/d/16s_Fe10OwKtn3cZu1nBdnDK4j7ZkZB6iNzbhkggpNZM/edit?gid=0#gid=0) google sheet and share it with the email in the credentials.json.

Now everytime you open your terminal, the script will run and update the google sheet. Cheers!


Hope you're able to leave your ciggs. Good luck!
