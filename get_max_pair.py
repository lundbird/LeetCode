def get_max_pair(items,cap):
    l, r = 0, len(items)-1
    max_val = 0
    while l<r:
        weight = items[l][0]+items[r][0]
        max_val = max(items[l][1]+items[r][1],max_val)
        if weight < cap:
            l += 1
        else:
            r -= 1
    return max_val

items =[(2,2),
        (3,3),
        (4,5),
        (5,6),
        (6,8),
        (7,10),
        (8,13),
         ]

print(get_max_pair(items,13)) #19