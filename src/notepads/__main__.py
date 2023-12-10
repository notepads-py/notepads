from . import (
    __version__,
    __description__,
    __python_version__,
    __author__,
    __license__,
    __copyright__,
    __credits__,
    __maintainer__,
    __email__,
    __status__,
    __repo__,
)

def main():
    notepads_table: dict = {
        'name': 'notepads',
        'version': __version__,
        'description': __description__,
        'python_version': __python_version__,
        'repo': __repo__,
        'author': __author__,
        'license': __license__,
        'copyright': __copyright__,
        'credits': __credits__,
        'maintainer': __maintainer__,
        'email': __email__,
        'status': __status__,
    }
    for key, value in notepads_table.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()
