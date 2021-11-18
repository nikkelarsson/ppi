import unittest
from ppi import parsing


class ParsingTestCase(unittest.TestCase):
    """Tests for the ArgParser -class."""
    def setUp(self) -> None:
        """Set up some values for testing."""
        self.args_inp: list = ["test", "-h", "--test", "---invalid", "-V"]
        self.name_inp: str = "name"
        self.version_inp: str = "version"
        self.lang_inp: str = "lang"
        self.argparser: object = parsing.ArgParser(
                self.args_inp,
                self.name_inp,
                self.version_inp,
                self.lang_inp
                )
        self.argparser._sort_args()

    def test_input_registration(self) -> None:
        """Test that inputs are registered properly."""
        self.assertEqual(self.argparser.args, self.args_inp)
        self.assertEqual(self.argparser.name, self.name_inp)
        self.assertEqual(self.argparser.version, self.version_inp)
        self.assertEqual(self.argparser.lang, self.lang_inp)

    @unittest.skip("test incomplete")
    def test_arg_sorting(self) -> None:
        """Test that args are sorted correctly."""
        self.assertEqual(self.argparser.invalid_args, ["---invalid"])


if __name__ == "__main__":
    unittest.main()
