# config.py
from gspread_formatting import *


# Paste your client_secret.json file into clientsecret folder


# Sheet name to copy to // make sure to share with your service account
sheet_name = "test1.0"



# Rules for formatting. Add your own rules here. Here are some example rules

# Rule 0 is a boolean rule wher if a value if 0, it is set to red=100,green=0,blue=0,
# if a value is 1, it is set to red=0,green=100,blue=0


# Rule 1 us a gradient rule which sets a black -> white gradient based off of MAX, PERCENTILE=50, and MIN

# For more understanding about how to make rules go to
# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#ConditionalFormatRule

rule_templates = {
        "0": [
            ('boolean', 'NUMBER_EQ', '0', Color(100, 0, 0)),
            ('boolean', 'NUMBER_EQ', '1', Color(0, 100, 0))
        ],
        "1": [
            ('gradient',
             GradientRule(
                maxpoint=InterpolationPoint(color=Color(1, 1, 1), type='MAX'),
                midpoint=InterpolationPoint(color=Color(75, 75, 75), type='PERCENTILE', value="50"),
                minpoint=InterpolationPoint(color=Color(200, 200, 200), type='MIN')
             ))
        ]
        ## ADD YOUR RULES HERE

        }