class multifilter:
    judge_half = lambda fx: sum(fx) >= len(fx) / 2
    judge_any = lambda fx: any(fx)
    judge_all = lambda fx: all(fx)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return (x for x in self.iterable if self.judge([f(x) for f in self.funcs]))

