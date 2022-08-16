import gc
import os.path

import nordvpn_switcher
import pandas as pd
import psutil
import time
from re import findall
from MisspellGenerator import misspell_sentence
from Comparer import correct_spelling_autocorrect, correct_spelling_spell_checker, correct_spelling_txt_blb, \
    grammar_check_gingerit, grammar_check_language_tool, Tested_Sentence
import objgraph, datetime


def print_info(if_all=False):
    if if_all:
        print(3 * '\n')
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(objgraph.show_growth(limit=10))
    print('vars', vars())
    print('locals', locals())
    print('globals', globals())
    print('dir', dir())
    if if_all:
        print(3 * '\n')


def verify_sentences(foo, template: str, test_sentence: str, path_to_file: str):
    start_time = time.time()
    dictionary = Tested_Sentence(str(template), str(foo(str(test_sentence)))).__dict__
    dictionary['time'] = time.time() - start_time
    pd.json_normalize(dictionary).to_csv('results\\' + path_to_file, mode='a+', index=False, header=False)
    del dictionary, start_time, path_to_file, test_sentence, template, foo


def get_date():
    YEAR = str(datetime.date.today().year)  # the current year
    MONTH = str(datetime.date.today().month)  # the current month
    DATE = str(datetime.date.today().day)  # the current day
    HOUR = str(datetime.datetime.now().hour)  # the current hour
    MINUTE = str(datetime.datetime.now().minute)  # the current minute
    SECONDS = str(datetime.datetime.now().second)  # the current second
    return f'{YEAR}-{MONTH}-{DATE}\t{HOUR}:{MINUTE}:{SECONDS}'


# spellchecker_results, textblob_results, autocorrect_results, gingerit_results, language_tool, gingerit_spellchecker, gingerit_textblob, gingerit_autocorrect, language_tool_spellchecker, language_tool_textblob, language_tool_autocorrect, median = [], [], [], [], [], [], [], [], [], [], [], []


# def write_pd_to_csv(path_to_file: str, list_of_dictionaries: list):
#     pd.json_normalize(list_of_dictionaries).to_csv(path_to_file, mode='a+', index=False, header=False)


# def clear_memory():
#     for name in dir():
#         if not name.startswith('_'):
#             del globals()[name]


directory = 'grammar_incorrect'
# nordvpn_switcher.initialize_VPN(save=1, area_input=None, skip_settings=None)
# nordvpn_switcher.rotate_VPN()
x = True
while x:
    try:
        for k in os.listdir(directory):
            i = 0
            with open(directory + '\\' + k) as file:
                while i < 50:
                    correct_sentence = file.readline()
                    wrong_grammar_sentence = file.readline()
                    start = time.time()
                    correct_sentence = findall(r'[^\n]+', correct_sentence)[0]
                    if len(wrong_grammar_sentence) > 1:
                        wrong_grammar_sentence = findall(r'[^\n]+', wrong_grammar_sentence)[0]
                    misspells = [misspell_sentence(correct_sentence, k) for k in range(1, 5)]

                    # verify_sentences(correct_spelling_spell_checker, correct_sentence, correct_sentence,
                    #                  'spellchecker\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(correct_spelling_spell_checker, correct_sentence, wrong_grammar_sentence,
                    #                      'spellchecker\\true_positives.csv')
                    # verify_sentences(correct_spelling_spell_checker, correct_sentence, misspells[0],
                    #                  'spellchecker\\one_misspell.csv')
                    # verify_sentences(correct_spelling_spell_checker, correct_sentence, misspells[1],
                    #                  'spellchecker\\two_misspells.csv')
                    # verify_sentences(correct_spelling_spell_checker, correct_sentence, misspells[2],
                    #                  'spellchecker\\three_misspells.csv')
                    # verify_sentences(correct_spelling_spell_checker, correct_sentence, misspells[3],
                    #                  'spellchecker\\four_misspells.csv')
                    #
                    # verify_sentences(correct_spelling_txt_blb, correct_sentence, correct_sentence,
                    #                  'textblob\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(correct_spelling_txt_blb, correct_sentence, wrong_grammar_sentence,
                    #                      'textblob\\true_positives.csv')
                    # verify_sentences(correct_spelling_txt_blb, correct_sentence, misspells[0],
                    #                  'textblob\\one_misspell.csv')
                    # verify_sentences(correct_spelling_txt_blb, correct_sentence, misspells[1],
                    #                  'textblob\\two_misspells.csv')
                    # verify_sentences(correct_spelling_txt_blb, correct_sentence, misspells[2],
                    #                  'textblob\\three_misspells.csv')
                    # verify_sentences(correct_spelling_txt_blb, correct_sentence, misspells[3],
                    #                  'textblob\\four_misspells.csv')
                    #
                    # verify_sentences(correct_spelling_autocorrect, correct_sentence, correct_sentence,
                    #                  'autocorrect\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(correct_spelling_autocorrect, correct_sentence, wrong_grammar_sentence,
                    #                      'autocorrect\\true_positives.csv')
                    # verify_sentences(correct_spelling_autocorrect, correct_sentence, misspells[0],
                    #                  'autocorrect\\one_misspell.csv')
                    # verify_sentences(correct_spelling_autocorrect, correct_sentence, misspells[1],
                    #                  'autocorrect\\two_misspells.csv')
                    # verify_sentences(correct_spelling_autocorrect, correct_sentence, misspells[2],
                    #                  'autocorrect\\three_misspellscsv')
                    # verify_sentences(correct_spelling_autocorrect, correct_sentence, misspells[3],
                    #                  'autocorrect\\four_misspells.csv')

                    # verify_sentences(grammar_check_gingerit, correct_sentence, correct_sentence,
                    #                  'gingerit\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_gingerit, correct_sentence, wrong_grammar_sentence,
                    #                      'gingerit\\true_positives.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence, misspells[0],
                    #                  'gingerit\\one_misspell.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence, misspells[1],
                    #                  'gingerit\\two_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence, misspells[2],
                    #                  'gingerit\\three_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence, misspells[3],
                    #                  'gingerit\\four_misspells.csv')
                    #
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_spell_checker(correct_sentence),
                    #                  'gingerit_spellchecker\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                      correct_spelling_spell_checker(wrong_grammar_sentence),
                    #                      'gingerit_spellchecker\\true_positives.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[0]),
                    #                  'gingerit_spellchecker\\one_misspell.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[1]),
                    #                  'gingerit_spellchecker\\two_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[2]),
                    #                  'gingerit_spellchecker\\three_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[3]),
                    #                  'gingerit_spellchecker\\four_misspells.csv')

                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_txt_blb(correct_sentence),
                    #                  'gingerit_textblob\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                      correct_spelling_txt_blb(wrong_grammar_sentence),
                    #                      'gingerit_textblob\\true_positives.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_txt_blb(misspells[0]),
                    #                  'gingerit_textblob\\one_misspell.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_txt_blb(misspells[1]),
                    #                  'gingerit_textblob\\two_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_txt_blb(misspells[2]),
                    #                  'gingerit_textblob\\three_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_txt_blb(misspells[3]),
                    #                  'gingerit_textblob\\four_misspells.csv')
                    # # #
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_autocorrect(correct_sentence),
                    #                  'gingerit_autocorrect\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                      correct_spelling_autocorrect(wrong_grammar_sentence),
                    #                      'gingerit_autocorrect\\true_positives.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,correct_spelling_autocorrect(misspells[0]),
                    #                  'gingerit_autocorrect\\one_misspell.csv'), correct_spelling_autocorrect(misspells[1]),
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_autocorrect(misspells[1]),
                    #                  'gingerit_autocorrect\\two_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_autocorrect(misspells[2]),
                    #                  'gingerit_autocorrect\\three_misspells.csv')
                    # verify_sentences(grammar_check_gingerit, correct_sentence,
                    #                  correct_spelling_autocorrect(misspells[3]),
                    #                  'gingerit_autocorrect\\four_misspells.csv')


                    # verify_sentences(grammar_check_language_tool, correct_sentence, correct_sentence,
                    #                  'language_tool\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_language_tool, correct_sentence, wrong_grammar_sentence,
                    #                      'language_tool\\true_positives.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence, misspells[0],
                    #                  'language_tool\\one_misspell.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence, misspells[1],
                    #                  'language_tool\\two_misspells.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence, misspells[2],
                    #                  'language_tool\\three_misspells.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence, misspells[3],
                    #                  'language_tool\\four_misspells.csv')
                    #
                    # verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                  correct_spelling_spell_checker(correct_sentence),
                    #                  'language_tool_spellchecker\\false_positives.csv')
                    # if len(wrong_grammar_sentence) > 1:
                    #     verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                      correct_spelling_spell_checker(wrong_grammar_sentence),
                    #                      'language_tool_spellchecker\\true_positives.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[0]),
                    #                  'language_tool_spellchecker\\one_misspell.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[1]),
                    #                  'language_tool_spellchecker\\two_misspells.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[2]),
                    #                  'language_tool_spellchecker\\three_misspells.csv')
                    # verify_sentences(grammar_check_language_tool, correct_sentence,
                    #                  correct_spelling_spell_checker(misspells[3]),
                    #                  'language_tool_spellchecker\\four_misspells.csv')
                    #
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_txt_blb(correct_sentence),
                                     'language_tool_textblob\\false_positives.csv')
                    if len(wrong_grammar_sentence) > 1:
                        verify_sentences(grammar_check_language_tool, correct_sentence,
                                         correct_spelling_txt_blb(wrong_grammar_sentence),
                                         'language_tool_textblob\\true_positives.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_txt_blb(misspells[0]),
                                     'language_tool_textblob\\one_misspells.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_txt_blb(misspells[1]),
                                     'language_tool_textblob\\two_misspells.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_txt_blb(misspells[2]),
                                     'language_tool_textblob\\three_misspells.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_txt_blb(misspells[3]),
                                     'language_tool_textblob\\four_misspells.csv')

                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_autocorrect(correct_sentence),
                                     'language_tool_autocorrect\\false_positives.csv')
                    if len(wrong_grammar_sentence) > 1:
                        verify_sentences(grammar_check_language_tool, correct_sentence,
                                         correct_spelling_autocorrect(wrong_grammar_sentence),
                                         'language_tool_autocorrect\\true_positives.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_autocorrect(misspells[0]),
                                     'language_tool_autocorrect\\one_misspell.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_autocorrect(misspells[1]),
                                     'language_tool_autocorrect\\two_misspells.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_autocorrect(misspells[2]),
                                     'language_tool_autocorrect\\three_misspells.csv')
                    verify_sentences(grammar_check_language_tool, correct_sentence,
                                     correct_spelling_autocorrect(misspells[3]),
                                     'language_tool_autocorrect\\four_misspells.csv')
                    i += 1
                    print_info(True)
                    gc.collect()
                    del correct_sentence, wrong_grammar_sentence
                    print_info(True)
        x = False



    except Exception as exc:
        pass
    # finally: x = False
    # with open('results\\logs.txt', mode='a+') as log_file:
    #     log_file.write(str(get_date()) + '\t' + str(exc))
    #     log_file.write(str(exc.args))
    #     log_file.write(str('\n'))

# finally: pass
'''
x = True
while x:
    try:
        for k in os.listdir(directory):
            i = 0
            with open(directory + '\\' + k) as file:
                while i < 50:
                    correct_sentence = file.readline()
                    wrong_grammar_sentence = file.readline()
                    start = time.time()
                    correct_sentence = findall(r'[^\n]+', correct_sentence)[0]
                    if len(wrong_grammar_sentence) > 1:
                        wrong_grammar_sentence = findall(r'[^\n]+', wrong_grammar_sentence)[0]
                    misspells = [misspell_sentence(correct_sentence, k) for k in range(1, 5)]
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_txt_blb(correct_sentence),
                                     'gingerit_textblob\\false_positives.csv')
                    if len(wrong_grammar_sentence) > 1:
                        verify_sentences(grammar_check_gingerit, correct_sentence,
                                         correct_spelling_txt_blb(wrong_grammar_sentence),
                                         'gingerit_textblob\\true_positives.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_txt_blb(misspells[0]),
                                     'gingerit_textblob\\one_misspell.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_txt_blb(misspells[1]),
                                     'gingerit_textblob\\two_misspells.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_txt_blb(misspells[2]),
                                     'gingerit_textblob\\three_misspells.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_txt_blb(misspells[3]),
                                     'gingerit_textblob\\four_misspells.csv')
                    # #
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_autocorrect(correct_sentence),
                                     'gingerit_autocorrect\\false_positives.csv')
                    if len(wrong_grammar_sentence) > 1:
                        verify_sentences(grammar_check_gingerit, correct_sentence,
                                         correct_spelling_autocorrect(wrong_grammar_sentence),
                                         'gingerit_autocorrect\\true_positives.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     'gingerit_autocorrect\\one_misspell.csv'), correct_spelling_autocorrect(misspells[1]),
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_autocorrect(misspells[1]),
                                     'gingerit_autocorrect\\two_misspells.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_autocorrect(misspells[2]),
                                     'gingerit_autocorrect\\three_misspells.csv')
                    verify_sentences(grammar_check_gingerit, correct_sentence,
                                     correct_spelling_autocorrect(misspells[3]),
                                     'gingerit_autocorrect\\four_misspells.csv')



    except Exception as exc:
        pass
    finally: x = False
'''
