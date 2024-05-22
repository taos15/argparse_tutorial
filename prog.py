"""This function goes though the python argparse library's tutorial.
"""

import argparse


def main():
    """This is the entry point of the program"""
    parser = argparse.ArgumentParser()

    parser.parse_args()


if __name__ == "__main__":
    main()
