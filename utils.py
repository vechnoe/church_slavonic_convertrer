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

    ('”', '\u00a0\u00b7'),  # NO-BREAK SPACE + MIDDLE DOT
    (',', '\u00a0\u002c'),  # COMMA + NO-BREAK SPACE
    ('.', '\u00a0\u002e'),  # FULL STOP, PERIOD + NO-BREAK SPACE
    ('~', '\u0483'),  # COMBINING CYRILLIC TITLO
    ('v', '\u2de1'),  # COMBINING CYRILLIC LETTER VE
    ("'", '\u0301'),  # COMBINING ACUTE ACCENT
    ('@', '\u0301'),  # COMBINING ACUTE ACCENT
    ('`', '\u0300'),  # COMBINING GRAVE ACCENT
    ('è', '\u0300'),  # COMBINING GRAVE ACCENT
    # CYRILLIC SMALL LETTER BE + COMBINING INVERTED BREVE:
    ('б^', '\u0431\u0311'),
    # CYRILLIC SMALL LETTER ТE + COMBINING INVERTED BREVE:
    ('т^', '\u0442\u0311'),
    # CYRILLIC SMALL LETTER ES + COMBINING INVERTED BREVE:
    ('с^', '\u0441\u0311'),
    ('^', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA
    ('$', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA
    ('њ', '\u0463'),  # CYRILLIC SMALL LETTER YAT
    ('ё', '\u0479'),  # CYRILLIC SMALL LETTER UK
    ('ђ', '\uA64B'),  # CYRILLIC SMALL LETTER MONOGRAPH UK
    ('#', '\u033E'),  # COMBINING VERTICAL TILDE
    ('c', '\ua67d'),  # COMBINING CYRILLIC PAYEROK
    ('ја', '\ua657'),  # CYRILLIC SMALL LETTER IOTIFIED A
    ('ЈА', '\ua656'),  # CYRILLIC CAPITAL LETTER IOTIFIED A
    ('ё', '\u0479'),  # CYRILLIC SMALL LETTER UK
    ('%', '\u0486\u0301'),  # ISO
    ('/', '\u0486\u0301'),  # ISO
    ('я', '\u0467'),  # CYRILLIC SMALL LETTER LITTLE YUS
    ('D', '\u2de3'),  # COMBINING CYRILLIC LETTER DE
    # Ligature: COMBINING CYRILLIC LETTER DE + COMBINING CYRILLIC LETTER I
    ('d', '\u2de3\u200d\ua675'),
    ('s', '\u2df5'),  # COMBINING CYRILLIC LETTER ES-TE
    # CYRILLIC SMALL LETTER ROUND OMEGA + COMBINING CYRILLIC PSILI PNEUMATA:
    ('ѓ҆', '\u047b\u0486'),
    ('ѓ', '\u047b'),  # CYRILLIC SMALL LETTER ROUND OMEGA
    ('M', '\u2de8'),  # COMBINING CYRILLIC LETTER EM
    ('X', '\u2def'),  # COMBINING CYRILLIC LETTER HA
    ('&', '\u0486\u0300'),  # Apostrophe
    ('T', '\u2dee'),  # COMBINING CYRILLIC LETTER TE
    # Ligature: COMBINING CYRILLIC LETTER CHE + COMBINING CYRILLIC POKRYTIE
    ('q', '\u2df1\u200d\u0487'),
    ('э', '\u0461'),  # CYRILLIC SMALL LETTER OMEGA
    ('n', '\u2de9'),  # COMBINING CYRILLIC LETTER EN
    ('џ', '\u0473'),  # CYRILLIC SMALL LETTER FITA
    ('ћ', '\u046f'),  # CYRILLIC SMALL LETTER KSI
    ('љ', '\u0475'),  # CYRILLIC SMALL LETTER IZHITSA
    ('=', '\u030f'),  # DOUBLE GRAVE ACCENT
    # Ligature: COMBINING CYRILLIC LETTER EL + COMBINING CYRILLIC POKRYTIE
    ('l', '\u2de7\u200d\u0487'),
    ('L', '\u2de7'),  # COMBINING CYRILLIC LETTER EL
    ('H', '\u2de2'),  # COMBINING CYRILLIC LETTER GHE
    # Ligature: COMBINING CYRILLIC LETTER GHE + COMBINING CYRILLIC POKRYTIE
    ('h', '\u2de2\u200d\u0487'),
    ('y', '\u2de4'),  # COMBINING CYRILLIC LETTER ZHE
    ('C', '\u2df0'),  # COMBINING CYRILLIC LETTER TSE



)


def convert(in_string):
    converted = in_string
    for symbol_in, symbol_out in CONVERTABLE:
        converted = converted.replace(symbol_in, symbol_out)

    return converted



