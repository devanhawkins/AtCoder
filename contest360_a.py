# Get standard input
input = input()

# Create boolean flags
rice_flag = False
error_flag = False

# Search through input string for order
for i in input:
    if i == 'M' and rice_flag == False:
        print('No')
        error_flag = True
        break
    if i == 'R':
        rice_flag = True
if error_flag == False:
    print('Yes')