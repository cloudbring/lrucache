from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__cache = OrderedDict()

    def put(self, key, value):
        print(f"Putting {key}: {value}")
        if key in self.__cache:
            print(f"Key {key} already exists, updating position")
            self.__cache.move_to_end(key)
        elif len(self.__cache) >= self.__capacity:
            removed = self.__cache.popitem(last=False)
            print(f"Cache full, removing {removed}")
        self.__cache[key] = value
        print(f"Cache after put: {list(self.__cache.keys())}")

    def get(self, key):
        print(f"Getting {key}")
        if key in self.__cache:
            value = self.__cache.pop(key)
            self.__cache[key] = value
        print(f"{key} not found")
        return None, False

# For debugging purposes
def __str__(self):
        return f"Cache state: {list(self.__cache.keys())}"