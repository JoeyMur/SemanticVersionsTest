# Recursive method that increments 1 to the current position in the version array
# If the value at the current position is 9, set it to 0 and increment (current_position - 1)
def increase_version_number(version_array, add_to_position):
    current_value = version_array[add_to_position]

    # [:] => Creates a shallow copy of the list rather than pass by reference
    updated_array = version_array[:]

    if (add_to_position == 0 or current_value < 9):
        updated_array[add_to_position] += 1
        return updated_array
    else:
        updated_array[add_to_position] = 0
        return increase_version_number(updated_array, add_to_position - 1)