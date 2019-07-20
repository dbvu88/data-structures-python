class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS

  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()

  def heapify_up(self):
    print("Heapifying up")
    # start at the last element of the list
    idx = len(self.heap_list) - 1
    # while there's a parent element available:
    while self.parent_idx(idx) > 0:
      parent_idx = self.parent_idx(idx)
      child = self.heap_list[idx]
      parent = self.heap_list[parent_idx]
      if parent > child:
        print("swapping parent_element with element_at_index")
        self.heap_list[idx] = parent
        self.heap_list[parent_idx] = child
      idx = parent_idx
