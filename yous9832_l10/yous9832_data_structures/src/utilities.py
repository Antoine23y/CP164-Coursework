"""
-------------------------------------------------------
stack and queue modification Methods named Utilities 
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from copy import deepcopy

# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        temp_value = source[-1]
        stack.push(temp_value)
        source.pop()

    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        value = stack.pop()
        target.insert(0, value)

    return None


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # Initializing Stack and source
    s = Stack()
    temp_source = deepcopy(source)

    # Testing is_empty Method
    b = s.is_empty()
    print(f'Expects True Output from is_empty Method -> Returned: {b}')

    # Testing push Method
    for x in temp_source:
        s.push(x)

    stack_values = []
    for v in s:
        stack_values.append(v)

    is_equal = '=='

    if temp_source != stack_values:
        is_equal = '!='

    print(
        f'Expects temp_source == stack_values Output from push Method -> Returned: {temp_source} {is_equal} {stack_values}')

    # Testing peek Method
    value = s.peek()

    is_equal = '=='

    if value != temp_source[-1]:
        is_equal = '!='

    print(
        f'Expects value == temp_source[-1] Output from push Method -> Returned: {value} {is_equal} {temp_source[-1]}')

    # Testing pop Method
    value = s.pop()
    stack_values = []
    for v in s:
        stack_values.append(v)

    is_equal = '=='
    is_equal_1 = '=='

    if value != temp_source[-1]:
        is_equal = '!='

    if stack_values != temp_source[:-1]:
        is_equal_1 = '!='

    print(
        f'Expects value == temp_source[-1] and stack_values == temp_source[:-1] Output from pop Method -> Returned: {value} {is_equal} {temp_source[-1]} and {stack_values} {is_equal_1} {temp_source[:-1]}')

    # Testing is_empty Method
    b = s.is_empty()
    print(f'Expects False Output from is_empty Method -> Returned: {b}')

    return None


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        temp_value = source[0]
        queue.insert(temp_value)

        source.pop(0)

    return None


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        value = queue.remove()
        target.append(value)

    return None


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    temp_source = deepcopy(a)

    # Testing is_empty Method
    b = q.is_empty()
    print(f'Expects True Output from is_empty Method -> Returned: {b}')

    # Testing push Method
    for x in temp_source:
        q.insert(x)

    queue_values = []
    for v in q:
        queue_values.append(v)

    is_equal = '=='

    if temp_source != queue_values:
        is_equal = '!='

    print(
        f'Expects temp_source == reversed(queue_values) Output from push Method -> Returned: {temp_source} {is_equal} {queue_values}')

    # Testing peek Method
    value = q.peek()

    is_equal = '=='

    if value != temp_source[0]:
        is_equal = '!='

    print(
        f'Expects value == temp_source[0] Output from push Method -> Returned: {value} {is_equal} {temp_source[0]}')

    # Testing remove Method
    value = q.remove()
    queue_values = []
    for v in q:
        queue_values.append(v)

    is_equal = '=='
    is_equal_1 = '=='

    if value != temp_source[0]:
        is_equal = '!='

    if queue_values != temp_source[1:]:
        is_equal_1 = '!='

    print(
        f'Expects value == temp_source[0] and queue_values == temp_source[1:] Output from remove Method -> Returned: {value} {is_equal} {temp_source[0]} and {queue_values} {is_equal_1} {temp_source[1:]}')

    # Testing is_empty Method
    b = q.is_empty()
    print(f'Expects False Output from is_empty Method -> Returned: {b}')

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        temp_value = source[0]
        pq.insert(temp_value)

        source.pop(0)

    return None


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not pq.is_empty():
        value = pq.remove()
        target.append(value)

    return None


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    temp_source = deepcopy(a)

    # Testing is_empty Method
    b = pq.is_empty()
    print(f'Expects True Output from is_empty Method -> Returned: {b}')

    # Testing push Method
    for x in temp_source:
        pq.insert(x)

    queue_values = []
    for v in pq:
        queue_values.append(v)

    is_equal = '=='

    if temp_source != queue_values:
        is_equal = '!='

    print(
        f'Expects temp_source == queue_values Output from push Method -> Returned: {temp_source} {is_equal} {queue_values}')

    # Testing peek Method
    value = pq.peek()

    is_equal = '=='

    if value != min(temp_source):
        is_equal = '!='

    print(
        f'Expects value == min(temp_source) Output from push Method -> Returned: {value} {is_equal} {min(temp_source)}')

    # Testing remove Method
    value = pq.remove()
    queue_values = []
    for v in pq:
        queue_values.append(v)

    is_equal = '=='

    if value != min(temp_source):
        is_equal = '!='

    print(
        f'Expects value == min(temp_source) Output from remove Method -> Returned: {value} {is_equal} {min(temp_source)}')

    # Testing is_empty Method
    b = pq.is_empty()
    print(f'Expects False Output from is_empty Method -> Returned: {b}')

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        temp_value = source[0]
        llist.append(temp_value)
        source.pop(0)

    return None


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not llist.is_empty():
        value = llist.pop(0)
        target.append(value)

    return None


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    temp_source = deepcopy(source)

    # Testing is_empty Method
    b = lst.is_empty()
    print(f'Expects True Output from is_empty Method -> Returned: {b}')

    # Testing insert Method
    for i in range(len(temp_source)):
        lst.insert(i, temp_source[i])

    list_values = []
    for v in lst:
        list_values.append(v)

    is_equal = '=='

    if temp_source != list_values:
        is_equal = '!='

    print(
        f'Expects temp_source == list_values Output from push Method -> Returned: {temp_source} {is_equal} {list_values}')

    # Testing count Method
    value = lst.count(temp_source[0])

    is_equal = '=='

    count = 0
    for x in temp_source:
        if x == temp_source[0]:
            count += 1

    if value != count:
        is_equal = '!='

    print(
        f'Expects value == count Output from count Method -> Returned: {value} {is_equal} {count}')

    # Testing Remove Method
    value = lst.remove(temp_source[0])
    list_values = []
    for v in lst:
        list_values.append(v)

    is_equal = '=='

    if value != temp_source[0]:
        is_equal = '!='

    print(
        f'Expects value == temp_source[0] Output from remove Method -> Returned: {value} {is_equal} {temp_source[0]}')

    temp_source.pop(0)

    # Testing Index Method
    n = lst.index(temp_source[0])

    is_equal = '=='

    if n != 0:
        is_equal = '!='

    print(
        f'Expects n == 0 Output from index Method -> Returned: {n} {is_equal} {0}')

    # Testing Find Method
    value = lst.find(temp_source[0])

    is_equal = '=='

    if value != temp_source[0]:
        is_equal = '!='

    print(
        f'Expects value == temp_source[0] Output from index Method -> Returned: {value} {is_equal} {temp_source}')

    # Testing Max Method
    value = lst.max()

    is_equal = '=='

    if value != max(temp_source):
        is_equal = '!='

    print(
        f'Expects value == max(temp_source) Output from index Method -> Returned: {value} {is_equal} {max(temp_source)}')

    # Testing Min Method
    value = lst.min()

    is_equal = '=='

    if value != min(temp_source):
        is_equal = '!='

    print(
        f'Expects value == min(temp_source) Output from index Method -> Returned: {value} {is_equal} {min(temp_source)}')

    # Testing is_empty Method
    b = lst.is_empty()
    print(f'Expects False Output from is_empty Method -> Returned: {b}')

    return
