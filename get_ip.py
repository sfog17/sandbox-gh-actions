import datetime
import requests
from pathlib import Path

def get_ip():
    """Find IP address of the server"""
    current_datetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file= output_dir / f'{current_datetime}_ip_info.json'
    r = requests.get('https://ipinfo.io/')
    print(r.text)
    with open(output_file, 'w') as f_out:
        f_out.write(r.text)


if __name__ == '__main__':
    get_ip()
