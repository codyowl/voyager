import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-place', '--place', help="place", required=False)
arguments = parser.parser_args()

place = arguments.place
