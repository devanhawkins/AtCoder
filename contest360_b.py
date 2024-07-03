# Get standard input
input = input().split()
s = input[0]
t = input[1]

def check_next_in_seq (s_str, t_target, position, w_spacer):
    # Check for out of bounds
    if 0 <= ((position * w_spacer) - 1) < len(s_str):
        #print(s_str[(position * w_spacer) - 1] + ' ' + t[position - 1])
        result = s_str[(position * w_spacer) - 1] == t[position- 1]
    else:
        #End of string. Return false
        #print('end')
        return False
    
    # If there is a match, check the next letter in the sequence
    if result == True:
        # Check if that was the last letter of t
        if len(t_target) == (position):
            return True

        else:
            # Continue to next letter in sequence
            return check_next_in_seq(s_str, t_target, position + 1, w_spacer)
    else:
        return False
    

# Loop through each possible sub-string length
w = 1
err_flag = True
while w < len(s):
    pair_exists = check_next_in_seq(s, t, 1, w)
    if pair_exists == True:
        print('Yes')
        err_flag = False
        break
    w += 1

if err_flag == True:
    print('No')