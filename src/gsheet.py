import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *
from helper_functions import delete_days, read_file
from config import sheet_name
import os
from conditional_formatting import create_formatting

#
def create_single_sheet(rules_codes, csv, delete_current, grid_range):
    if delete_current:
        delete_days()

    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        './clientsecret/client_secret.json', scope)
    client = gspread.authorize(creds)

    df = read_file(csv)

    sheet = client.open(sheet_name).get_worksheet(0)

    sheet.update([df.columns.values.tolist()] + df.values.tolist())
    rules = get_conditional_format_rules(sheet)
    new_rules = create_formatting(rules_codes, sheet, grid_range)

    for r in new_rules:
        rules.append(r)

    rules.save()


def create_multiple_sheets(rules_codes, directory_path, delete_current, grid_range):
    if delete_current:
        delete_days()

    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        './clientsecret/client_secret.json', scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open(sheet_name)

    for csv in os.listdir(directory_path):
        if csv.endswith('.csv'):  # Assuming you are reading CSV files
            file_path = os.path.join(directory_path, csv)
            df = read_file(file_path)

            worksheet_title = os.path.splitext(csv)[0]  # Using the file name as the worksheet title
            sheet = spreadsheet.add_worksheet(title=worksheet_title, rows=str(df.shape[0]), cols=str(df.shape[1]))

            sheet.update([df.columns.values.tolist()] + df.values.tolist())

            rules = get_conditional_format_rules(sheet)
            new_rules = create_formatting(rules_codes, sheet, grid_range)

            for r in new_rules:
                rules.append(r)

            rules.save()

            # Prevent API rate limit
            time.sleep(2)


