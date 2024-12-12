class MyHashMap:

    def __init__(self):
        self.buckets = [[] for i in range(25)]
        n_buckets = len(self.buckets)
        self.bucket_number_fn = lambda key: key % n_buckets

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.buckets[self.bucket_number_fn(key)].append((key, value))

    def get(self, key: int) -> int:
        return next(map(lambda e: e[1], filter(lambda e: e[0] == key, self.buckets[self.bucket_number_fn(key)])), -1)

    def remove(self, key: int) -> None:
        bucket_number = self.bucket_number_fn(key)
        self.buckets[bucket_number] = list(filter(lambda e: e[0] != key, self.buckets[bucket_number]))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
