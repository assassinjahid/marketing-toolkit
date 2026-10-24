"""Reproduce ClypChip reporting calculations. Python 3 standard library only."""
import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BDT_PER_USD = Decimal('120')  # Owner-supplied historical comparison rate.

def read_rows(name):
    with (ROOT / name).open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))

def analyse():
    groups = defaultdict(lambda: [Decimal(0), 0])
    converted_spend = Decimal(0)
    print('CAMPAIGNS (platform-reported results)')
    for row in read_rows('campaign-summary.csv'):
        spend, results = Decimal(row['spend']), int(row['results'])
        key = (row['period_start'], row['period_end'], row['currency'], row['result_type'])
        groups[key][0] += spend
        groups[key][1] += results
        cost = f'{spend / results:.4f}' if results else 'unavailable'
        print(f"{row['campaign']}: {row['currency']} {spend:.2f}; {results} {row['result_type']}; cost/result {cost}")
        converted_spend += spend / BDT_PER_USD if row['currency'] == 'BDT' else spend
    print('\nGROUP TOTALS (separate periods, currencies and result definitions)')
    for key, (spend, results) in groups.items():
        cost = f'{spend / results:.4f}' if results else 'unavailable'
        print(f'{key}: spend {spend:.2f}; results {results}; cost/result {cost}')
    print(f'\nIndicative recorded June–September spend: USD {converted_spend:.2f}, using BDT {BDT_PER_USD}/USD.')
    print('Not a complete through-October advertising bill or a verified billing exchange rate.')
    print('\nOWNER-REPORTED PRODUCT PRICES (BDT per unit)')
    for row in read_rows('product-economics.csv'):
        spread = Decimal(row['selling_price_bdt']) - Decimal(row['purchase_price_bdt'])
        print(f"{row['product']}: price spread {spread:.2f}; {row['quantity_qualifier']} units {row['units_reported']} ({row['sales_period']})")
    print('Price spread excludes all other costs. Sales are owner-reported, include recurring customers and span August–October.')
    print('Verified ROAS, purchase CPA, sales conversion rate and net profit: unavailable.')
    return groups

if __name__ == '__main__':
    analyse()
