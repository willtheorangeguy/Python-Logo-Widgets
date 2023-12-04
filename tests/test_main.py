"""This is a test file for the Python-Logo-Widgets package."""
# pylint: disable=locally-disabled, wrong-import-position, import-error

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest.mock
import main


def test_widgets():
    """Test the widgets function."""
    with unittest.mock.patch(
        "main.logo_widget"
    ) as mock_logo_widget, unittest.mock.patch(
        "main.length_widget"
    ) as mock_length_widget, unittest.mock.patch(
        "main.width_widget"
    ) as mock_width_widget:
        main.widgets()
        mock_logo_widget.assert_called_once()
        mock_length_widget.assert_called_once()
        mock_width_widget.assert_called_once()
