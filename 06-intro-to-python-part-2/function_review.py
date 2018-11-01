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