# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
        return str1.find(str2)

print(find_substring("Hello, world!", "world"))
print(find_substring("The quick brown fox jumps over the lazy dog", "cat"))



