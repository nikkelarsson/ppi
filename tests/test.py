from ppi import langcodes
import unittest as ut


class LangcodesTestCase(ut.TestCase):
    def test_integrity(self) -> None:
        """Test the correctness of each langcode -variable
        defined in 'langcodes.py'."""
        for key, value in langcodes.LANGCODES.items():
            self.assertTrue(value.endswith(".UTF-8"), f"{value}: invalid suffix.")


if __name__ == "__main__":
    ut.main()
