def doesValidArrayExist(self, derived: List[int]) -> bool:
    return reduce(xor, derived) == 0