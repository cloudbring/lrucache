import unittest
from src.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)  # Create a cache with capacity 2 for most tests

    def test_put_and_get(self):
        self.cache.put("key1", "value1")
        value, found = self.cache.get("key1")
        self.assertTrue(found)
        self.assertEqual(value, "value1")

    def test_capacity_limit(self):
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")  # This should evict key1
        _, found = self.cache.get("key1")
        self.assertFalse(found)
        _, found = self.cache.get("key2")
        self.assertTrue(found)
        _, found = self.cache.get("key3")
        self.assertTrue(found)

    def test_lru_eviction_order(self):
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.get("key1")  # Access key1 to make it most recently used
        self.cache.put("key3", "value3")  # This should evict key2
        _, found = self.cache.get("key2")
        self.assertFalse(found)
        _, found = self.cache.get("key1")
        self.assertTrue(found)
        _, found = self.cache.get("key3")
        self.assertTrue(found)

    def test_update_existing_key(self):
        self.cache.put("key1", "value1")
        self.cache.put("key1", "new_value1")
        value, found = self.cache.get("key1")
        self.assertTrue(found)
        self.assertEqual(value, "new_value1")

    def test_get_nonexistent_key(self):
        value, found = self.cache.get("nonexistent")
        self.assertFalse(found)
        self.assertIsNone(value)

    def test_large_capacity(self):
        large_cache = LRUCache(1000)
        for i in range(1000):
            large_cache.put(f"key{i}", f"value{i}")
        for i in range(1000):
            value, found = large_cache.get(f"key{i}")
            self.assertTrue(found)
            self.assertEqual(value, f"value{i}")
    
    def test_complex_usage_scenario(self):
        # Create a cache with capacity 3
        cache = LRUCache(3)
        print("\nInitial state:", cache)

        # Step 1: Add 3 items
        cache.put("A", 1)
        print("After adding A:", cache)
        cache.put("B", 2)
        print("After adding B:", cache)
        cache.put("C", 3)
        print("After adding C:", cache)

        # Step 2: Get an existing item
        value, found = cache.get("A")
        print("After getting A:", cache)
        self.assertTrue(found)
        self.assertEqual(value, 1)

        # Step 3: Add a new item
        cache.put("D", 4)
        print("After adding D:", cache)

        # Verify D exists
        value, found = cache.get("D")
        self.assertTrue(found)
        self.assertEqual(value, 4)

        # Verify B does not exist (should have been evicted)
        value, found = cache.get("B")
        self.assertFalse(found)

if __name__ == '__main__':
    unittest.main()