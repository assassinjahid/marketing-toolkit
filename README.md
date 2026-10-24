# Marketing Toolkit

Practical campaign reporting resources and a documented ClypChip case study by **Md Jahid Hasan**, digital marketer and mentor.

This collection combines historical campaign exports and original ad compositions with newly prepared reusable reporting resources. Sales recollections, platform results and derived calculations are labelled separately.

## Start here

| Resource | What it contains |
| --- | --- |
| [ClypChip case study](CLYPCHIP-CASE-STUDY.md) | Business context, audience decisions, results, product economics and six creative examples |
| [Campaign summary](campaign-summary.csv) | Six campaign-level records extracted from the two source reports |
| [Product economics](product-economics.csv) | Owner-reported prices and units, with period and approximation labels |
| [Reporting template](report-template.csv) | Blank CSV with the same reporting structure |
| [Campaign brief](CAMPAIGN-BRIEF.md) | Reusable planning and review prompts |
| [Data dictionary and method](DATA-DICTIONARY.md) | Definitions, source mapping, currency treatment and interpretation limits |
| [Analysis script](analyse.py) | Standard-library Python script that reproduces the main calculations |

## Reproduce the analysis

Download or clone this repository, open its folder in a terminal and run:

```sh
python3 analyse.py
```

Python 3 is the only requirement. The script reads the supplied CSV files and prints campaign costs, grouped results, currency conversion and per-unit price spreads. It does not connect to an ad account or require credentials.

For a new report, copy the headers from report-template.csv into campaign-summary.csv and supply your own campaign-level records. Supported currencies are BDT and USD. Review the historical conversion rate before reusing the script for another period. The script rejects unsupported currencies, duplicate campaign keys and several invalid input types; it cannot determine whether your source selection or attribution is correct.

## Evidence at a glance

- June–July 2024: BDT 4,871.11 spent; 965 Facebook likes attributed across two campaigns.
- August–September 2024: USD 16.54 spent on three messaging campaigns; 354 messaging conversations started, approximately USD 0.0467 per conversation.
- August–October 2024: owner-reported product sales, including approximately 70 mice. This longer period includes recurring customers and does not provide campaign-level purchase attribution.

The case study includes the source workbooks and reviewed creative examples. It makes no verified ROAS, net-profit or targeting-uplift claim.

## Use and authorship

Jahid confirms ownership of ClypChip and responsibility for its campaigns and creative work. Product trademarks and underlying product imagery belong to their respective rights holders. No open-source or commercial reuse licence is granted for the brand assets. The CSV template and planning prompts were prepared for this portfolio and can be adapted for personal learning with attribution.

The Python implementation and reporting resources were prepared for this retrospective portfolio. Their presence does not imply that Python was used to manage the original campaigns.

[Profile](https://github.com/assassinjahid) · [Teaching portfolio](https://github.com/assassinjahid/digital-marketing-teaching) · [Project overviews](https://github.com/assassinjahid/digital-marketing-case-studies) · [LinkedIn](https://www.linkedin.com/in/jahid-akash/)
