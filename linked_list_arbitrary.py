def deep_copy_arbitrary_pointer(head):
   #TODO: Write - Your - Code
  
  # first create a dictionary to store copy
  # the complexity of this problem is that
  # the "arbitrary" or "random" pointer can point
  # to nodes that haven't been yet created
  # so you first store the entire linked list in a hash map (one by one)
  # then you copy all the pointers on the second pass

  copy_dict = { None:None }

  current = head
  while current != None:
    copy = LinkedListNode(current.data)
    copy_dict[current] = copy
    current = current.next

  current = head
  while current != None:
    copy = copy_dict[current]
    copy.next = current.next
    copy.arbitrary = current.arbitrary
    current = current.next

  return copy_dict[head]
