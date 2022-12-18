rock_types = [
    "####",
    ".#.\n###\n.#.",
    "..#\n..#\n###",
    "#\n#\n#\n#",
    "##\n##"
]

input_file_path = "day17/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = list(infile.read())

k = 0
top = 0
landed = [0, 0, 0, 0, 0, 0, 0]

for i in range(1, 3):
    rock_type = rock_types[i % len(rock_types)]
    rock_width = len(list(rock_type.split("\n")[0]))
    left_edge = 2
    bottom = top + 3

    f = 0
    rock_is_falling = True
    while rock_is_falling:
        jet_pattern = input[f % len(input)]
        if jet_pattern == ">":
            if left_edge + rock_width < 6:
                left_edge += 1
                print(f"Rock {i} is pushed to the right; the left edge is now at {left_edge}")
            else:
                print(f"Rock {i} can't move any further to the right")
        else:
            if left_edge > 0:
                left_edge -= 1
                print(f"Rock {i} is pushed to the left; the left edge is now at {left_edge}")
            else:
                print(f"Rock {i} can't move any further to the left")

        # Has the rock landed yet?
        rock_rows = rock_type.split("\n")

        for j, pixel in enumerate(list(rock_rows[-1])):
            if pixel == "#" and landed[j + left_edge] + 1 == bottom:
                print(f"Pixel {j} of rock {i} has made contact with a solid object, causing it to come to rest")
                rock_is_falling = False
                break

        if len(rock_rows) > 1:
            for j, pixel in enumerate(list(rock_rows[-2])):
                if pixel == "#" and landed[j + left_edge] + 2 == bottom:
                    print(
                        f"Pixel {j} of the second row of rock {i} has made contact with a solid object, causing it to come to rest")
                    rock_is_falling = False
                    break

        if not rock_is_falling:
            for j, row in enumerate(reversed(rock_rows)):
                for k, pixel in enumerate(list(row)):
                    if pixel == "#":
                        landed[k + left_edge] = max(landed[k + left_edge], bottom + j)

        bottom -= 1
        f += 1

    top = max(landed)

print(top)
