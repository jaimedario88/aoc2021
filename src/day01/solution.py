import os


def quantity_larger_measurements(measurements: list[int]) -> int:

    ret = 0

    for index, measurement in enumerate(measurements):
        if index == 0:
            pass
        else:
            current = measurement
            previous = measurements[index - 1]

            difference = current - previous

            if difference > 0:
                ret += 1

    return ret


def quantity_sliding_window_larger_measurements(measurements: list[int]) -> int:
    window_sums: list[int] = []
    for index, _ in enumerate(measurements):
        window_sum = sum(measurements[index : index + 3])
        window_sums.append(window_sum)
    return quantity_larger_measurements(window_sums)


if __name__ == "__main__":

    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
    rel_path = "input.dat"
    abs_file_path = os.path.join(script_dir, rel_path)

    values_list = []
    with open(abs_file_path, encoding="utf-8") as input_file:
        for line in input_file:
            stripped_line = int(line.strip())
            values_list.append(stripped_line)
        result_1 = quantity_larger_measurements(values_list)
        print("Result 1", result_1)
        result_2 = quantity_sliding_window_larger_measurements(values_list)
        print("Result 2", result_2)
