# read the file and count the number of increases

def day_one_part_one():
    with open('input_day1.txt', 'r') as file:
        input = []
        for line in file.readlines():
            input.append(int(line))
        return count_increase(input)

def day_one_part_two():
    with open('input_day1.txt', 'r') as file:
        input = file.readlines()
        return window(input)

def count_increase(data_feed):
    count = 0
    prev = data_feed[0]
    for line in data_feed:
        if line > prev:
            count += 1
        prev = line
    return count

# to reduce the noise in the data
def window(data):
    windows = []
    # look up to next 2 values and add them up
    for idx in range(len(data)):
        if idx < len(data) - 2:
            windows.append(data[idx] + data[idx + 1] + data[idx + 2])
    return count_increase(windows)

# clean execution of the code
if __name__ == "__main__":
    input = []
    with open('input_day1.txt', 'r') as file:
        input = []
        for line in file.readlines():
            input.append(int(line))

    # day 1 part 1
    print(count_increase(input))
    print(window(input))