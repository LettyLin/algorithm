import random


class MerchantsAndServants:
    capacity = 2

    def __init__(self, m, s):
        self.merchants = m
        self.servants = s

    def allow_status(self):
        """
        calculate the safe status of the problem
        safe when the number of merchants is more or equal than the number of servants at any coast
        S = {(x, y) | x=0,y=0,1,2,3; x=3,y=0,1,2,3; x=y=1,2}
        :return: list of all safe status
        """
        safe_set = []
        for i in range(self.merchants+1):
            for j in range(self.servants+1):
                if i == 0:
                    safe_set.append([i, j])
                elif i == self.merchants:
                    safe_set.append([i, j])
                elif (i >= j) and (self.merchants-i >= self.servants-j):
                    safe_set.append([i, j])
        return safe_set

    def allow_decision(self):
        """
        define the decision(the step stride) according to the capacity of the boat
        D = {(u, v) | 0< u+v <= 2}
        :return: list of next decision
        """
        allow_step = []
        for i in range(self.capacity+1):
            for j in range(self.capacity+1):
                if (i+j > 0) and (i+j <= self.capacity):
                    allow_step.append([i, j])

        return allow_step

    def random_algorithm(self, safe_set, allow_step):
        """
        transform: Sk+1 = Sk + (-1)**k * dk
        :param safe_set: list of safe status
        :param allow_step: list of next decision
        :return:
        """
        start = [self.merchants, self.servants]
        end = [0, 0]
        res = [start]

        step = 1
        while start != end:
            move = allow_step[random.randint(0, len(allow_step))-1]
            next_set = [start[0]+(-1)**step*move[0], start[1]+(-1)**step*move[1]]
            if next_set in safe_set:
                start = next_set
                res.append(start)
                step = step + 1

        return res


mas = MerchantsAndServants(3, 3)
safeset = mas.allow_status()
print(safeset)
allowstep = mas.allow_decision()
print(allowstep)
res = mas.random_algorithm(safeset,allowstep)
for i in res:
    print(i)

