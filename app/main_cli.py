import argparse


def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic CLI App")
    parser.add_argument("--name", help="Your name", required=True)
    args = parser.parse_args()

    greet(args.name)
