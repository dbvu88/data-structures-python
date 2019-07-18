from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def getIndex(self, key):
    return self.compress(self.hash(key))

  def assign(self, key, value):
    array_index = self.getIndex(key)
    payload = Node([key, value])

    list_at_array = self.array[array_index]
    for node in list_at_array:
      print(node)
      if node[0] == key:
        node[1] = value
        return
    list_at_array.insert(payload)
    # print(list_at_array.head_node.get_value())

    return

  def retrieve(self, key):

    array_index = self.getIndex(key)
    list_at_index = self.array[array_index]

    for node in list_at_index:
      if node[0] == key:
        return node[1]
    return None

hash_map = HashMap(5)
hash_map.assign('Dog','Chihuahua')
hash_map.assign('Dog','Pitbull')


print(hash_map.retrieve('Dog'))
print(hash_map.retrieve('Mouse'))
