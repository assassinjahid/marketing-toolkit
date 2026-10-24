"""Reproduce ClypChip reporting calculations. Python 3 standard library only."""
import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BDT_PER_USD = Decimal('120')  # Owner-supplied historical comparison rate.

def read_rows(name):
    with (ROOT / name).open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))

def nonnegative_number(value, field):
    number = Decimal(value)
    if not number.is_finite() or number < 0:
        raise ValueError(f'{field} must be a finite, non-negative number.')
    return number

def validate_campaigns(rows):
    if not rows:
        raise ValueError('Campaign input has no data rows; a blank template is not a zero-spend report.')
    seen = set()
    required = {'period_start', 'period_end', 'campaign', 'currency', 'spend',
                'result_type', 'results', 'impressions', 'link_clicks'}
    for row in rows:
        if not required.issubset(row) or any(not row[k] for k in required):
            raise ValueError('Campaign input contains missing fields or blank required values.')
        if row['currency'] not in {'BDT', 'USD'}:
            raise ValueError('Supported currencies are BDT and USD. No other currency is converted implicitly.')
        if date.fromisoformat(row['period_start']) > date.fromisoformat(row['period_end']):
            raise ValueError('Campaign reporting start must not follow its end.')
        nonnegative_number(row['spend'], 'spend')
        for field in ('results', 'impressions', 'link_clicks'):
            value = nonnegative_number(row[field], field)
            if value != value.to_integral_value():
                raise ValueError(f'{field} must be a whole-number count.')
        key = tuple(row[k] for k in ('period_start', 'period_end', 'campaign', 'currency', 'result_type'))
        if key in seen:
            raise ValueError('Duplicate campaign record: review the reporting level before summing.')
        seen.add(key)

def analyse():
    campaigns = read_rows('campaign-summary.csv')
    validate_campaigns(campaigns)
    products = read_rows('product-economics.csv')
    for row in products:
        for field in ('purchase_price_bdt', 'selling_price_bdt', 'units_reported'):
            nonnegative_number(row[field], field)
    groups = defaultdict(lambda: [Decimal(0), 0])
    converted_spend = Decimal(0)
    print('CAMPAIGNS (platform-reported results)')
    for row in campaigns:
        spend, results = Decimal(row['spend']), int(Decimal(row['results']))
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
    print(f'\nIndicative recorded spend for supplied reporting windows: USD {converted_spend:.2f}, using BDT {BDT_PER_USD}/USD.')
    print('Not a complete through-October advertising bill or a verified billing exchange rate.')
    print('\nOWNER-REPORTED PRODUCT PRICES (BDT per unit)')
    for row in products:
        spread = Decimal(row['selling_price_bdt']) - Decimal(row['purchase_price_bdt'])
        print(f"{row['product']}: price spread {spread:.2f}; {row['quantity_qualifier']} units {row['units_reported']} ({row['sales_period']})")
    print('Price spread excludes all other costs. Sales are owner-reported, include recurring customers and span August–October.')
    print('Verified ROAS, purchase CPA, sales conversion rate and net profit: unavailable.')
    return groups

if __name__ == '__main__':
    analyse()
