import os
import sys
import qrcode
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_qr_code():
    try:
        # Get environment variables
        data_url = os.getenv("QR_DATA_URL", "https://github.com/ykarthik03")
        output_dir = os.getenv("QR_CODE_DIR", "qr_codes")
        filename = os.getenv("QR_CODE_FILENAME", "github_qr.png")
        fill_color = os.getenv("FILL_COLOR", "black")
        back_color = os.getenv("BACK_COLOR", "white")

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img_path = os.path.join(output_dir, filename)
        img.save(img_path)

        logging.info(f"QR code generated successfully at {img_path}")
        return 0
    except Exception as e:
        logging.error(
            f"Error generating QR code: {str(e)}", exc_info=True
        )  # Modified line 45
        return 1


if __name__ == "__main__":
    sys.exit(generate_qr_code())