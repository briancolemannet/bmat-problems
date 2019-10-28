from typing import List, Dict


def calculate_stats(vals: str) -> Dict:
    if not vals:
        return None

    val_list = vals.split()

    if len(val_list) == 0:
        return None

    num_vals = []

    for v in val_list:
        num_vals.append(float(v))

    result = {
        'Mean': get_mean(num_vals),
        'Min': get_min(num_vals),
        'Max': get_max(num_vals),
        'Median': get_median(num_vals),
        'Sum': get_sum(num_vals),
        'StandardDeviation': get_standard_deviation(num_vals),
    }
    
    for k in result:
        print(f'{k}: {result[k]}')

    return result


def get_mean(vals: List[float]) -> float:
    sum = get_sum(vals)
    return sum/len(vals)


def get_min(vals: List[float]) -> float:
    min = vals[0]

    for x in vals:
        if x < min:
            min = x
    return min


def get_max(vals: List[float]) -> float:
    max = vals[0]

    for x in vals:
        if x > max:
            max = x
    return max


def get_median(vals: List[float]) -> float:
    vals.sort()
    len_vals = len(vals)
    median_index = int(len_vals/2)
    
    if (len_vals % 2) == 0:
        val1 = vals[median_index - 1]
        val2 = vals[median_index]
        return get_mean([val1, val2])

    return vals[median_index]


def get_sum(vals: List[float]) -> float:
    sum = 0
    for x in vals:
        sum += x
    return sum


def get_standard_deviation(vals: List[float]) -> float:
    pass
