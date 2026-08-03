"""Tests for the widget classes."""

import unittest
from unittest.mock import patch, MagicMock


class TestLogoWidget(unittest.TestCase):
    """Test LogoWidget instantiation and behavior."""

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_creates_with_parent(self, mock_load, mock_photo, _mock_label):
        """Test widget creation with a parent."""
        from python_logo_widgets import LogoWidget  # pylint: disable=import-outside-toplevel

        parent = MagicMock()
        widget = LogoWidget(parent)
        mock_load.assert_called_once_with("logo.gif")
        mock_photo.assert_called_once_with(file="fake.gif")
        self.assertIsNotNone(getattr(widget, "_image"))

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_custom_bg(self, _mock_load, _mock_photo, mock_label):
        """Test custom background propagation."""
        from python_logo_widgets import LogoWidget  # pylint: disable=import-outside-toplevel

        parent = MagicMock()
        LogoWidget(parent, bg="white")
        mock_label.assert_called_once()
        call_kwargs = mock_label.call_args[1]
        self.assertEqual(call_kwargs["bg"], "white")


class TestPoweredByLengthWidget(unittest.TestCase):
    """Test PoweredByLengthWidget instantiation."""

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_creates_with_parent(self, mock_load, _mock_photo, _mock_label):
        """Test powered-by-length widget creation with a parent."""
        from python_logo_widgets import PoweredByLengthWidget  # pylint: disable=import-outside-toplevel

        parent = MagicMock()
        widget = PoweredByLengthWidget(parent)
        mock_load.assert_called_once_with("length.gif")
        self.assertIsNotNone(getattr(widget, "_image"))


class TestPoweredByWidthWidget(unittest.TestCase):
    """Test PoweredByWidthWidget instantiation."""

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_creates_with_parent(self, mock_load, _mock_photo, _mock_label):
        """Test powered-by-width widget creation with a parent."""
        from python_logo_widgets import PoweredByWidthWidget  # pylint: disable=import-outside-toplevel

        parent = MagicMock()
        widget = PoweredByWidthWidget(parent)
        mock_load.assert_called_once_with("width.gif")
        self.assertIsNotNone(getattr(widget, "_image"))


if __name__ == "__main__":
    unittest.main()
