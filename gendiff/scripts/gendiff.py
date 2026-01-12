import argparse

from gendiff.core import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='output format (default: "stylish")'
        )
    
    args = parser.parse_args()
    print(f"Сравниваю файлы: {args.first_file} и {args.second_file}")
    
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()


