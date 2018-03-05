def cacl(expr):
    func_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    stack = []
    for c in expr:
        if c in '(+-*/':
            stack.append(c)
        elif c.strip() == '':  # 对空格的处理
            pass
        else:
            if c != ')':
                c = int(c)
                if stack[-1] in '+/-*':
                    s = stack.pop()
                    if not isinstance(stack[-1], (int, float)):
                        raise Exception('wrong expr')
                    v = stack.pop()
                    v = func_map[s](v, c)
                    stack.append(v)
                else:
                    stack.append(c)
            if c == ')':
                if isinstance(stack[-1], (int, float)):
                    v = stack.pop()
                    if stack[-1] == '(':
                        stack.pop()
                        stack.append(v)
                    else:
                        raise Exception('wrong expr')
                else:
                    raise Exception('wrong expr')
    while stack:
        c = stack.pop()
        if not isinstance(c, (int, float)):
            raise Exception('wrong expr')
        if stack[-1] in '+/-*':
            s = stack.pop()
            if not isinstance(stack[-1], (int, float)):
                raise Exception('wrong expr')
            v = stack.pop()
            v = func_map[s](v, c)
            if not stack:  # 栈顶是None时才表明表达式解析完成
                return v
        else:
            raise Exception('wrong expr')


if __name__ == '__main__':
    expr = '(3 + 4) * 5 / ((2 + 3) *3)'
    print(cacl(expr))