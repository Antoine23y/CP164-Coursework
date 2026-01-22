"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = True

        if self._count != target._count:

            equals = False

        else:

            target_node = target._front
            self_node = self._front

            while self_node is not None and equals == True:

                if self_node._value != target_node._value:

                    equals = False

                else:

                    self_node = self_node._next
                    target_node = target_node._next

        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if self._count == 0:

            new_node = _Deque_Node(value, None, None)

            self._front = new_node
            self._rear = new_node

        else:

            new_node = _Deque_Node(value, None, self._front)

            self._front._prev = new_node
            self._front = new_node

        self._count += 1

        return None

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if self._count == 0:

            new_node = _Deque_Node(value, None, None)

            self._front = new_node
            self._rear = new_node

        else:

            new_node = _Deque_Node(value, self._rear, None)

            self._rear._next = new_node
            self._rear = new_node

        self._count += 1

        return None

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        # your code here
        value = self._front._value

        if self._count == 1:

            self._front = None
            self._rear = None
            self._prev = None

        else:

            self._front = self._front._next
            self._front._prev = None

        self._count -= 1

        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        # your code here
        value = self._rear._value

        if self._count == 1:

            self._front = None
            self._rear = None
            self._prev = None

        else:

            self._rear = self._rear._prev
            self._rear._next = None

        self._count -= 1

        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        # your code here
        return deepcopy(self._front._value)

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        # your code here
        return deepcopy(self._rear._value)

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        # your code here
        if l is not r:

            if l is self._front and r is self._rear:

                self._front = r

                r._next = l._next
                r._prev._next = l

                l._next = None
                r._prev = None

                self._rear = l

            elif r is self._front and l is self._rear:

                self._front = l

                l._next = r._next
                l._prev._next = r

                r._next = None
                l._prev = None

                self._rear = r

            elif l is self._front:

                r._prev._next = l
                r._next._prev = l

                r_next = r._next
                r_prev = r._prev

                self._front = r
                r._next = l._next
                r._prev = None

                l._next = r_next
                l._prev = r_prev

            elif r is self._front:

                l._prev._next = r
                l._next._prev = r

                l_next = l._next
                l_prev = l._prev

                self._front = l
                l._next = r._next
                l._prev = None

                r._next = l_next
                r._prev = l_prev

            elif l is self._rear:

                l._prev._next = r

                r._prev._next = l
                r._next._prev = l

                l._next = r._next
                l._prev = r._prev

                r._next = None

                self._rear = r

            elif r is self._rear:

                r._prev._next = l

                l._prev._next = r
                l._next._prev = r

                r._next = l._next
                r._prev = l._prev

                l._next = None

                self._rear = l

            elif l._next is r:

                l._prev._next = r
                l._next._prev = r
                l._next = r._next

                r._next._prev = l
                r._prev._next = l
                r._next = l

                r._prev = l._prev
                l._prev = r

            elif r._next is l:

                r._prev._next = l
                r._next._prev = l
                r._next = l._next

                l._next._prev = r
                l._prev._next = r
                l._next = r

                l._prev = r._prev
                r._prev = l

            else:

                l_prev = l._prev
                l_next = l._next

                r_prev = r._prev
                r_next = r._next

                l._prev._next = r
                l._next._prev = r

                r._prev._next = l
                r._next._prev = l

                l._next = r_next
                l._prev = r_prev

                r._next = l_next
                r._prev = l_prev

        return None

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
