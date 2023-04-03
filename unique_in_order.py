def unique_in_order(iterable):
    unique = []
    if len(iterable) == 0:
        return unique
    elif len(iterable) == 1:
        unique.append(iterable[0])
        return unique
    else:
        for i in range(len(iterable)-1):
            if iterable[i] != iterable[i+1]:
                unique.append(iterable[i])
            else:
                if iterable.count(iterable[0]) == len(iterable):
                    unique.append(iterable[0])
        if iterable[-1] != unique[-1]:
            unique.append(iterable[-1])
        return unique


print(unique_in_order("AABBccAA"))