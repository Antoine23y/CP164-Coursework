"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Queue_Node(value, None)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1

        return None

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # your code here
        if self._count == 1:

            self._rear = None

            value = self._front._value

            self._front = None

            self._count -= 1

        else:

            temp_node = self._front._next

            value = self._front._value

            self._front = temp_node

            self._count -= 1

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        # your code here
        value = deepcopy(self._front._value)

        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        # your code here
        if self._count == 0:

            temp_node = source._front
            temp_node2 = source._front._next

            self._front = temp_node
            self._rear = temp_node
            self._front._next = None

            source._front = temp_node2

            self._count += 1
            source._count -= 1

        elif source._count == 1:

            temp_node = source._front
            temp_node2 = source._front._next

            self._rear._next = temp_node
            self._rear = source._front
            self._rear._next = None

            source._front = temp_node2
            source._rear = temp_node2

            self._count += 1
            source._count -= 1

        else:

            temp_node = source._front
            temp_node2 = source._front._next

            self._rear._next = temp_node
            self._rear = source._front
            self._rear._next = None

            source._front = temp_node2

            self._count += 1
            source._count -= 1

        return None

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # your code here
        if self._front is None:

            self._front = source._front
            self._rear = source._rear
            self._count += source._count

            source._front = None
            source._rear = None
            source._count = 0

        else:

            self._rear._next = source._front
            self._rear = source._rear
            self._count += source._count

            source._front = None
            source._rear = None
            source._count = 0

        return None

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if source1._front is None:

            self._front = source2._front
            self._rear = source2._rear
            self._count += source2._count

            source2._front = None
            source2._rear = None
            source2._count = 0

        elif source2._front is None:

            self._front = source1._front
            self._rear = source1._rear
            self._count += source1._count

            source1._front = None
            source1._rear = None
            source1._count = 0

        else:

            self._front = source1._front
            self_node = self._front

            source1_node = source1._front._next
            source2_node = source2._front

            while source1_node or source2_node is not None:

                if source2_node is not None:

                    self_node._next = source2_node
                    self_node = self_node._next

                    source2_node = source2_node._next

                if source1_node is not None:

                    self_node._next = source1_node
                    self_node = self_node._next

                    source1_node = source1_node._next

            if source1._count > source2._count:

                self._rear = source1._rear

            else:

                self._rear = source2._rear

            self._count += source1._count + source2._count

        source1._front = None
        source1._rear = None
        source1._count = 0

        source2._front = None
        source2._rear = None
        source2._count = 0

        return None

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        target1 = Queue()
        target2 = Queue()

        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)

            else:
                target2._move_front_to_rear(self)

            left = not left

        self._rear = None

        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
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

            self_node = self._front
            target_node = target._front

            while self_node is not None and equals == True:

                if self_node._value == target_node._value:

                    self_node = self_node._next
                    target_node = target_node._next

                else:

                    equals = False

        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
