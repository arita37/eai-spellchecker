# simple_spellcheck.py
# Guy Dumais, 2018-08-30
# Copyright (c) 2018 Element AI. All rights reserved.

import pkg_resources

from spellchecker.symspell import SymSpell, Verbosity  # import the module


def main():
    # create object
    initial_capacity = 83000
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    sym_spell = SymSpell(initial_capacity, max_edit_distance_dictionary,
                         prefix_length)
    # load dictionary
    dictionary_path = pkg_resources.resource_filename('spellchecker', 'frequency_dictionary_en_82_765.txt')
    iterator = SymSpell.SpaceDelimitedFileIterator(0, 1, dictionary_path)
    sym_spell.load_dictionary(iterator)

    # lookup suggestions for single-word input strings
    input_term = "memebers"  # misspelling of "members"
    # max edit distance per lookup
    # (max_edit_distance_lookup <= max_edit_distance_dictionary)
    max_edit_distance_lookup = 2
    suggestion_verbosity = Verbosity.CLOSEST  # TOP, CLOSEST, ALL
    suggestions = sym_spell.lookup(input_term, suggestion_verbosity,
                                   max_edit_distance_lookup)
    # display suggestion term, term frequency, and edit distance
    for suggestion in suggestions:
        print(suggestion)

    # lookup suggestions for multi-word input strings (supports compound
    # splitting & merging)
    input_term = ("whereis th elove hehad dated forImuch of thepast who "
                  "couqdn'tread in sixtgrade and ins pired him")
    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 2
    suggestions = sym_spell.lookup_compound(input_term,
                                            max_edit_distance_lookup)
    # display suggestion term, edit distance, and term frequency
    for suggestion in suggestions:
        print("{}, {}, {}".format(suggestion.term, suggestion.count,
                                  suggestion.distance))


if __name__ == "__main__":
    main()
