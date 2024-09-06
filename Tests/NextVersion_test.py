import unittest
from App.NextVersion import nextVersion
from unittest.mock import patch, MagicMock

class TestNextVersionFunctional(unittest.TestCase):
    def test_simple_increment(self):
        self.assertEqual(nextVersion("1.2.3"), "1.2.4")

    def test_rollover(self):
        self.assertEqual(nextVersion("0.9.9"), "1.0.0")

    def test_single_number(self):
        self.assertEqual(nextVersion("1"), "2")

    def test_long_version(self):
        self.assertEqual(nextVersion("1.2.3.4.5.6.7.8"), "1.2.3.4.5.6.7.9")

    def test_double_rollover(self):
        self.assertEqual(nextVersion("9.9"), "10.0")

    def test_complex_rollover(self):
        self.assertEqual(nextVersion("1.9.9"), "2.0.0")

    def test_rollover_with_leading_zero(self):
        self.assertEqual(nextVersion("0.9"), "1.0")

class TestNextVersionValidation(unittest.TestCase):

    def test_null_param(self):
        self._mock_logger(None, "Version parameter required")

    def test_empty_string(self):
        self._mock_logger("", "Version parameter required")

    def test_invalid_integer(self):
        self._mock_logger("1.9a.9", "'9a' cannot be converted to an integer.")

    def test_negative_value(self):
        self._mock_logger("1.-1", "Input version is not in the correct format")

    def test_value_too_high(self):
        self._mock_logger("1.2.3.4.5.6.7.10", "Input version is not in the correct format")

    def test_first_part_is_negative(self):
        self._mock_logger("-1.2.3.4", "Input version is not in the correct format")

    # Helper method to mock the logger
    def _mock_logger(self, current_version, log_message):
        with patch('App.NextVersion.Logger') as mock_logger:
            mock_logger.error = MagicMock()
            nextVersion(current_version)
            mock_logger.error.assert_called_once_with(log_message)

if __name__ == "__main__":
    unittest.main()