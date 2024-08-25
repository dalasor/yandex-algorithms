import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
            # break

        pass

    def print(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


# 1. Создание связанного списка и проверка

head = Node(3)

elems = [Node(i) for i in range(5, 16)]
random.shuffle(elems)

print('Созданные значения узлов по порядку:')
for el in elems:
    print(el.value, end=' ')
print()

ll = LinkedList(head=head)  # список создан внутри перемнной ll

for el in elems:
    ll.append(el)

print('Связанный список, порядок должен совпадать:')
ll.print()


# 2. Удаление
ll.delete(13)
ll.print()

# 3. Вставка
ll.insert(Node(100), 3)
ll.print()

# 4. Проверка на непустоту
print(ll.is_empty())