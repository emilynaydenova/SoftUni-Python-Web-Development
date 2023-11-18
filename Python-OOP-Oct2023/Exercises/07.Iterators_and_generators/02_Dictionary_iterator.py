class dictionary_iter:
    def __init__(self, in_dict: dict):
        self.in_dict = in_dict
        self.list_of_tuples = [(k, v) for k, v in self.in_dict.items()]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.list_of_tuples):
            temp = self.list_of_tuples[self.idx]
            self.idx += 1
            return temp
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# My 2021

class dictionary_iter:
    def __init__(self, dict_obj):
        self.i = 0
        self.dict_tuples = (dict_obj.items())  # tuple of tuples

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.dict_tuples):
            idx = self.i
            self.i += 1
            return self.dict_tuples[idx-1]
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
