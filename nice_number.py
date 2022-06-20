import math


def nice_number(value):
    if value == 0:
        return 0
    sign = 2 * int(value > 0) - 1
    exponent = math.floor(math.log10(abs(value)))
    fraction = abs(value) / 10 ** exponent

    # nice_numbers = [1, 1.1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5,
    #                 7, 7.5, 8.5, 9, 9.5, 10]
    nice_numbers = [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10]

    for num in nice_numbers:
        if fraction <= num:
            nice_fraction = num
            break

    return sign * nice_fraction * 10**exponent


def ticks(axis_min, axis_max, base_tick, num_ticks):
    axis_start = axis_min
    axis_end = axis_max

    axis_width = axis_end - axis_start
    raw_tick = axis_width / (num_ticks - 1)
    if raw_tick == 0:
        raw_tick = 0.1
    sign = 2 * int(raw_tick > 0) - 1

    good = False
    while good is False:
        nice_tick = nice_number(raw_tick)
        new_axis_start = (base_tick
                          - math.ceil((base_tick - axis_start) / nice_tick)
                          * nice_tick)
        new_axis_end = new_axis_start + nice_tick * (num_ticks - 1)

        if sign * new_axis_end < sign * axis_end:
            raw_tick = 1.04 * raw_tick
        else:
            good = True

    ticks = new_axis_start, new_axis_end

    return ticks
