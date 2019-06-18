def isCousins(root: TreeNode, x: int, y: int) -> bool:
    q = [(root,0,None)]
    found_nodes = []
    while q:
        cur_node,cur_depth,cur_parent = q.pop()
        if cur_node is None:
            continue
        
        if cur_node.val==x or cur_node.val==y:
            found_nodes.append((cur_node,cur_depth,cur_parent))
        elif len(found_nodes)==1 and cur_depth > found_nodes[0][1]: #pruning optimization. Why pass instead of False??
            pass
        else:
            q.append((cur_node.left,cur_depth+1,cur_node))
            q.append((cur_node.right,cur_depth+1,cur_node))
    
    if len(found_nodes) != 2: #could not find two nodes
        return False
    #if depths are the same but parent is different then true
    if found_nodes[0][1] == found_nodes[1][1] and found_nodes[0][2] != found_nodes[1][2]: 
        return True
    else:
        return False