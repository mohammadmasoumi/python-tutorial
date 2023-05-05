"""
101101
010110
"""

input_ch = input() # "101101"
output_ch = input() # "010110"

zero_2_one_cnt = 0
one_2_zero_cnt = 0

for idx in range(len(input_ch)):
    # input_ch[idx]: "1" or "0"
    if input_ch[idx] != output_ch[idx]:
        if input_ch[idx] == "1": # input:1 output:0
            one_2_zero_cnt += 1
        else: # input:0 output: 1
            zero_2_one_cnt += 1

print(min(one_2_zero_cnt, zero_2_one_cnt) + abs(one_2_zero_cnt - zero_2_one_cnt))
print(max(one_2_zero_cnt, zero_2_one_cnt))