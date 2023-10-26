class CustomList(list):
    def __init__(self, *args):
        # parent class constructor
        super().__init__(*args)

    def __setattr__(self, name, value):
        if name == "concat":
            self.extend(value)
        else:
            super().__setattr__(name, value)

    def __new__(cls, *args):
        return super().__new__(cls, *args)

    def __add__(self, second):
        try:
            second = CustomList(second)
            result = CustomList()
            len_max = max(len(self), len(second))
            for i in range(len_max):
                if i < len(self):
                    self_elem = self[i]
                else:
                    self_elem = 0
                if i < len(second):
                    second_elem = second[i]
                else:
                    second_elem = 0
                result.append(self_elem + second_elem)
            return result
        except TypeError:
            print("Not a list")

    def __sub__(self, second):
        try:
            second = CustomList(second)
            result = CustomList()
            len_max = max(len(self), len(second))
            for i in range(len_max):
                if i < len(self):
                    self_elem = self[i]
                else:
                    self_elem = 0
                if i < len(second):
                    second_elem = second[i]
                else:
                    second_elem = 0
                result.append(self_elem - second_elem)
            return result
        except TypeError:
            print("Not a list")

    def __rsub__(self, first):
        try:
            first = CustomList(first)
            result = CustomList()
            len_max = max(len(self), len(first))
            for i in range(len_max):
                if i < len(self):
                    self_elem = self[i]
                else:
                    self_elem = 0
                if i < len(first):
                    first_elem = first[i]
                else:
                    first_elem = 0
                result.append(first_elem - self_elem)
            return result
        except TypeError:
            print("Not a list")

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"{super().__str__()}, sum = {sum(self)}"

    def copy(self):
        return CustomList(self)
