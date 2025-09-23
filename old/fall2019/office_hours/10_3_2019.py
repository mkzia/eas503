my_list = [1, 4, 6, 8]

total = 0
for i in my_list:
    total += i
    # total = total + i


print(total)
print(total/len(my_list))


won_due_to_stick_count = 0
won_due_to_switch_count = 0

for i in range(1000):
    print(i)
    wl, sw_st = sp()

    if wl == True:
        if sw_st == True:
            won_due_to_stick_count += 1
        elif sw_st == False:
            won_due_to_switch_count += 1
