import argparse


def cli_main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="Model to use for inference", required=True)
    parser.add_argument("-t", "--text", help="Text to run inference on", required=True)
    args = parser.parse_args()

    print(f"Model: {args.model}")
    print(f"Text: {args.text}")


if __name__ == "__main__":
    cli_main()
