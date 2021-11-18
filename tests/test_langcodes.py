import unittest
from ppi.static import langcodes


class LangcodesTestCase(unittest.TestCase):
    def test_integrity(self) -> None:
        """Test langcodes correctness."""
        for key, value in langcodes.LANGCODES.items():
            self.assertTrue(value.endswith(".UTF-8"), f"{value}: invalid suffix.")


if __name__ == "__main__":
    unittest.main()
