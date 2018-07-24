class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, item):
        if item > 0:
            super(PositiveList, self).append(item)
        else:
            raise NonPositiveError

lst = PositiveList([1, 2, 3])
lst.append(2)
lst.append(0)
lst.append(-1)