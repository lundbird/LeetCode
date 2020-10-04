def restoreString(self, s: str, indices: List[int]) -> str:
    final_string = list(s)
    for i in range(len(indices)):
        final_string[indices[i]] = s[i]
    return ''.join(final_string)