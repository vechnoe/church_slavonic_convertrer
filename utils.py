UNUSED = (
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
)




CONVERTABLE = (
    # in, out
    ('”', '\u00a0\u00b7'),  # NO-BREAK SPACE + MIDDLE DOT
    (',', '\u00a0\u002c'),  # COMMA + NO-BREAK SPACE
    ('.', '\u00a0\u002e'),  # FULL STOP, PERIOD + NO-BREAK SPACE
    ('~', '\u0483'),  # COMBINING CYRILLIC TITLO
    ('v', '\u2de1'),  # COMBINING CYRILLIC LETTER VE
    ("'", '\u0301'),  # COMBINING ACUTE ACCENT
    ('@', '\u0301'),  # COMBINING ACUTE ACCENT
    ('`', '\u0300'),  # COMBINING GRAVE ACCENT
    ('è', '\u0300'),  # COMBINING GRAVE ACCENT

    # CYRILLIC SMALL LETTER BE + COMBINING CYRILLIC PALATALIZATION:
    ('б>', '\u0431\u0484'),
    # CYRILLIC SMALL LETTER EL + COMBINING CYRILLIC PALATALIZATION:
    ('л>', '\u043b\u0484'),
    # CYRILLIC SMALL LETTER ТE + COMBINING CYRILLIC PALATALIZATION:
    ('т>', '\u0442\u0484'),
    # CYRILLIC SMALL LETTER ES + COMBINING CYRILLIC PALATALIZATION:
    ('с>', '\u0441\u0484'),
    # CYRILLIC SMALL LETTER VE + COMBINING CYRILLIC PALATALIZATION:
    ('в>', '\u0443\u0484'),

    ('>', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA

    ('$', '\u0486'),  # COMBINING CYRILLIC PSILI PNEUMATA
    ('њ', '\u0463'),  # CYRILLIC SMALL LETTER YAT
    # CYRILLIC SMALL LETTER IOTIFIED A +  COMBINING CYRILLIC PSILI PNEUMATA
    ('ја^', '\ua657\u0486'),
    # CYRILLIC SMALL LETTER UK + COMBINING CYRILLIC PSILI PNEUMATA
    ('ё^', '\u0479\u0486'),
    # CYRILLIC SMALL LETTER ROUND OMEGA + COMBINING CYRILLIC PSILI PNEUMATA:
    ('ѓ^', '\u047b\u0486'),
    ('ё', '\u0479'),  # CYRILLIC SMALL LETTER UK
    ('ђ', '\uA64B'),  # CYRILLIC SMALL LETTER MONOGRAPH UK
    ('^', '\u0311'),  # COMBINING INVERTED BREVE (KAMORA)
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
    # Ligature: COMBINING CYRILLIC LETTER EN + COMBINING CYRILLIC POKRYTIE
    ('n', '\u2de9\u200d\u0487'),
    ('џ', '\u0473'),  # CYRILLIC SMALL LETTER FITA
    ('ћ', '\u046f'),  # CYRILLIC SMALL LETTER KSI
    ('љ', '\u0475'),  # CYRILLIC SMALL LETTER IZHITSA
    ('=', '\u030f'),  # DOUBLE GRAVE ACCENT
    # Ligature: COMBINING CYRILLIC LETTER EL + COMBINING CYRILLIC POKRYTIE
    ('l', '\u2de7\u200d\u0487'),
    ('L', '\u2de7'),  # COMBINING CYRILLIC LETTER EL
    ('H', '\u2de2'),  # COMBINING CYRILLIC LETTER GHE
    # Ligature: COMBINING CYRILLIC LETTER GHEc
    ('h', '\u2de2\u200d\u0487'),
    ('Q', '\u2de4'),  # COMBINING CYRILLIC LETTER ZHE
    # Ligature: COMBINING CYRILLIC LETTER ZHE + COMBINING CYRILLIC LETTER IE
    ('y', '\u2de4\u200d\u2df7'),
    # Ligature: COMBINING CYRILLIC LETTER TSE + COMBINING CYRILLIC POKRYTIE
    ('w', '\u2df0\u200d\u0487'),
    ('C', '\u2df0'),  # COMBINING CYRILLIC LETTER TSE
    ('Эt', '\u047e'),  # CYRILLIC CAPITAL LETTER OT: deprecated
    ('Э', '\u0460'),  # CYRILLIC CAPITAL LETTER OMEGA
    # Ligature: COMBINING CYRILLIC LETTER O + COMBINING CYRILLIC POKRYTIE
    ('o', '\u2dea\u200d\u0487'),
    ('O', '\u047c'),  # CYRILLIC CAPITAL LETTER OMEGA WITH TITLO: deprecated
    # Ligature: COMBINING CYRILLIC LETTER ER + COMBINING CYRILLIC POKRYTIE
    ('r', '\u2dec\u200d\u0487'),
    # Ligature: COMBINING CYRILLIC LETTER SHCHA + COMBINING CYRILLIC POKRYTIE
    ('u', '\u2df3\u200d\u0487'),
    # Ligature: COMBINING CYRILLIC LETTER PE + COMBINING CYRILLIC POKRYTIE
    ('p', '\u2deb\u200d\u0487'),
    # Ligature: COMBINING CYRILLIC LETTER EF + COMBINING CYRILLIC POKRYTIE
    ('f', '\ua69e\u200d\u0487'),
    # Ligature: COMBINING CYRILLIC LETTER KA + COMBINING CYRILLIC POKRYTIE
    ('k', '\u2de6\u200d\u0487'),
    ('"', '\u0306'),  # COMBINING BREVE
    # Ligature: COMBINING CYRILLIC LETTER FITA + COMBINING CYRILLIC POKRYTIE
    ('g', '\u2df4\u200d\u0487'),
    ('Z', '\u2de5'),  # COMBINING CYRILLIC LETTER ZE
    # Ligature: COMBINING CYRILLIC LETTER BE + COMBINING CYRILLIC POKRYTIE
    ('b', '\u2de0\u200d\u0487'),






)

def replace_on_position(string, inchar, outchar) -> str:
    """
    >>> replace_on_position('h^o^la', '^', '&')
    'h&o^la'
    >>> replace_on_position('ho^la', '^', '&')
    'ho^la'
    >>> replace_on_position(' ', '^', '&')
    ' '
    >>> replace_on_position('h^', '^', '&')
    'h&'
    """
    if not len(string) >= 2:
        return string

    if string[1] != inchar:
        return string

    lpart = string[:1]
    rpart = string[2:]

    return "".join([lpart, outchar, rpart])


def convert(in_string) -> str:

    for symbol_in, symbol_out in UNUSED:
        in_string = in_string.replace(symbol_in, symbol_out)

    out = []
    for s in in_string.split():
        out.append(replace_on_position(s, '^', '>'))

    converted = " ".join(out)
    for symbol_in, symbol_out in CONVERTABLE:
        converted = converted.replace(symbol_in, symbol_out)

    return converted



