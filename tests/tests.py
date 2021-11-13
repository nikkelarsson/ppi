from ppi.static import langcodes
from ppi import main
from ppi import parsing
import unittest as ut


class LangcodesTestCase(ut.TestCase):
    def test_integrity(self) -> None:
        """Test langcodes correctness."""
        for key, value in langcodes.LANGCODES.items():
            self.assertTrue(
                    value.endswith(".UTF-8"),
                    f"{value}: invalid suffix."
                    )

    @ut.skip("yet to be implemented")
    def test_validity(self) -> None:
        """Verify langcodes validity."""
        pass


class OSTestCase(ut.TestCase):
    def test_system(self) -> None:
        """Test system compatibility."""
        from sys import platform
        self.assertEqual(
                platform,
                "darwin" or "linux",
                f"{main.NAME} is only compatible with macOS and Linux."
                )


class ArgparserTestCase(ut.TestCase):
    """Tests for the Argparser -class."""
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
        self.argparser.sort_args()

    def test_input_registration(self) -> None:
        """Test that inputs are registered properly."""
        self.assertEqual(self.argparser.args, self.args_inp)
        self.assertEqual(self.argparser.name, self.name_inp)
        self.assertEqual(self.argparser.version, self.version_inp)
        self.assertEqual(self.argparser.lang, self.lang_inp)

    @ut.skip("test incomplete")
    def test_arg_sorting(self) -> None:
        """Test that args are sorted correctly."""
        self.assertEqual(self.argparser.invalid_args, ["---invalid"])


if __name__ == "__main__":
    ut.main()
