def reconstructQueue(people):
    people.sort(key = lambda x: (x[0],-x[1])) #sorts based on height, reverse within height
    open_slots = list(range(len(people))) #track which slots are open in the queue
    result = [None] * len(people)
    for val in people:
        index = open_slots[val[1]]
        result[index] = val
        open_slots.remove(index)
    return result

if __name__=="__main__":
    test = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(reconstructQueue(test))