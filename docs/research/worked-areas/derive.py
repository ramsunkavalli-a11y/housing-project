"""Recompute the research measures from included public ACS extracts. Python 3, no dependencies."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARES = [
    ('detached', 'Detached homes', 'B25024', [2]),
    ('attached', 'Attached single-unit homes', 'B25024', [3]),
    ('two_to_four', 'Units in 2–4-unit buildings', 'B25024', [4, 5]),
    ('five_plus', 'Units in buildings with 5+ units', 'B25024', [6, 7, 8, 9]),
    ('zero_one_bed', 'Zero or one bedroom', 'B25041', [2, 3]),
    ('two_bed', 'Two bedrooms', 'B25041', [4]),
    ('three_bed', 'Three bedrooms', 'B25041', [5]),
    ('four_plus_bed', 'Four or more bedrooms', 'B25041', [6, 7]),
    ('three_plus_bed', 'Three or more bedrooms', 'B25041', [5, 6, 7]),
    ('pre1940', 'Built before 1940', 'B25034', [11]),
    ('built1940_1969', 'Built 1940–1969', 'B25034', [8, 9, 10]),
    ('built1970_1999', 'Built 1970–1999', 'B25034', [5, 6, 7]),
    ('built2000_plus', 'Built 2000 or later', 'B25034', [2, 3, 4]),
    ('owner_occupied', 'Owner-occupied share of occupied homes', 'B25003', [2]),
    ('vacant', 'Vacant share of housing units', 'B25002', [3]),
    ('fixed_broadband_subscription', 'Households subscribing to cable/fiber/DSL', 'B28002', [7]),
    ('cellular_only', 'Households with cellular-only subscriptions', 'B28002', [6]),
]

def usable(raw):
    """This sample contains nonnegative numbers and one missing-MOE sentinel."""
    try:
        value = float(raw)
        return value if value >= 0 else None
    except (ValueError, TypeError):
        return None

def proportion(row, table, columns):
    e = lambda n: usable(row[f'{table}_E{n:03d}'])
    m = lambda n: usable(row[f'{table}_M{n:03d}'])
    inputs = [e(n) for n in columns] + [e(1)]
    if None in inputs or e(1) == 0:
        return {'estimate': None, 'moe90_pp': None, 'status': 'insufficient_evidence'}
    numerator, denominator = sum(e(n) for n in columns), e(1)
    p = numerator / denominator
    assert 0 <= p <= 1
    margins = [m(n) for n in columns] + [m(1)]
    moe, method = None, 'missing_input_moe'
    if None not in margins:
        numerator_variance = sum(m(n) ** 2 for n in columns)
        radicand = numerator_variance - p ** 2 * m(1) ** 2
        method = 'subset_proportion_approximation'
        if radicand < 0:
            radicand = numerator_variance + p ** 2 * m(1) ** 2
            method = 'ratio_fallback_approximation'
        moe = 100 * math.sqrt(radicand) / denominator
    return dict(estimate=100*p, moe90_pp=moe, numerator=numerator,
                denominator=denominator, method=method, unit='percent',
                numerator_columns=[f'{table}_E{n:03d}' for n in columns],
                denominator_column=f'{table}_E001',
                interval90_clipped=[max(0,100*p-moe), min(100,100*p+moe)] if moe is not None else None)

def derive():
    data = json.loads((ROOT/'acs-extract.json').read_text(encoding='utf-8'))
    output = {'method_version': 'worked-example-1', 'period': data['period'], 'areas': {}}
    geoids = list(data['tables']['B25024']['rows'])
    for geoid in geoids:
        measures = {}
        for key,label,table,cols in SHARES:
            measures[key] = dict(label=label, table=table,
                **proportion(data['tables'][table]['rows'][geoid],table,cols))
        for key,label,table,col in [
            ('value','Median owner-reported home value','B25077',1),
            ('rent','Median gross monthly rent','B25064',1),
            ('owner_cost_mortgage','Median monthly owner costs, with mortgage','B25088',2),
            ('owner_cost_no_mortgage','Median monthly owner costs, no mortgage','B25088',3),
        ]:
            row = data['tables'][table]['rows'][geoid]
            raw_e,raw_m = row[f'{table}_E{col:03d}'],row[f'{table}_M{col:03d}']
            measures[key]=dict(label=label,table=table,column=col,estimate=usable(raw_e),
                moe90_dollars=usable(raw_m),raw_estimate=raw_e,raw_moe=raw_m,
                unit='2024_USD',status='median_open_interval' if raw_m=='-333333333' else 'published_estimate')
        output['areas'][geoid]=measures
    (ROOT/'derived-measures.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return output

if __name__ == '__main__':
    result = derive()
    for geoid, measures in result['areas'].items():
        print(geoid)
        for key in ('detached','three_plus_bed','pre1940','fixed_broadband_subscription'):
            d=measures[key]
            print(f"  {key}: {d['estimate']:.1f}% +/- {d['moe90_pp']:.1f} percentage points")
