import os.path
import sys

import pandas as pd
import Comparer, time, re
import MisspellGenerator


def verify_sentences(foo, template: str, test_sentence: str, path_to_file: str):
    start_time = time.time()
    dictionary = Comparer.Tested_Sentence(template, str(foo(test_sentence))).__dict__
    dictionary['time'] = time.time() - start_time
    pd.json_normalize(dictionary).to_csv('results\\' + path_to_file, mode='a+', index=False, header=False)
    del dictionary
    print("GLOBALS:", globals())
    print("LOCAL:", locals())
    print("VARS:", vars())
    print("DIR:", dir())

# spellchecker_results, textblob_results, autocorrect_results, gingerit_results, language_tool, gingerit_spellchecker, gingerit_textblob, gingerit_autocorrect, language_tool_spellchecker, language_tool_textblob, language_tool_autocorrect, median = [], [], [], [], [], [], [], [], [], [], [], []


# def write_pd_to_csv(path_to_file: str, list_of_dictionaries: list):
#     pd.json_normalize(list_of_dictionaries).to_csv(path_to_file, mode='a+', index=False, header=False)


# true_negatives = {
#     "spellchecker": (Comparer.correct_spelling_spell_checker), "textblob": (correct_spelling_txt_blb), "autocorrect": (), "gingerit_results": (), "language_tool": (),
#     "gingerit_spellchecker": (), "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": (), "language_tool_textblob": (), "language_tool_autocorrect": (), "median": ()

# true_positives = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }
#
# false_positives = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }
#
# one_misspell = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }
#
# two_misspells = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }
#
# three_misspells = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }
#
# four_misspells = {
#     "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
#     "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
# }

directory = 'grammar_incorrect'
for file in os.listdir(directory):
    with open(directory + '\\' + file) as file:
        while True:
            correct_sentence = file.readline()
            wrong_grammar_sentence = file.readline()
            if not correct_sentence:
                break

            else:
                start_time = time.time()
                correct_sentence = re.findall(r'[^\n]+', correct_sentence)[0]
                wrong_grammar_sentence = re.findall(r'[^\n]+', wrong_grammar_sentence)[0]
                misspells = [MisspellGenerator.misspell_sentence(correct_sentence, k) for k in range(1, 5)]
                print(misspells)

                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, correct_sentence,
                                 'spellchecker\\false_positives.csv')
                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, wrong_grammar_sentence,
                                 'spellchecker\\true_positives.csv')
                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[0],
                                 'spellchecker\\one_misspell.csv')
                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[1],
                                 'spellchecker\\two_misspells.csv')
                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[2],
                                 'spellchecker\\three_misspells.csv')
                verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[3],
                                 'spellchecker\\four_misspells.csv')

                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, correct_sentence,
                                 'textblob\\false_positives.csv')
                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, wrong_grammar_sentence,
                                 'textblob\\true_positives.csv')
                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[0],
                                 'textblob\\one_misspell.csv')
                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[1],
                                 'textblob\\ two_misspells.csv')
                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[2],
                                 'textblob\\three_misspells.csv')
                verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[3],
                                 'textblob\\four_misspells.csv')

                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, correct_sentence,
                                 'autocorrect\\false_positives.csv')
                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, wrong_grammar_sentence,
                                 'autocorrect\\true_positives.csv')
                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[0],
                                 'autocorrect\\one_misspell.csv')
                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[1],
                                 'autocorrect\\two_misspells.csv')
                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[2],
                                 'autocorrect\\three_misspellscsv')
                verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[3],
                                 'autocorrect\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, correct_sentence,
                                 'gingerit\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, wrong_grammar_sentence,
                                 'gingerit\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[0],
                                 'gingerit\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[1],
                                 'gingerit\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[2],
                                 'gingerit\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[3],
                                 'gingerit\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, correct_sentence,
                                 'language_tool\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, wrong_grammar_sentence,
                                 'language_tool\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[0],
                                 'language_tool\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[1],
                                 'language_tool\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[2],
                                 'language_tool\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[3],
                                 'language_tool\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(correct_sentence),
                                 'gingerit_spellchecker\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(wrong_grammar_sentence),
                                 'gingerit_spellchecker\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[0]),
                                 'gingerit_spellchecker\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[1]),
                                 'gingerit_spellchecker\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[2]),
                                 'gingerit_spellchecker\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[3]),
                                 'gingerit_spellchecker\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(correct_sentence),
                                 'gingerit_textblob\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(wrong_grammar_sentence),
                                 'gingerit_textblob\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[0]),
                                 'gingerit_textblob\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[1]),
                                 'gingerit_textblob\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[2]),
                                 'gingerit_textblob\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[3]),
                                 'gingerit_textblob\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(correct_sentence),
                                 'gingerit_autocorrect\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(wrong_grammar_sentence),
                                 'gingerit_autocorrect\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[0]),
                                 'gingerit_autocorrect\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[1]),
                                 'gingerit_autocorrect\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[2]),
                                 'gingerit_autocorrect\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[3]),
                                 'gingerit_autocorrect\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(correct_sentence),
                                 'language_tool_spellchecker\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(wrong_grammar_sentence),
                                 'language_tool_spellchecker\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[0]),
                                 'language_tool_spellchecker\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[1]),
                                 'language_tool_spellchecker\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[2]),
                                 'language_tool_spellchecker\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_spell_checker(misspells[3]),
                                 'language_tool_spellchecker\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(correct_sentence),
                                 'language_tool_textblob\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(wrong_grammar_sentence),
                                 'language_tool_textblob\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[0]),
                                 'language_tool_textblob\\one_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[1]),
                                 'language_tool_textblob\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[2]),
                                 'language_tool_textblob\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_txt_blb(misspells[3]),
                                 'language_tool_textblob\\four_misspells.csv')

                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(correct_sentence),
                                 'language_tool_autocorrect\\false_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(wrong_grammar_sentence),
                                 'language_tool_autocorrect\\true_positives.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[0]),
                                 'language_tool_autocorrect\\one_misspell.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[1]),
                                 'language_tool_autocorrect\\two_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[2]),
                                 'language_tool_autocorrect\\three_misspells.csv')
                verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                                 Comparer.correct_spelling_autocorrect(misspells[3]),
                                 'language_tool_autocorrect\\four_misspells.csv')

                print('CZAS: ', time.time() - start_time)



