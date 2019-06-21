f = open("small.txt", "r")
curpos = [0, 0]
cur_dir = "N"
obstacles = set()  # store obstacles as set of coordinate tuples
max_dist = 0  # track maximum distance the robot travels at any point
obstacle_count, action_count = f.readline().split()

# update the obstacle set
for i in range(int(obstacle_count)):
    x, y = f.readline().replace('\n', '').split()
    obstacles.add((int(x), int(y)))

for line in f:
    line_data = line.replace('\n', '').split()
    instr = line_data[0]
    move_count = line_data[1] if len(line_data) == 2 else None
    # switch current direction based on instruction
    if instr == "L":
        if cur_dir == "N":
            cur_dir = "W"
        elif cur_dir == "E":
            cur_dir = "N"
        elif cur_dir == "S":
            cur_dir = "E"
        else:
            cur_dir = "S"
    elif instr == "R":
        if cur_dir == 'N':
            cur_dir = "E"
        elif cur_dir == "E":
            cur_dir = "S"
        elif cur_dir == "S":
            cur_dir = "W"
        else:
            cur_dir = "N"
    else:
        # if instr is M we move the robot until it hits obstacle.
        # TODO add break upon hitting an obstacle. Will increase performance
        for i in range(int(move_count)):
            if cur_dir == "N":
                if (curpos[0], curpos[1]+1) not in obstacles:
                    curpos[1] += 1
            if cur_dir == "E":
                if (curpos[0]+1, curpos[1]) not in obstacles:
                    curpos[0] += 1
            if cur_dir == "S":
                if (curpos[0], curpos[1]-1) not in obstacles:
                    curpos[1] -= 1
            if cur_dir == "W":
                if (curpos[0]-1, curpos[1]) not in obstacles:
                    curpos[0] -= 1
        # update maximum found distance
        max_dist = max(max_dist, (curpos[0]**2+curpos[1]**2)**.5)

print(max_dist)


f.close()
