from Utils.Logger import Logger
from App.IncrementVersionNumber import increase_version_number
from App.ValidateVersionFormat import validate_version_format
from App.ConvertToIntArray import convert_to_int_array

def nextVersion(version_string):
    try:
        if not version_string:
            raise Exception("Version parameter required")

        # Convert string to Integer Array
        version_array = convert_to_int_array(version_string)

        # Validate correct version format
        validate_version_format(version_array)

        # Increase Version Number
        last_position = len(version_array) - 1 #0-based array
        next_version_integer_array = increase_version_number(version_array, last_position)

        # Convert Integer array back to string and join with '.'
        updated_version_string = '.'.join(map(str, next_version_integer_array))

        return updated_version_string
    except Exception as e:
        Logger.error(str(e))
