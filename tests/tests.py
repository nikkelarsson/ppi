from ppi import langcodes
from ppi import main
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


if __name__ == "__main__":
    ut.main()
