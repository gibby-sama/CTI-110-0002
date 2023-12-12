num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num_list = [ num1, num2, num3, num4 ]
num_prod = num1 * num2 * num3 * num4
num_avg = sum(num_list) / len(num_list)

print(f'{num_prod:.0f} {num_avg:.0f}')
print(f'{num_prod:.3f} {num_avg:.3f}')