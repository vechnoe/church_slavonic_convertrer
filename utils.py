CONVERTABLE = (
    # in, out

    # remove unused symbols
    ('*', ''),
    ('(', ''),
    (')', ''),
    ('[', ''),
    (']', ''),
    ('-', ''),
    ('1', ''),
    ('2', ''),
    ('3', ''),
    ('4', ''),
    ('5', ''),
    ('6', ''),
    ('7', ''),
    ('8', ''),
    ('9', ''),
    ('0', ''),

    ('”', '.'),
    ('~', '\u0483'),  # COMBINING CYRILLIC TITLO
    ('v', '\u2DE1'),  # COMBINING CYRILLIC LETTER VE
    ("'", '\u0301'),  # COMBINING ACUTE ACCENT
    ('`', '\u0300'),  # COMBINING GRAVE ACCENT
    # CYRILLIC SMALL LETTER BE + COMBINING INVERTED BREVE:
    ('б^', '\u0431\u0311'),
    # CYRILLIC SMALL LETTER ТE + COMBINING INVERTED BREVE:
    ('т^', '\u0442\u0311'),
    ('^', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA
    ('$', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA
    ('њ', '\u0463'),  # CYRILLIC SMALL LETTER YAT
    ('ё', '\u0479'),  # CYRILLIC SMALL LETTER UK
    ('ђ', '\uA64B'),  # CYRILLIC SMALL LETTER MONOGRAPH UK
    ('#', '\u033E'),  # COMBINING VERTICAL TILDE
    ('c', '\ua67d'),  # COMBINING CYRILLIC PAYEROK
    ('ја', '\ua657'),  # CYRILLIC SMALL LETTER IOTIFIED A
    ('ё', '\u0479'),  # CYRILLIC SMALL LETTER UK
    ('%', '\u0486\u0301'),  # ISO
    ('/', '\u0486\u0301'),  # ISO
    ('я', '\u0467'),  # CYRILLIC SMALL LETTER LITTLE YUS
    ('D', '\u2de3'),  # COMBINING CYRILLIC LETTER DE
    ('s', '\u2df5'),  # COMBINING CYRILLIC LETTER ES-TE
    # CYRILLIC SMALL LETTER ROUND OMEGA + COMBINING CYRILLIC PSILI PNEUMATA:
    ('ѓ҆', '\u047b\u0486'),
    ('M', '\u2de8'),  # COMBINING CYRILLIC LETTER EM
    ('X', '\u2def'),  # COMBINING CYRILLIC LETTER HA
    ('&', '\u0486\u0300'),  # Apostrophe
    ('T', '\u2dee'),  # COMBINING CYRILLIC LETTER TE
    ('q', '\u2df1'),  # COMBINING CYRILLIC LETTER CHE
    ('э', '\u0461'),  # CYRILLIC SMALL LETTER OMEGA
    ('n', '\u2de9')  # COMBINING CYRILLIC LETTER EN


)


def convert(in_string):
    converted = in_string
    for symbol_in, symbol_out in CONVERTABLE:
        converted = converted.replace(symbol_in, symbol_out)

    return converted



