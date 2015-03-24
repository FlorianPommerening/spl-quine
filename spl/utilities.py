ROMAN_LITERALS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def scene_number(n):
    if not isinstance(n, int):
        raise TypeError("Can only convert integers to scene numbers")
    if not 0 < n < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    result = ""
    for value, literal in ROMAN_LITERALS:
        count = int(n / value)
        result += literal * count
        n -= value * count
    return result
