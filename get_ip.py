def get_ip():
    """Find IP address of the server"""
    wifi_name = get_wifi_name()
    print(wifi_name)
    current_datetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    f_name=f'{current_datetime}_ip_info.json'
    r = requests.get('https://ipinfo.io/')
    with open(f_name, 'w') as f_out:
        f_out.write(r.text)


if __name__ == '__main__':
    get_ip()
