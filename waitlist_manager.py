# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name,):
        self.name = name
        self.next = None
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
	
    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        if not current:
            print("The list is empty. Add some values!")
        else:
            while current:
                print(current.name)
                current = current.next
   
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head 
        self.head = new_node  

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  

    def remove(self, name):
        if not self.head:
            return f"{name} not found"
    
   
        if self.head.name == name:
            self.head = self.head.next
            return f"{name} has been removed from the waitlist."
    
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return f"{name} has been removed from the waitlist."
            current = current.next
    



def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            print(waitlist.add_front(name))

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
The list works by connecting nodes together in a sequence, Each node stores a customer name and then points to the next node
- What role does the head play?
The head is the first point in the entire list. It points us to the first customer in the waitlist. When adding new people it creates a new node and the head points to it. When removing a customer the head changs to moves to the second node in the list.
- When might a real engineer need a custom list like this?
An engineer might use linked lists with complex data structures for stacks, queues, and graphs,
When adding and removing people quickly like what would happen with a real world queue or stack the list can be updated and changed quickly. 
'''
