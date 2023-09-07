from gspread_formatting import *
from config import rule_templates


def create_formatting(rules, sheet, grid_range='1:400'):
    rules_final = []
    letters = [chr(i) for i in range(65, 91)] + [chr(i) + chr(j) for i in range(65, 91) for j in range(65, 91)]
    for count, rule_x in enumerate(rules):
        if rule_x in rule_templates:
            for rule_detail in rule_templates[rule_x]:
                if rule_detail[0] == 'gradient':
                    rule = ConditionalFormatRule(
                        ranges=[GridRange.from_a1_range(f'{letters[count]}{grid_range}', sheet)],
                        gradientRule=rule_detail[1]
                    )
                elif rule_detail[0] == 'boolean':
                    condition_type, condition_value, color = rule_detail[1:]
                    rule = ConditionalFormatRule(
                        ranges=[GridRange.from_a1_range(f'{letters[count]}{grid_range}', sheet)],
                        booleanRule=BooleanRule(
                            condition=BooleanCondition(condition_type, [condition_value]),
                            format=CellFormat(backgroundColor=color)
                        )
                    )
                rules_final.append(rule)

    return rules_final
