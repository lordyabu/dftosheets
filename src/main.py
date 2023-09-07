from gsheet import create_single_sheet, create_multiple_sheets



def main():
    # YOUR CODE HERE

    # z is placeholder so no rules are applied to that column. Any char not used in config.rule_templates will
    # have same effect

    rules_codes = ['z', '1']

    # Either create single sheet or multiple

    # create_single_sheet(rules_codes=rules_codes, csv='./files/PriceDay.csv', delete_current=True, grid_range='1:400')
    # create_multiple_sheets(rules_codes=rules_codes, directory_path='./files/example_multiple', delete_current=True, grid_range='1:400')





if __name__ == '__main__':
    main()