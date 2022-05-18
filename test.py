lines = ['This is a line', 'this is another line']
with open('text.txt', 'w') as f:
    f.writelines(lines)