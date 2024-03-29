from Stack import Stack


def infix_to_postfix(infix):
    postfix = ""
    st = Stack()

    for symbol in infix:
        if symbol == ' ' or symbol == '\t':  # ignore blanks and tabs
            continue

        if symbol == '(':
            st.push(symbol)
        elif symbol == ')':
            next1 = st.pop()
            while next1 != '(':
                postfix = postfix + next1
                next1 = st.pop()
        elif symbol in '+-*/%^':
            while not st.is_empty() and precedence(st.peek()) >= precedence(symbol):
                postfix = postfix + st.pop()
            st.push(symbol)
        else:  # operand
            postfix = postfix + symbol

    while not st.is_empty():
        postfix = postfix + st.pop()
    return postfix


def precedence(symbol):
    if symbol == '(':
        return 0
    elif symbol == '+-':
        return 1
    elif symbol == '*/%':
        return 2
    elif symbol == '^':
        return 3
    else:
        return 0


def evaluate_postfix(postfix):
    st = Stack()

    for symbol in postfix:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == '+':
                st.push(y + x)
            elif symbol == '-':
                st.push(y - x)
            elif symbol == '*':
                st.push(y * x)
            elif symbol == '/':
                st.push(y / x)
            elif symbol == '%':
                st.push(y % x)
            elif symbol == '^':
                st.push(y ** x)

    return st.pop()


#################################################

while True:
    print("Enter infix expression (q to quit) : ", end='')
    expression = input()
    if expression == "q":
        break

    postfix1 = infix_to_postfix(expression)
    print("Postfix expression is : ", postfix1)
    print("Value of expression : ", evaluate_postfix(postfix1))
