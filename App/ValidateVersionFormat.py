# Condition 1: Only the first element in the version array can be greater than 9
# Condition 2: No negative numbers allowed
def validate_version_format(version_array):
    versions_without_first_element = version_array[1:]

    for part in versions_without_first_element:
        if (part < 0 or part > 9):
            raise Exception("Input version is not in the correct format")
    
    # First element in the array cannot be less than 0
    if (version_array[0] < 0):
        raise Exception("Input version is not in the correct format")