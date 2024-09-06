def convert_to_int_array(version_string):
    version_array = []
    for part in version_string.split('.'):
        try:
            version_array.append(int(part))
        except ValueError:
            raise Exception(f"'{part}' cannot be converted to an integer.")

    return version_array