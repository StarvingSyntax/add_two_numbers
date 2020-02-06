# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their
# nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# P
    # Given two linked lists with all positive or neutral numbers. You start from the back of the list, and add the nodes as if they 
    # were normal numbers
    
# E
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    
    # Input: (7 -> 2 -> 1) + (4 -> 7)
    # Output: 1 -> 0 -> 2
    
    # Look at how we add and carry over numbers.
    
# D 
    # Abstract DataType -> Nodes, as well as numbers

# A
    # Using Node class, create a front and a back
    # Find how to iterate through node
    # Iterate through node
    # 
    
# C

class Node:
    def __init__(self, data = None):
        self.data = data
        self.front = data
        self.back = None
        self.next = None



def add_two_numbers(num1: Node, num2: Node) -> Node:
    # Loop over each node
    # Build the number rather add it in real time.
        #IMPORTANT: Doing it in real time was the best solution.
    # Create variable to hold numbers as string. (It will be in reverse order.)
    # Once you have both numbers, loop over strings starting from the back to add build.
    
    str_num1 = ""
    str_num2 = ""
    
    while not num1 == None:
      str_num1 += num1 # add it the collector
      num1 = num1.next
      
    while not num2 == None:
      str_num2 += num2 # add it the collector
      num2 = num2.next
    
    str_num1 = str_num1[::-1] # convert to string and reverse it.
    str_num2 = str_num2[::-1]
    
    str_num1 = int(str_num1) + int(str_num2)
    
    
    
    # CORRECT SOLUTION FROM CLASS:
    
    # curr1 = num1
    # curr2 = num2
    # carry = 0
    # sum_list = Node()
    # curr_sum = sum_list
    
    # while curr1 or curr2 or carry:
    #     total = curr1.data + curr2.data + carry
    #     if total > 9:
    #         carry = 1
    #         total -= 10
    #         curr_sum.next = Node(total)
    #     else:
    #         carry = 0
    #         curr_sum.next = Node(total)
        
    #     # Logic goes here
    #     curr1 = curr1.next
    #     curr2 = curr2.next
    #     curr_sum = curr_sum.next
        
    # return sum_list.next
    

test = Node(5)
test.next = Node(2)
test.next.next = Node(8)
print(test.data)
print(test.next.data)
print(test.next.next.data)