import time

for _ in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)
print(' Pronto!')


nums = [1, 5, 33, 6, 77, 3, 1, 2]
nums.sort()

print(nums)
words = ['a', 'b', 'c', 'd', 'e', 'f']

zipado = dict(zip(words, nums))
print(zipado)
