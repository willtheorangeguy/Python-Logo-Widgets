"""Tests for backward-compatible functions and demo."""

import unittest
from unittest.mock import patch, MagicMock


class TestCompatFunctions(unittest.TestCase):
    """Test that legacy wrapper functions create root and call mainloop."""

    @patch("python_logo_widgets._compat.LogoWidget")
    @patch("python_logo_widgets._compat.tk.Tk")
    def test_logo_widget(self, mock_tk, mock_cls):
        from python_logo_widgets._compat import logo_widget

        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        logo_widget()
        mock_root.title.assert_called_once_with("Python Logo Widget")
        mock_cls.assert_called_once_with(mock_root)
        mock_root.mainloop.assert_called_once()

    @patch("python_logo_widgets._compat.PoweredByLengthWidget")
    @patch("python_logo_widgets._compat.tk.Tk")
    def test_length_widget(self, mock_tk, mock_cls):
        from python_logo_widgets._compat import length_widget

        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        length_widget()
        mock_root.title.assert_called_once_with("Python Powered Widget")
        mock_cls.assert_called_once_with(mock_root)
        mock_root.mainloop.assert_called_once()

    @patch("python_logo_widgets._compat.PoweredByWidthWidget")
    @patch("python_logo_widgets._compat.tk.Tk")
    def test_width_widget(self, mock_tk, mock_cls):
        from python_logo_widgets._compat import width_widget

        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        width_widget()
        mock_root.title.assert_called_once_with("Python Powered Widget")
        mock_cls.assert_called_once_with(mock_root)
        mock_root.mainloop.assert_called_once()


class TestDemo(unittest.TestCase):
    """Test the demo function."""

    @patch("python_logo_widgets._demo.PoweredByWidthWidget")
    @patch("python_logo_widgets._demo.PoweredByLengthWidget")
    @patch("python_logo_widgets._demo.LogoWidget")
    @patch("python_logo_widgets._demo.tk.Tk")
    def test_demo_creates_all_widgets(self, mock_tk, mock_logo, mock_length, mock_width):
        from python_logo_widgets._demo import demo

        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        demo()
        mock_logo.assert_called_once_with(mock_root)
        mock_length.assert_called_once_with(mock_root)
        mock_width.assert_called_once_with(mock_root)
        mock_root.mainloop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
