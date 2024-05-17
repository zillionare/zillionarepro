"""Console script for zillionarepro."""

import fire


def help() -> None:
    print("zillionarepro")
    print("=" * len("zillionarepro"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
