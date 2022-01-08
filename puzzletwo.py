# initially given rules in part 1
def determine_position(commands):
    # position incorporates two components
    horizontal = 0
    depth = 0

    # loop through list of commands in input file
    for command in commands:
        # each command is a line formatted as: "<direction>(str) <unit>(int)"
        command = command.split(" ");
        direction = command[0]
        unit = int(command[1])

        # apply conditional rules based on problem statement
        if (direction == "forward"):
            horizontal += unit
        elif (direction == "up"):
            depth -= unit
        elif (direction == "down"):
            depth += unit

    # position is calculated based on a history provided though sequence of events in the input file
    # this implies a fixed value in the present moment of time, so position is represented as a tuple
    return (horizontal, depth)

# the new rules incorporate an aim factor
def determine_real_position(commands):
    # all are initialized to 0
    horizontal = 0
    depth = 0
    aim = 0

    # loop through list of input commands
    for command in commands:
        # each command is a line formatted as: "<direction>(str) <unit>(int)"
        command = command.split(" ")
        direction = command[0]
        unit = int(command[1])

        # apply conditional rules based on problem statement
        if (direction == "forward"):
            horizontal += unit
            depth += (aim * unit)
        elif (direction == "up"):
            aim -= unit
        elif (direction == "down"):
            aim += unit
    
    # return position as a fixed tuple
    return (horizontal, depth)

if __name__ == "__main__":
    input = []
    with open("input_day2.txt", "r") as file:
        input = file.readlines()

    # day two part one
    position = determine_position(input)
    print(position[0] * position[1])

    # day two part two
    real_position = determine_real_position(input)    
    print(real_position[0] * real_position[1])