import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import sheet_name
import pandas as pd

# Deletes the current data on sheet. Doesn't delete the actual sheet
def delete_days():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'src/clientsecret/client_secret.json', scope)

    client = gspread.authorize(creds)

    sh = client.open('{}'.format(sheet_name))

    worksheets = sh.worksheets()
    reqs = [{"addSheet": {"properties": {"index": 0}}}] + [{"deleteSheet": {"sheetId": s.id}} for s in worksheets]
    sh.batch_update({"requests": reqs})



# Reads file. Accounts for files with/without leading comma
def read_file(filename):
    # First, read just the first row to check the columns
    first_row = pd.read_csv(filename, nrows=0)
    cols = first_row.columns

    # If the first column is unnamed, adjust the columns to use
    if 'Unnamed: 0' in cols[0]:
        usecols = cols[1:]
    else:
        usecols = cols

    # Read the file with the appropriate columns
    df = pd.read_csv(filename, usecols=usecols)

    return df


