"""
This module contains the methods for optimizing pokcrystal music scripts.

Copyright (C) 2020  nephitejnf and hyperdriveguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Full plain text license https://www.gnu.org/licenses/agpl-3.0.txt
"""

from random import random
import argparse


def optimize(script, name):
    """Call if importing as a module."""
    pass


class MainFileIteration():
    """Controls the primary iteration over the file."""

    def __init__(self):
        pass


class SubSearch():
    """Based on the given query, find all matches and their indexes."""

    def __init__(self):
        pass


def main():
    """For running as a standalone script."""
    parser = argparse.ArgumentParser(
        description="A script for optimizing pokecrystal music.")
    parser.add_argument('asm', help="script input file")
    parser.add_argument('name', help="name of the song (eg. \"YeetBattle\")")
    args = parser.parse_args()
    optimize(args.asm, args.name)


if __name__ == "__main__":
    main()
