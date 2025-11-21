import ctypes


class MultyDynArray:
    def __init__(self, dimensions, *capacities):
        self.dimensions = dimensions
        self.capacities = capacities
        self.array = self.make_array(self.capacities)

    def __getitem__(self, indices):
        if self.is_out_of_bounds(indices):
            raise IndexError('Index is out of bounds')
        return self.array[self.get_real_index(*indices)]

    def __setitem__(self, indices, val):
        # проверка на расширение
        if self.is_out_of_bounds(indices):
            new_capacities = []
            i = 0
            for index in reversed(indices):
                if index >= self.capacities[i]:
                    new_capacities.append(index + 1)
                else:
                    new_capacities.append(self.capacities[i])
                i += 1
            self.resize(tuple(new_capacities))
        # вставка
        self.array[self.get_real_index(*indices)] = val

    def is_out_of_bounds(self, indices):
        i = 0
        for index in reversed(indices):
            if index < 0 or index >= self.capacities[i]:
                return True
            i += 1
        return False

    def get_real_index(self, *indices):
        index = 0
        dim_capacity_multiplier = 1
        current_dimension = 0
        for i in reversed(indices):
            index += i * dim_capacity_multiplier
            dim_capacity_multiplier = self.dim_full_capacity[current_dimension]
            current_dimension += 1
        return index

    def get_real_level_capacity(self, *capacities):
        result = []
        calc_capacity = 1
        for cap in capacities:
            calc_capacity *= cap
            result.append(calc_capacity)
        return result
        
    def make_array(self, new_capacities):
        summary_capacity = 1
        caps = new_capacities
        for i in caps:
            summary_capacity *= i
        arr = (summary_capacity * ctypes.py_object)()
        for i in range(summary_capacity):
            arr[i] = None
        self.dim_full_capacity = self.get_real_level_capacity(*new_capacities)
        return arr

    def resize(self, new_capacities):
        new_array = self.make_array(new_capacities)
        # copy (маппим старые индексы в новые)
        for i in range(len(self.array)):
            if self.array[i] is not None:
                indices = self.retain_indices(i)
                new_index = self.get_real_index(*indices)
                new_array[new_index] = self.array[i]
        self.capacities = new_capacities
        self.array = new_array

    def retain_indices(self, index):
        result = []
        rest_count = index
        for c in self.capacities:
            result.append(rest_count % c)
            rest_count = rest_count // c
        return tuple(reversed(result))


