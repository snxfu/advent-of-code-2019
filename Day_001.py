arr = [
    142156, 108763, 77236, 78186, 110145, 126414, 115436, 133275, 132634, 82606, 118669, 90307, 134124, 102597, 128607,
    109214, 50160, 72539, 99033, 145334, 135409, 97525, 109865, 142319, 79027, 96924, 72530, 85993, 109594, 115991,
    107998, 112934, 85198, 112744, 129637, 95515, 90804, 107052, 89707, 93658, 60115, 118752, 94315, 59645, 115668,
    139320, 70734, 56771, 74741, 69284, 92228, 145376, 103317, 55143, 58370, 54873, 52424, 95392, 67892, 90858, 74693,
    77363, 51496, 79375, 71206, 103492, 94065, 72084, 144311, 67381, 129958, 86741, 148906, 123383, 147575, 136327,
    118108, 136529, 66356, 70746, 147569, 107267, 122434, 69688, 122127, 94072, 110203, 50546, 57836, 139334, 113240,
    96729, 68516, 74635, 126951, 138948, 88312, 101477, 129730, 93816
]


def get_fuel():
    sum_fuel = 0
    sum_combined = 0
    for i in arr:
        j = round(i // 3) - 2
        sum_combined += module_fuel(j)
        sum_fuel += j
    return sum_fuel, sum_combined


def module_fuel(val):   # used for part two
    sum_fuel = val
    while val > 0:
        v = round(val // 3) - 2
        if v > 0:
            sum_fuel += v
        val = v
    return sum_fuel


s = get_fuel()
print(s)