balanced_brackets = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
unbalanced_brackets = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]
balanced_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}
result = balanced_brackets + unbalanced_brackets
class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_ballance(list):
    stack = Stack()
    for items in list:
        if items in balanced_dict:
            stack.push(items)
        elif items == balanced_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()


if __name__ == '__main__':
    for brackets in result:
        print(f'{brackets:<30}{check_ballance(brackets)}')