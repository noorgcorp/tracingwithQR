import pyqrcode


def generate_qrcode(website_url: str, unique_id: int) -> None:
    url = pyqrcode.create(f'{website_url}/{unique_id}')
    url.png(f'{unique_id}.png', scale=10)
