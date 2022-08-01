# import Levenshtein
# import pandas as pd
# import Comparer, DataProcessing
#
# sent_1, sent_2, sent_3 = 'I love apples.', 'I loves apples.', 'I love aples.'
# sentence_dictionary = {'template': 'I love apples.',
#                        'sentence_to_test': 'I loves apples.',
#                        'results': {'SpellChecker': ['I loves apples.', {'damerau_levenshtein_distance': 1,
#                                                                         'jaro_winkler': 0.9438095238095238,
#                                                                         'levenshtein_distance': 1,
#                                                                         'similarity': 0.9655172413793104},
#                                                     1.177931785583496],
#                                    'TextBlob': ['I loves apples.', {'damerau_levenshtein_distance': 1,
#                                                                     'jaro_winkler': 0.9438095238095238,
#                                                                     'levenshtein_distance': 1,
#                                                                     'similarity': 0.9655172413793104},
#                                                 0.03294253349304199],
#                                    'Autocorrect': ['I loves apples.', {'damerau_levenshtein_distance': 1,
#                                                                        'jaro_winkler': 0.9438095238095238,
#                                                                        'levenshtein_distance': 1,
#                                                                        'similarity': 0.9655172413793104},
#                                                    0.10658097267150879],
#                                    'GingerIt': ['I love apples.', {'damerau_levenshtein_distance': 0,
#                                                                    'jaro_winkler': 1.0,
#                                                                    'levenshtein_distance': 0,
#                                                                    'similarity': 1.0}, 0.80841064453125],
#                                    'Language_tool': ['I love apples.', {'damerau_levenshtein_distance': 0,
#                                                                         'jaro_winkler': 1.0,
#                                                                         'levenshtein_distance': 0,
#                                                                         'similarity': 1.0},
#                                                      9.704583168029785],
#                                    'GingerIt(SpellChecker)': ['I love apples.', {'damerau_levenshtein_distance': 0,
#                                                                                  'jaro_winkler': 1.0,
#                                                                                  'levenshtein_distance': 0,
#                                                                                  'similarity': 1.0},
#                                                               0.6864645481109619],
#                                    'GingerIt(TextBlob)': ['I loves apples.', {'damerau_levenshtein_distance': 1,
#                                                                               'jaro_winkler': 0.9438095238095238, 'levenshtein_distance': 1, 'similarity': 0.9655172413793104}, 0.5865581035614014],
#                                    'GingerIt(Autocorrect)': ['I love apples.', {'damerau_levenshtein_distance': 0, 'jaro_winkler': 1.0, 'levenshtein_distance': 0, 'similarity': 1.0}, 0.695828914642334],
#                                    'Language_tool(SpellChecker)': ['I love apples.', {'damerau_levenshtein_distance': 0, 'jaro_winkler': 1.0, 'levenshtein_distance': 0, 'similarity': 1.0}, 13.063977718353271],
#                                    'Language_tool(TextBlob)': ['. loves apples.', {'damerau_levenshtein_distance': 2, 'jaro_winkler': 0.8548229548229549, 'levenshtein_distance': 2, 'similarity': 0.896551724137931}, 16.734331130981445],
#                                    'Language_tool(Autocorrect)': ['I love apples.', {'damerau_levenshtein_distance': 0, 'jaro_winkler': 1.0, 'levenshtein_distance': 0, 'similarity': 1.0}, 26.060853481292725],
#                                    'Median': ['I love apples.', {'damerau_levenshtein_distance': 0, 'jaro_winkler': 1.0, 'levenshtein_distance': 0, 'similarity': 1.0}, 0.12915]}}
#
# print("""("spellchecker", ""): [], "textblob": [], " autocorrect": [], " gingerit_results": [], " language_tool": [],
# " gingerit_spellchecker": [], " gingerit_textblob": [], " gingerit_autocorrect": [],
# " language_tool_spellchecker": [], " language_tool_textblob": [], " language_tool_autocorrect": [], " median": []""".replace('"', '"'))
#
#
import re

import Comparer
import DataProcessing

file = 'misspells\\4_misspell.txt'

variants = {
        # self.verify_variant(correct_spelling_spell_checker, 'SpellChecker', self.sentence_to_test)
        # self.verify_variant(correct_spelling_txt_blb, 'TextBlob', self.sentence_to_test)
        # self.verify_variant(correct_spelling_autocorrect, 'Autocorrect', self.sentence_to_test)
        # self.verify_variant(grammar_check_gingerit, 'GingerIt', self.sentence_to_test)
        # self.verify_variant(grammar_check_language_tool, 'Language_tool', self.sentence_to_test)
        # self.verify_variant(grammar_check_gingerit, 'GingerIt(SpellChecker)',
        #                     correct_spelling_spell_checker(self.sentence_to_test))
        # self.verify_variant(grammar_check_gingerit, 'GingerIt(TextBlob)',
        #                     correct_spelling_txt_blb(self.sentence_to_test))
        # self.verify_variant(grammar_check_gingerit, 'GingerIt(Autocorrect)',
        #                     correct_spelling_autocorrect(self.sentence_to_test))
        # self.verify_variant(grammar_check_language_tool, 'Language_tool(SpellChecker)',
        #                     correct_spelling_spell_checker(self.sentence_to_test))
        # self.verify_variant(grammar_check_language_tool, 'Language_tool(TextBlob)',
        #                     correct_spelling_txt_blb(self.sentence_to_test))
        # self.verify_variant(grammar_check_language_tool, 'Language_tool(Autocorrect)',
        #                     correct_spelling_autocorrect(self.sentence_to_test))
        # list_of_sentences = [str(k) for k in self.results.values() if k != 0]
        # if len(list_of_sentences) > 0:
        #     self.results['Median'] = Levenshtein.median_improve(Levenshtein.median(list_of_sentences),
        #                                                         list_of_sentences)
                                                                }

#reading files
true_positives, false_postives = [], []
with open(file) as file:
    while True:
        correct_sentence = file.readline()
        wrong_sentence = file.readline()
        if not correct_sentence:
            break
        else:
            correct_sentence = re.findall(r'[^\n]+', correct_sentence)[0]
            wrong_sentence = re.findall(r'[^\n]+', wrong_sentence)[0]
            DataProcessing.verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, correct_sentence, false_postives)
            DataProcessing.verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, wrong_sentence, true_positives)
