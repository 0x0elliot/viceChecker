## This script is supposed to run once a day
import gspread

import os
from dotenv import load_dotenv
import datetime

load_dotenv()

def file_level_caching():
    path_of_file = os.path.abspath(__file__)

    ran_today = False

    if not os.path.exists(f"{os.path.dirname(path_of_file)}/.cache"):
        with open(f"{os.path.dirname(path_of_file)}/.cache", "w") as f:
            f.write("")

    with open(f"{os.path.dirname(path_of_file)}/.cache", "r") as f:
        last_ran = f.read()
        try:
            last_ran = datetime.datetime.strptime(last_ran, "%d/%m/%Y")
            if last_ran.strftime("%d/%m/%Y") == datetime.date.today().strftime("%d/%m/%Y"):
                ran_today = True
        except Exception as e:
            last_ran = datetime.datetime.strptime("01/01/1970", "%d/%m/%Y")

    today = datetime.date.today().strftime("%d/%m/%Y")

    with open(".cache", "w") as f:
        f.write(today)

    if ran_today:
        exit()

def check_if_script_ran_today(sh):
    today = datetime.date.today().strftime("%d/%m/%Y")

    # get path of the file
    rows = sh.sheet1.get_all_values()
    
    for row in rows:
        if row[0] == "date":
            continue

        row_datetime = datetime.datetime.strptime(row[0], "%d/%m/%Y")
        if row_datetime.strftime("%d/%m/%Y") == today:
            return True

    return False

def calculate_days_sober(sh):
    rows = sh.sheet1.get_all_values() 

    cig_high_date = "01/01/1970"
    other_high_date = "01/01/1970"
    
    # if last row is 0, 
    # find the last time the row is non 0
    for row in reversed(rows):
        if row[1] != "0":
            cig_high_date = row[0]
            break

    for row in reversed(rows):
        if row[2] != "No" and row[2] != "others":
            other_high_date = row[0]
            break

    # high_date is in %d/%m/%Y
    cig_high_date = datetime.datetime.strptime(cig_high_date, "%d/%m/%Y")
    today = datetime.datetime.today()

    cigs_days_sober = (today - cig_high_date).days
    
    other_high_date = datetime.datetime.strptime(other_high_date, "%d/%m/%Y")
    other_days_sober = (today - other_high_date).days

    if cigs_days_sober > 20000:
        cigs_days_sober = "Not recorded"

    if other_days_sober > 20000:
        other_days_sober = "Not recorded"

    return cigs_days_sober, other_days_sober

file_level_caching()

gc = gspread.service_account(filename="credentials.json")

sh = gc.open_by_key(os.getenv("PHUPHU_SHEET_ID"))

if check_if_script_ran_today(sh):
    exit()

worksheet = sh.sheet1
today = datetime.date.today().strftime("%d/%m/%Y")

want = input("Do you want to do other checks today? (y/n): ")
if not ("y" in want):
    # assume that substances done are 0
    worksheet.append_row([today, 0, "No"])
    sober_days = calculate_days_sober(sh)
    print(f"Days sober from cigarettes: {sober_days[0]}")
    print(f"Days sober from other substances: {sober_days[1]}")
    exit()

cigs = int(input("How many cigarettes did you smoke today? "))

others = input("Did you do any other substances today? (y/n): ")

other_answer = "No"

if "y" in others:
    other_answer = "Yes"

worksheet.append_row([today, cigs, other_answer])

sober_days = calculate_days_sober(sh)

print(f"Days sober from cigarettes: {sober_days[0]}")
print(f"Days sober from other substances: {sober_days[1]}")
