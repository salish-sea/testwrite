import os
print("Current working directory is:", os.getcwd())
lines = ['This is a line', 'this is another line']
with open('text.txt', 'w') as f:
    f.writelines(lines)

with open ('text.txt', 'r') as f:
    print(f.readline())