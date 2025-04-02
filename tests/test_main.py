import os
import pytest
from unittest.mock import patch, MagicMock
from main import generate_qr_code


def test_default_qr_generation():
    with patch("main.os.makedirs"), patch(
        "main.qrcode.QRCode.make_image"
    ) as mock_make_image, patch("main.logging.info") as mock_logging:

        result = generate_qr_code()
        assert result == 0
        mock_logging.assert_called_with(
            "QR code generated successfully at qr_codes/github_qr.png"
        )


def test_custom_environment_variables():
    with patch.dict(
        os.environ,
        {
            "QR_DATA_URL": "https://google.com",
            "QR_CODE_DIR": "custom_dir",
            "QR_CODE_FILENAME": "custom.png",
            "FILL_COLOR": "blue",
            "BACK_COLOR": "white",
        },
    ), patch("main.os.makedirs"), patch("main.qrcode.QRCode.make_image"):
        result = generate_qr_code()
        assert result == 0


def test_file_creation(tmpdir):
    test_dir = tmpdir.mkdir("test_qr")
    with patch.dict(os.environ, {"QR_CODE_DIR": str(test_dir)}):
        result = generate_qr_code()
        assert result == 0
        assert len(test_dir.listdir()) == 1


def test_error_handling():
    with patch(
        "main.qrcode.QRCode.make_image", side_effect=Exception("Fake Error")
    ), patch("main.logging.error") as mock_logging:
        result = generate_qr_code()
        assert result == 1
        # Check if exc_info=True is passed
        mock_logging.assert_called_with(
            "Error generating QR code: Fake Error", exc_info=True  # Add this assertion
        )


def test_directory_creation_failure():
    with patch("main.os.makedirs", side_effect=PermissionError("No permission")), patch(
        "main.logging.error"
    ) as mock_logging:
        result = generate_qr_code()
        assert result == 1
        # Check if exc_info=True is passed
        mock_logging.assert_called_with(
            "Error generating QR code: No permission",
            exc_info=True,
        )