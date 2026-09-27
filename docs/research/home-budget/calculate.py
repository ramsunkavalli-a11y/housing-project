"""Reproduce the fictional home-budget example; standard-library Python only."""
import json,pathlib

def payment(principal, annual_rate, months=360):
 r=annual_rate/12
 return principal/months if not r else principal*r/(1-(1+r)**(-months))

scenarios={
 'lower':dict(rate=.06,tax_rate=.011,insurance=150,utilities=200,maintenance=250),
 'central':dict(rate=.065,tax_rate=.012,insurance=250,utilities=250,maintenance=350),
 'higher':dict(rate=.07,tax_rate=.014,insurance=400,utilities=350,maintenance=500)}
rows=[]
for price in [550000,650000,750000]:
 costs={}
 for name,s in scenarios.items():
  pi=payment(price*.8,s['rate']); tax=price*s['tax_rate']/12
  costs[name]=dict(principal_interest=pi,taxes=tax,insurance=s['insurance'],utilities=s['utilities'],maintenance=s['maintenance'],total=pi+tax+s['insurance']+s['utilities']+s['maintenance'])
 rows.append(dict(price=price,down_payment=price*.2,closing_moving_initial_costs=25000,retained_cash=25000,cash_required=price*.2+50000,costs=costs))
# Solve for the price where the monthly spending limit is reached in each scenario.
limits={}
for name,s in scenarios.items():
 factor=payment(.8,s['rate'])+s['tax_rate']/12
 limits[name]=(5000-s['insurance']-s['utilities']-s['maintenance'])/factor
out=dict(label='Entirely fictional teaching example; not market prices, quotes, or personal advice',monthly_limit=5000,total_cash=195000,down_payment_fraction=.2,months=360,hoa=0,mortgage_insurance=0,assumptions=scenarios,rows=rows,monthly_price_limits=limits,cash_price_limit=(195000-50000)/.2)
pathlib.Path(__file__).with_name('scenarios.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
# Independent balance recurrence validates amortization; zero-rate edge case.
assert abs(payment(120000,0,120)-1000)<1e-9
for rate in [.06,.065,.07]:
 bal=520000;pmt=payment(bal,rate)
 for _ in range(360):bal=bal*(1+rate/12)-pmt
 assert abs(bal)<.001
assert all(r['costs']['lower']['total']<r['costs']['central']['total']<r['costs']['higher']['total'] for r in rows)
assert out['cash_price_limit']==725000
print('Amortization, scenario ordering, and cash arithmetic checked.')
