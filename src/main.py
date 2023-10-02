import argparse
from gsheet import create_single_sheet, create_multiple_sheets


'''
YOUR CODE HERE
'''
def main_manual():

    # Conditional Formatting rules specified in config.py

    rule_codes = ['1', '1']

    # Either create single sheet or multiple

    create_single_sheet(rules_codes=rule_codes, csv='./files/PriceDay.csv', delete_current=True, grid_range='1:400')
    # create_multiple_sheets(rules_codes=rules_codes, directory_path='./files/example_multiple', delete_current=True, grid_range='1:400')

def main(args):
    if args.single_sheet:
        create_single_sheet(rules_codes=args.rule_codes, csv=f'./files/{args.csv}', delete_current=args.delete_current, grid_range=args.grid_range)
    elif args.multiple_sheets:
        create_multiple_sheets(rules_codes=args.rule_codes, directory_path=f'./files/{args.directory}', delete_current=args.delete_current, grid_range=args.grid_range)
    else:
        print("Please specify whether to create a single sheet or multiple sheets.")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Command-line tool for creating Google Sheets")

    parser.add_argument('--rule-codes', nargs='+', required=True, help="List of rule codes. E.g., --rules-codes 1 1")
    parser.add_argument('--single-sheet', action='store_true', help="Flag to create a single sheet")
    parser.add_argument('--multiple-sheets', action='store_true', help="Flag to create multiple sheets")
    parser.add_argument('--csv', type=str, default='PriceDay',
                        help="Name of the CSV file for single sheet creation without the .csv extension")
    parser.add_argument('--directory', type=str, default='example_multiple',
                        help="Name of the directory for multiple sheet creation")
    parser.add_argument('--delete-current', action='store_true', default=True, help="Flag to delete current sheets")
    parser.add_argument('--grid-range', type=str, default='1:400', help="Grid range for the sheets")

    args = parser.parse_args()
    main(args)
