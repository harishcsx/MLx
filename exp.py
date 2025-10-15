# replica of original numpy array 


class MyArray:
    """
    A very simple replica of a NumPy array to demonstrate the concept.
    """
    def __init__(self, data: list):
        # This is the constructor. It runs when you create a new MyArray object.
        # It stores the list inside the object itself.
        self.data = data
        print(f"MyArray object created with data: {self.data}")

    def __repr__(self):
        # This special method controls what print() shows.
        # It provides a developer-friendly representation of the object.
        return f"MyArray({self.data})"

    def sum(self):
        # Let's add a custom method, just like NumPy's .sum()
        total = 0
        for item in self.data:
            total += item
        return total

# --- Let's use our new class! ---

# 1. Create an instance of our MyArray class
my_arr = MyArray([1, 2, 3])

# 2. Print the object itself
# Because we defined __repr__, this will print our custom string
print(f"The object is: {my_arr}")

# 3. Print the TYPE of the object
# This will now show that it belongs to our custom MyArray class!
print(f"The type is: {type(my_arr)}")

# 4. Use our custom .sum() method
print(f"The sum is: {my_arr.sum()}")