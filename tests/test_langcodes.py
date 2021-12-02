import unittest
from ppi.static import lang_codes


class LangcodesTestCase(unittest.TestCase):
    def test_integrity(self) -> None:
        """Test langcodes correctness."""
        for key, value in lang_codes.LANGCODES.items():
            self.assertTrue(value.endswith(".UTF-8"), f"{value}: invalid suffix.")


if __name__ == "__main__":
    unittest.main()
