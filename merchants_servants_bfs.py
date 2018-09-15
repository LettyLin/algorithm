class MerchantsAndServants:

    def __init__(self, m, s):
        self.merchants = m
        self.servants = s
        self.res = []

    def is_safe(self, state):
        if state[0] == 0 and (state[1] == 0 or state[1] == 1 or state[1] == 2 or state[1] ==3):
            return True
        elif state[0] == self.merchants and (state[1] == 0 or state[1] == 1 or state[1] == 2 or state[1] ==3):
            return True
        elif state[0] >= state[1] and self.merchants-state[0] >= self.servants-state[1]:
            return True
        else:
            return False

    def explore(self, state, step, last_move=(0, 0)):
        # 这里last_move不用list是因为list可变
        if step >= 20:
            return False
        if state == (3, 3):
            self.res.append(state)
            return True
        d = [(0, 1), (0, 2), (1, 1), (1, 0), (2, 0)]
        for item in d:
            if item == last_move:
                continue
            move = ((-1)**step*item[0], (-1)**step*item[1])
            next_state = (state[0] + move[0], state[1] + move[1])
            if self.is_safe(next_state) is True:
                if self.explore(next_state, step+1, item) is True:
                    self.res.append(state)
                    return True


instance = MerchantsAndServants(3, 3)
instance.explore((0, 0), 0)
print(instance.res)
