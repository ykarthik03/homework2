FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV QR_DATA_URL="https://github.com/ykarthik03" \
  QR_CODE_DIR="/app/qr_codes" \
  QR_CODE_FILENAME="github_qr.png" \
  FILL_COLOR="black" \
  BACK_COLOR="white"

VOLUME /app/qr_codes

CMD ["python", "main.py"]