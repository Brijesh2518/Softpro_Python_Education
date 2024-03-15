'''
Program to take full name as input
and print last name first, and first
name at the last.
'''


def reverse_full_name(full_name):
    names = full_name.split()
    if len(names) >= 2:
        reversed_name = names[-1] + ', ' + ' '.join(names[:-1])
        return reversed_name
    else:
        return "Invalid input"
full_name = input("Enter your full name: ")
reversed_full_name = reverse_full_name(full_name)
print("Reversed full name:", reversed_full_name)
