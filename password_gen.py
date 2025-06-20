# import random
import string as s
import secrets
import math
random = secrets.SystemRandom()
# print(s.ascii_letters)

# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = '0123456789'
chars = s.ascii_letters
nums = s.digits
special = '!@$*()'
# pass_len = int(input('Enter Password lenght: '))
pass_len = 16
if (pass_len < 8):
    print('\nPassword length must be atleast 8')
    exit()
elif (pass_len > 32):
    print('\nPassword length must be less than 32')
    exit()
chars_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (chars_len + num_len)


def generate_randoms(lenght, array, chars=False):
    result = []
    for i in range(lenght):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if chars:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        result.append(character)
    return result


buffer = []
buffer.extend(generate_randoms(chars_len, chars, True))
buffer.extend(generate_randoms(num_len, nums))
buffer.extend(generate_randoms(special_len, special))
random.shuffle(buffer)
password = ''.join([str(i) for i in buffer])
print('\nGenerated Password:\n')
print(password)
