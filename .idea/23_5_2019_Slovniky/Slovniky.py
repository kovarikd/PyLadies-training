cisla = {
    'Maruska': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barvy = {
    'hruska': 'zelena',
    'jablko': 'cervena',
    'meloun': 'zelena',
    'svestka': 'modra',
    'redkvicka': 'cervena',
    'zelí': 'zelena',
    'mrkev': 'cervena',
}

barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'cerno-hnedo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])

