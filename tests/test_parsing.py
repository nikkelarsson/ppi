import unittest
from ppi import parsing


class ParsingTestCase(unittest.TestCase):
    """Tests for the ArgParser -class."""

    def setUp(self) -> None:
        """Set up some values for testing."""
        self.input: list = [
            # Invalid options
            "----this-is-a-bad-option",
            "---invalid-option",
            "--also-invalid",

            # Positional options
            "postional",
            "other_one",

            # Valid options
            "-h", "--help",
            "-V", "--version",
            "-q", "--quiet",
            "-i", "--git-init",
        ]

        self.program: str = "dummy-name"
        self.language: str = "en_US.UTF-8"
        
        self.argparser: object = parsing.ArgParser(
            self.input,
            self.program,
            self.language
        )

    def test_input_registration(self) -> None:
        """Test that inputs are registered properly."""
        self.assertEqual(self.argparser.argv, self.input)
        self.assertEqual(self.argparser.program, self.program)
        self.assertEqual(self.argparser.language, self.language)

    @unittest.skip("test incomplete")
    def test_arg_sorting(self) -> None:
        """Test that args are sorted correctly."""
        self.assertEqual(self.argparser.invalid_args, ["---invalid"])


if __name__ == "__main__":
    unittest.main()
