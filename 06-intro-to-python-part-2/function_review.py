# def say_hello():
#     return "Hello!"
#     return "Goodbye"

# print(say_hello())

# def confuse():
#     print("bears")
#     return 42

# confuse()

# def more_confused():
#     2 + 2

# print(more_confused())

# def start_K(name):
#     return name[0] == "K"

# print(start_K("Karl"))
# print(start_K("Nat"))

# word = "happy"
# for num in range(len(word)):
#     print(num, word[num])

# def word_triangle(word):
#     length = len(word)
#     for n in range(length):
#         print(word[:length - n])

# word_triangle("Hello")

# def adverbly(string):
#     return string + "ly"

# def middle(a, b, c):
#     if b >= a >= c or c >= a >= b:
#        return a
#     if a >= b >= c or c >= b >= a:
#        return b
#     if a >= c >= b or b >= c >= a:
#        return c

# print(middle(10, 5, 7))


# def total_of_three():
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     num3 = int(input("Enter a third number: "))
#     sum = num1 + num2 + num3
#     print(f"{num1} + {num2} + {num3} = {sum}")

# total_of_three()

# def starts_with(t, s):
#     print(s == t[:len(s)])

# starts_with("apple", "a")
# starts_with("banana", "ban")
# starts_with("toenail", "tony")

# def total_length(list):
#     total = 0
#     for item in list:
#         total += len(item)
#     return total

# def total_length(strings):
#     return sum(map(len, strings))

# print(total_length(['Queen', 'rules']))

# def count_ch(str, char):
#     count = 0
#     for letter in str:
#         if letter == char:
#             count += 1
#     return count

# print(count_ch("the goofy doom of the balloon goons", "o"))
# print(count_ch("papa pony and the parcel post problem", "p"))
# print(count_ch("this bunch of words has no", "e"))

# def until_dot(str):
#     index = 0
#     while index < len(str) and str[index] != '.':
#         index += 1
#     return str[:index]

# print(until_dot("This is a sentence. This is another."))
# print(until_dot("192.168.200.2"))
# print(until_dot("No dots here"))

# def find_512():
#     for x in range(100):
#         for y in range(100):
#             if x * y == 512:
#                 return f"{x} * {y} == 512"
    
# print(find_512())

# def starts_with(sub, str):
#     return sub == str[:len(sub)]

# def starts_with_v1(long, short):
#     for position in range(len(short)):
#         if long[position] != short[position]:
#             return False
#     return True

# def starts_with_v2(long, short):
#     length = len(short)
#     beginning = long[0 : length]
#     if beginning == short:
#         return True
#     else:
#         return False

# def starts_with_v3(long, short):
#     return long[0:len(short)] == short

# print(starts_with('bob', 'bob newby'))
# print(starts_with('bill', 'electric bill'))
# print(starts_with('tinkerbell', 'tin'))

# starts_with_v1("tin", "tinkerbell")
# starts_with_v2("tin", "tinkerbell")
# starts_with_v3("tin", "tinkerbell")

# my solution
# def is_substring(s, t):
#     if t.find(s) != -1:
#         return True
#     else:
#         return False

# def is_substring(short, long):
#     index = 0
#     while index < (len(long) - len(short) + 1):
#         if long[index : index + len(short)] == short:
#             return True
#         index += 1
#     return False

# print(is_substring('bad', 'abracadabra'))
# print(is_substring('dab', 'abracadabra'))
# print(is_substring('pony', 'pony'))
# print(is_substring('', 'balloon'))
# print(is_substring('balloon', ''))

# def count_substring(string, target):
#     count = 0
#     index = 0
#     while index < (len(string) - len(target) + 1):
#         if string[index : index + len(target)] == target:
#             count += 1
#         index += 1
#     return count

# def locate_first(t, s):
#     return s.find(t)

# locate_first('ook', 'cookbook')
# locate_first('base', 'all your bass are belong to us')

# def locate_all(s, t):
#     l = []
#     i = 0
#     while i < (len(s) - len(t) + 1):
#         if s[i : i + len(t)] == t:
#             l.append(i)
#             i += len(t)
#         else:
#             i += 1
#     return l

# locate_all('cookbook', 'ook')
# locate_all('yesyesyes', 'yes')
# locate_all('the upside down', 'barb')

# def breakify(strings):
#     print("<br>".join(strings))

# lines = ["Haiku frogs in snow",
#          "A limerick came from Nantucket",
#          "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

# breakify(lines)

import random
import words


def silly_string(nouns, verbs, templates):
    template = random.choice(templates)
    output = []
    pos = 0

    while pos < len(template):
        if template[pos:pos+8] == '{{noun}}':
            output.append(random.choice(nouns))
            pos += 8
        elif template[pos:pos+8] == '{{verb}}':
            output.append(random.choice(verbs))
            pos += 8
        else:
            output.append(template[pos])
            pos += 1
    
    output = ''.join(output)

    return output


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))