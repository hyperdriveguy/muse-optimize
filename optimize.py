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


def optimize(music, name):
    """Call if importing as a module."""
    search = MetaSearch(music, name)
    search.iterate_script()


class MetaSearch():
    """Controls the primary iteration over the file."""

    def __init__(self, music, name):
        self.music = music
        self.song_name = name
        # Start at the beginning of the file
        self.main_file_index = 0

    def iterate_script(self):
        while self.main_file_index < len(self.music):
            self.search_in_place()
            self.main_file_index += 1

    def search_in_place(self):
        # minimum search size to see space savings is 4
        search_size = 4
        # 2D list for calculating ideal optimizations
        search_results = []
        while not search_is_over(search_results):
            # Set the parameters for a new search
            search_array = []
            for index in range(self.main_file_index,
                               self.main_file_index + search_size):
                try:
                    search_array.append(self.music[index])
                except IndexError:
                    # Can't search past the end of the file
                    pass
            print('found', len(self.check_matches(search_array)), 'match(es)')
            search_results.append(self.check_matches(search_array))
            # Increment search length to find optimum savings
            search_size += 1
        # TODO: pick most optimal search size and use it

    def check_matches(self, search):
        """Iterate over the file to check for search matches."""
        match_indexes = []
        for file_index in range(0, len(self.music)):
            # See if the line we're on matches the first line in the search
            if search[0] == self.music[file_index]:
                # Innocent until proven guilty
                search_match = True
                # We need to check the other values
                for search_index in range(0, len(search)):
                    try:
                        if(search[search_index] !=
                                self.music[search_index + file_index]):
                            search_match = False
                            break
                    except IndexError:
                        # Past EOF, so it's not a match
                        search_match = False
                        break
                if search_match:
                    match_indexes.append(file_index)
        # Sort out conflicts
        conflicts = []
        for match in match_indexes:
            try:
                if(match_indexes[match_indexes.index(match) + 1]
                        < match + len(search)):
                    conflicts.append(match_indexes.index(match) + 1)
            except IndexError:
                # We reached the end, nothing to be concerned over
                pass
        # Iterate through the conflicts backwards to avoid messing up indexes
        for conflict_index in range(len(conflicts) - 1, -1, -1):
            print(match_indexes)
            print('trying to rm:', conflicts[conflict_index])
            match_indexes.pop(conflicts[conflict_index])
            print('success rm:', conflicts[conflict_index])
        return match_indexes


def search_is_over(results):
    # If the list is empty, don't bother (avoids IndexError)
    print('results:', results)
    if len(results) < 1:
        return False
    if len(results[-1]) == 1:
        return True
    else:
        return False


def main():
    """For running as a standalone script."""
    parser = argparse.ArgumentParser(
        description="A script for optimizing pokecrystal music.")
    parser.add_argument('asm', help="script input file")
    parser.add_argument('name', help="name of the song (eg. \"YeetBattle\")")
    args = parser.parse_args()
    with open(args.asm, 'r') as music:
        file_array = music.readlines()
    optimize(file_array, args.name)


if __name__ == "__main__":
    main()
