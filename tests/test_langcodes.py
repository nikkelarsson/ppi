import unittest
from ppi import constants


class LangcodesTestCase(unittest.TestCase):
    """Tests regarding language codes."""

    def test_integrity(self) -> None:
        """Test langcodes correctness."""
        for key, value in constants.LANG_CODES.items():
            self.assertTrue(value.endswith(".UTF-8"), f"{value}: invalid suffix.")


if __name__ == "__main__":
    unittest.main()
