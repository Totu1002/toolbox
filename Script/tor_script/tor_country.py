import pycountry
import pprint

#torrcにおけるExcludeNodesを生成するスクリプト

pp = pprint.PrettyPrinter(indent=4)

def concat_sets(countries):
  return ','.join(['{' + r.lower()+'}' for r in countries])

entry_countries = set({
  'JP',
})

include_countries = set({
  'JP',
  #'KR',
  #'HK',
  #'TW',
  #'SG',
  #'PH',
  #'US',
  #'AU',
})

exit_countries = set({
  'JP',
})

forbid_countries = set({
  ## 5-eyes
  #'US',
  #'GB',
  #'CA',
  #'AU',
  #'NZ',
  ## 9-eyes
  #'DK',
  #'FR',
  #'NL',
  #'NO',
  ## 14-eyes
  #'DE',
  #'BE',
  #'IT',
  #'ES',
  #'SE',
  ## 41-eyes
  #'AT',
  #'CZ',
  #'GR',
  #'HU',
  #'IS',
  #'JP',
  #'LU',
  #'PL',
  #'PT',
  #'KR',
  #'CH',
  #'TR',
  ## Dangerous (harmful exit) countries
  #'RU',
  #'UA',
  #'CN',
})

all_countries = set([c.alpha_2 for c in list(pycountry.countries)])

if len(forbid_countries) > 0:
  exclude_countries = forbid_countries
else:
  exclude_countries = all_countries - include_countries

exclude_nodes = concat_sets(exclude_countries)
entry_nodes = concat_sets(entry_countries)
exit_nodes = concat_sets(exit_countries)

print("StrictNodes 1")
print("ExcludeNodes SlowServer," + exclude_nodes)
if len(entry_nodes) > 0:
  print("EntryNodes " + entry_nodes)
if len(exit_nodes) > 0:
  print("ExitNodes " + exit_nodes)
