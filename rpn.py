import math
import random

class Stack():
    rows = 10 #DEFINE HERE THE STACK SIZE, OR NUMBER OF ROWS OF RPN CALCULATOR
    pile = []
    def __init__(self):
        for i in range(self.rows):
            self.pile.append(0.0)
    
    def pop(self,n_last=1): #pops n_last number of last elements
        i = 1
        while i <= n_last: 
            self.pile.pop(-1)
            i = i + 1
    
    def put(self,n):        #puts number on last position of stack
        self.pile.pop(0)
        self.pile.append(n)
    
    def print_stack(self):  #print stack formatted to 4 decimal places
        for j in self.pile: print(f'{float(j):.4f}')

    def op(self, comm):     #function for mathematical operations
        res = 0             #need res initialization for try block, otherwise its not needed
        if comm in ['+','-','*','/','^']: #outer if for deciding 2 operands operation or 1 operand operation
            if comm == '+': res = self.pile[-2] + self.pile[-1]      #to add operations, add an elif clause and add in the list of outer if
            elif comm == '-': res = self.pile[-2] - self.pile[-1]
            elif comm == '*': res = self.pile[-2] * self.pile[-1]
            elif comm == '^': res = self.pile[-2] ** self.pile[-1]
            elif comm == '/': 
                try:
                    res = self.pile[-2] / self.pile[-1]
                except ZeroDivisionError: print('zero div')
            self.pop(2)
            self.pile.insert(0,0.0)
            self.pile.append(res)        
        elif comm in ['sqrt','rand']:                                          #to add operations, add an elif clause and add in the list of outer if
            if comm == 'sqrt': res = math.sqrt(self.pile[-1])
            if comm == 'rand': res = random.random()
            self.pop()
            self.pile.append(res)
        
stack1 = Stack()
inp = ''
while inp != 'exit':
    stack1.print_stack()
    inp = input('->')
    if inp == '': stack1.put(stack1.pile[-1]) 
    try:
        n = float(inp)
        stack1.put(n)
    except ValueError: stack1.op(inp)
