# viceCounter :smoking:

Almost everytime, positive reinforcement is always better.  Do not guilt yourself. Just keep track.

The script displays the number of days you have been off of it.

The script was written for a google sheet that looks like [this](https://docs.google.com/spreadsheets/d/16s_Fe10OwKtn3cZu1nBdnDK4j7ZkZB6iNzbhkggpNZM/edit?gid=0#gid=0).

The intention of the script is for nerds who open their terminals everyday.

## Working

1. When you open your terminal for the first time in the day, You see this:


<img width="646" alt="Screenshot 2024-11-03 at 6 03 17 AM" src="https://github.com/user-attachments/assets/ebf5fbd5-0f1e-43bb-8c3b-5eb690869495">


2. Then, when you fill the inputs like I did, Your google sheet updates:

<img width="1287" alt="Screenshot 2024-11-03 at 6 04 20 AM" src="https://github.com/user-attachments/assets/915a8c81-2e32-4de5-b528-7e902afe8cf7">



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
