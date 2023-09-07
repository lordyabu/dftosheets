# dftosheets
Connect pandas DF to google sheets with conditional formatting

## Installation
```python
git clone https://github.com/lordyabu/dftosheets.git
cd dftosheets
```

## Requirements

- Python 3.9 or greater
- pandas
- gspread_formatting
- oauth2client
- Google Spreadsheets Service account: https://docs.gspread.org/en/latest/oauth2.html#service-account

# How to use

## 1. upload files
put csv files you would like to use in ./files. It works for both single/multiple files
 
## 2. configure
set sheet_name to your sheet name, and add any rules you want. for more info on how to make rules go to:  https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#ConditionalFormatRule
```python
  sheet_name = "test1.0"
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

        //  ADD YOUR RULES HERE

        }
```


## 3. Run 
go to main.py and set 1 rule code for each column. If columns are [DateTime, Price], len(rule_codes) == 2 Then either run single/multiple sheets
```python
  rules_codes = ['z', '1']

  create_single_sheet(rules_codes=rules_codes, csv='./files/PriceDay.csv', delete_current=True, grid_range='1:400')
  create_multiple_sheets(rules_codes=rules_codes, directory_path='./files/example_multiple', delete_current=True, grid_range='1:400')
```

# 4. Results
if you run the example data on multiple sheets the sheet should look like this
![Screenshot (39)](https://github.com/lordyabu/dftosheets/assets/92772420/225075a2-2069-40d1-b5c9-55e1b74d6d13)
