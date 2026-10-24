# Data dictionary and analysis method

## Sources

- source-jun-jul-2024.xlsx: original uploaded June–July export, Creative Reporting sheet. Campaign-level rows 2 and 61. Currency BDT, confirmed by the owner.
- source-aug-sep-2024.xlsx: original uploaded August–September workbook, Raw Data Report sheet, campaign-level rows 4, 6, 8 and 10. Formatted Report contains the same campaigns. Currency USD, confirmed by the owner.
- Six uploaded creative PNGs: renamed descriptively without changing image content. Exact ad IDs and carousel card order are not established by the images alone.
- Owner's written account: campaign responsibility, retrospective targeting decisions, August–October sales quantities, prices, recurring customers, and historical conversion convention of BDT 120 per USD.

## Campaign summary fields

| Field | Definition |
| --- | --- |
| period_start / period_end | Export reporting window, not necessarily campaign launch/end dates |
| campaign | Original campaign label, shortened only for Promoting ClypChip by removing the date prefix |
| currency / spend | Source-labelled account currency and campaign spend |
| result_type / results | Source result definition and count; likes and conversations remain separate |
| impressions | Campaign-level impressions, additive across the selected non-overlapping records |
| link_clicks | Source link clicks, distinct from all clicks |

## Product economics fields

Purchase and selling prices are owner-reported BDT per unit. Quantities cover August–October 2024. The mouse quantity is approximate. Delivered-versus-ordered status, discounts, cancellations and returns have not been independently checked. Price spread is selling price minus purchase price, before all other costs. It is not net profit.

## Calculation rules

- Cost per result = matching spend / matching result count. Group by currency, period and result definition. A zero result count means unavailable cost per result.
- Link CTR = link clicks / impressions × 100. Do not substitute all-click CTR.
- Historical comparison conversion: BDT amount / 120 = approximate USD equivalent, using the owner's supplied historical rate rather than a verified transaction rate. Original currencies remain intact.
- June–July spend: 4,871.11 / 120 = approximately USD 40.59. Combined June–September recorded spend is approximately USD 64.57 after adding USD 23.98. This is not a complete through-October advertising bill.
- Do not add campaign, ad-set, ad, demographic and month subtotal rows together. Do not add both representations of the August–September workbook.
- Do not sum reach as unique reach across campaigns; audiences can overlap. Conversations and new-contact counts are not verified unique buyers across campaigns.
- Attribution windows describe platform reporting, not a guarantee of causal impact. June–July export states 7-day click or 1-day view; retain each export's settings for further work.
- Sales are owner-reported across August–October, with recurring customers. Ad reports end September. No matched order attribution or complete October spend is available, so do not calculate verified ROAS, CPA or purchase conversion rate.
- Missing purchase/revenue fields are unavailable data, not evidence of zero sales.

## Validation

Campaign summary values were compared against campaign-level rows in both workbooks. All six images were visually reviewed. The analysis script is checked against the documented spend, result totals and per-unit price spreads. No exact interest selections, historical targets, optimisation uplift or customer count are invented.
