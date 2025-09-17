class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # referencia al siguiente nodo

    def __repr__(self):
        return f"Node({self.data!r})"




class SinglyLinkedList:
  def __init__(self):
        self.head = None


  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


  def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node



  def append_tail(self, data):
    node = Node(data)
    if self.tail is None:  # lista vacía
        self.head = self.tail = node
    else:
        self.tail.next = node
        self.tail = node
    self._size += 1 

  def pop_first(self):
    if not self.head:
        return None
    value = self.head.data
    self.head = self.head.next
    return value

  def __str__(self):
    values = []
    current = self.head
    while current:
        values.append(str(current.data))
        current = current.next
    return " -> ".join(values) + " -> None" 

  def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data
  
  def find(self, target):
    current = self.head
    index = 0
    while current:
        if current.data == target:
            return index
        current = current.next
        index += 1
    return -1
  
  def get(self, index):
        return self._node_at(index).data

  def set(self, index, data):
        self._node_at(index).data = data

  def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("índice fuera de rango")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
      
  def traverse(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

  def insert(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("índice fuera de rango")
        if index == 0:
            return self.prepend(data)
        if index == self._size:
            return self.append(data)
        prev = self._node_at(index - 1)
        node = Node(data, prev.next)
        prev.next = node
        self._size += 1          



sll = SinglyLinkedList()
sll.append(10)
sll.prepend(5)
sll.append(20)
sll.insert(1, 7)   # 5, 7, 10, 20
print(sll)         # SLL([5, 7, 10, 20])
print(len(sll))    # 4
print(sll.get(2))  # 10
sll.set(2, 11)     # 5, 7, 11, 20
sll.remove(7)      # 5, 11, 20
sll.pop_first()    # 11, 20
sll.pop()          # 11
sll.reverse()      # 11
print(list(sll))






























































