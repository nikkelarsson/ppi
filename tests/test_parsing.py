import sys
import unittest

from ppi import parsing


@unittest.skip("Skip for now")
class CommandLineArgumentsParsingTestCase(unittest.TestCase):
    """Tests for the ArgParser -class."""

    def setUp(self) -> None:
        """Prepare all the tests inside this class for testing."""
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

        # Append the test input straight to sys.argv
        for _ in self.input:
            sys.argv.append(_)

        self.program: str = "dummy-name"
        self.language: str = "en_US.UTF-8"
        
        self.argparser: object = parsing.ArgParser(
            self.program,
            self.language
        )

    def tearDown(self) -> None:
        """Clean things up after tests are run."""
        for idx, _ in enumerate(sys.argv):
            if idx == 0:
                continue
            del _

    def test_input_registration(self) -> None:
        """Test that inputs are registered properly."""
        self.assertEqual(self.argparser.argv, self.input)
        self.assertEqual(self.argparser.program, self.program)
        self.assertEqual(self.argparser.language, self.language)


if __name__ == "__main__":
    unittest.main()
