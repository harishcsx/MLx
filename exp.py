class N_array:
    def array(self, arr: list[int]) -> list[int]:
        return arr
    

obj = N_array()
print(type(obj))
h_array = obj.array([1,2,3])
print(h_array)
print(type(h_array))