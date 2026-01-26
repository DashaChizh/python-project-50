import argparse

from gendiff.core import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        'first_file',
        help='Path to first file'
    )
    parser.add_argument(
        'second_file',
        help='Path to second file'
    )

    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help='output format: stylish, plain or json'
        )
    
    args = parser.parse_args()
    print(f"Сравниваю файлы: {args.first_file} и {args.second_file}\n")
    
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()


