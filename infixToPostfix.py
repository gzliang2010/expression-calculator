"""The following steps will produce a string of tokens in postfix order.

1. Create an empty stack called opstack for keeping operators. Create an empty list for output.
2. Convert the input infix string to a list.
3. Scan the token list from left to right.
	If the token is an operand, append it to the end of the output list.
	If the token is a left parenthesis, push it on the opstack.
	If the token is a right parenthesis, pop the opstack until the corresponding 
		left parenthesis is removed. Append each operator to the end of the output list.
	If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any 
		operators already on the opstack that have higher or equal precedence and append them to the output list.
4. When the input expression has been completely processed, check the opstack. Any operators still 
	on the stack can be removed and appended to the end of the output list.
"""

from stack import Stack

def strToList(infixexpr):   # infixexpr is a string.
	infix = []
	str_num =''
	for ch in infixexpr:
		if ch == '(':
			infix.append(ch)
		elif ch in "0123456789.":
			str_num +=ch
		elif ch in "+-*/^)":
			if str_num != '':   # important
				infix.append(float(str_num))
			str_num = ''   # Don't forget to return str_num to an empty string.
			infix.append(ch)
		elif ch ==' ':
			pass
		else:
			print "invalid input!"
			return
	if str_num != '':
		infix.append(float(str_num))
	return infix          # infix is a list

def infixToPostfix(infixexpr):  # infixexpr is a string.
	infix = strToList(infixexpr)  # strToList returns a list with operand and operators
	precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3} 
	# Don't forget to put '(' in, or it will cause error in precedence["("]
	s = Stack()
	postfix = []
	for item in infix:
		if item == '(':
			s.push(item)
		elif isinstance(item, float):     # It is always a bad idea to use type(item)
			postfix.append(item)
		elif item in "+-*^/":
			while s.isEmpty() != True and precedence[item]<=precedence[s.peek()]:
				postfix.append(s.pop())
			s.push(item)
		elif item == ')':
			while s.peek() != '(':
				postfix.append(s.pop())
			s.pop()
	while s.isEmpty()!=True:
		postfix.append(s.pop())
	return postfix

"""Scan the token list from left to right.
	If the token is an operand, convert it from a string to an integer and push the value 
		onto the operandStack.
	If the token is an operator, *, /, +, or -, it will need two operands. 
		Pop the operandStack twice. The first pop is the second operand and the second pop is the 
		first operand. Perform the arithmetic operation. Push the result back on the operandStack.
When the input expression has been completely processed, the result is on the stack. 
Pop the operandStack and return the value."""

def postfixEval(postfix):
	operandStack = Stack()
	for item in postfix:
		if isinstance(item, float):
			operandStack.push(item)
		else:
			a = operandStack.pop()
			b = operandStack.pop()
			if item == '*':
				operandStack.push(b*a)
			elif item == '/':
				operandStack.push(b/a)
			elif item == '+':
				operandStack.push(b+a)
			elif item == '-':
				operandStack.push(b-a)
			elif item == '^':
				operandStack.push(b**a)
	return operandStack.pop()


infixexp = raw_input("Enter a infix expression:\n")
infixexp2 = strToList(infixexp)
print "The infix expression is:"
for item in infixexp2:
	print item,
print

postfixexp = infixToPostfix(infixexp)
print "The corresponding postfix expression is:"
for item in postfixexp:
	print item,
print
print "The result of the expression is: %.3f" %postfixEval(postfixexp)