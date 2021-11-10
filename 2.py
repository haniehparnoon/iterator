def find_prime(n):
    prime_list = []
    for i in range(1, n):
        c = 0
        for j in range(2, i):
            if i % j == 0:
                c += 1
        if c == 0:
            prime_list.append(i)
    return prime_list


number = int(input("enter number"))
result = find_prime(number)
final_result = iter(result)
for i in range(len(result)):
    print(next(final_result))

print("--------------------------------روش دوم------------------------------")


def find_prime_less_than_input_number(n):
    for i in range(1, n):
        c = 0
        for j in range(2, i):
            if i % j == 0:
                c += 1
        if c == 0:
            yield i


number = int(input("enter number"))
p = find_prime_less_than_input_number(number)
while True:
    try:
        print(next(p))
    except StopIteration:
        break

