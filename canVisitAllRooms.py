def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    def dfs(node):
        if node in visited:
            return
        else:
            visited.add(node)
        for child in rooms[node]:
            dfs(child)
    dfs(0)
    return len(visited)==len(rooms)