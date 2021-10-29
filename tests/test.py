from ppi import langcodes
import unittest as ut


class LangcodesTestCase(ut.TestCase):
    def test_integrity(self) -> None:
        """Test the correctness of each langcode -variable
        defined in 'langcodes.py'."""
        # A correct langcode ends with ".UTF-8".
        self.codes: list = []
        for key, value in vars(langcodes).items():
            if key.isupper():
                self.codes.append(value)
        for code in self.codes:
            self.assertTrue(code.endswith(".UTF-8"), f"{code}: invalid suffix.")


if __name__ == "__main__":
    ut.main()
