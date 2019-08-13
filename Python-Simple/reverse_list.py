import sys

"""
Reverse the contents of a list, in place.
Return the reversed list after.
"""
def reverse_list(li):
    end = len(li) - 1
    for i in range(0, len(li) // 2):
        temp = li[i]
        li[i] = li[end - i]
        li[end - i] = temp
    return li


if __name__ == "__main__":
    # Lack of error checking for input argc/formatting
    print("enter list items as a single string");
    li = input();
    result = reverse_list(list(li))
    print(result)