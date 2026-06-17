"""Tests for the widget classes."""

import unittest
from unittest.mock import patch, MagicMock


class TestLogoWidget(unittest.TestCase):
    """Test LogoWidget instantiation and behavior."""

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_creates_with_parent(self, mock_load, mock_photo, mock_label):
        from python_logo_widgets import LogoWidget

        parent = MagicMock()
        widget = LogoWidget(parent)
        mock_load.assert_called_once_with("logo.gif")
        mock_photo.assert_called_once_with(file="fake.gif")
        self.assertIsNotNone(widget._image)

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_custom_bg(self, mock_load, mock_photo, mock_label):
        from python_logo_widgets import LogoWidget

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
    def test_creates_with_parent(self, mock_load, mock_photo, mock_label):
        from python_logo_widgets import PoweredByLengthWidget

        parent = MagicMock()
        widget = PoweredByLengthWidget(parent)
        mock_load.assert_called_once_with("length.gif")
        self.assertIsNotNone(widget._image)


class TestPoweredByWidthWidget(unittest.TestCase):
    """Test PoweredByWidthWidget instantiation."""

    @patch("python_logo_widgets.widgets.tk.Label")
    @patch("python_logo_widgets.widgets.tk.PhotoImage")
    @patch("python_logo_widgets.widgets._load_image", return_value="fake.gif")
    def test_creates_with_parent(self, mock_load, mock_photo, mock_label):
        from python_logo_widgets import PoweredByWidthWidget

        parent = MagicMock()
        widget = PoweredByWidthWidget(parent)
        mock_load.assert_called_once_with("width.gif")
        self.assertIsNotNone(widget._image)


if __name__ == "__main__":
    unittest.main()
