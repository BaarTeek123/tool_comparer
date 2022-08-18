import os
import Levenshtein



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
# import re
#
# import Comparer
# import DataProcessing
#
# file = 'misspells\\4_misspell.txt'
#
# variants = {
#         # self.verify_variant(correct_spelling_spell_checker, 'SpellChecker', self.sentence_to_test)
#         # self.verify_variant(correct_spelling_txt_blb, 'TextBlob', self.sentence_to_test)
#         # self.verify_variant(correct_spelling_autocorrect, 'Autocorrect', self.sentence_to_test)
#         # self.verify_variant(grammar_check_gingerit, 'GingerIt', self.sentence_to_test)
#         # self.verify_variant(grammar_check_language_tool, 'Language_tool', self.sentence_to_test)
#         # self.verify_variant(grammar_check_gingerit, 'GingerIt(SpellChecker)',
#         #                     correct_spelling_spell_checker(self.sentence_to_test))
#         # self.verify_variant(grammar_check_gingerit, 'GingerIt(TextBlob)',
#         #                     correct_spelling_txt_blb(self.sentence_to_test))
#         # self.verify_variant(grammar_check_gingerit, 'GingerIt(Autocorrect)',
#         #                     correct_spelling_autocorrect(self.sentence_to_test))
#         # self.verify_variant(grammar_check_language_tool, 'Language_tool(SpellChecker)',
#         #                     correct_spelling_spell_checker(self.sentence_to_test))
#         # self.verify_variant(grammar_check_language_tool, 'Language_tool(TextBlob)',
#         #                     correct_spelling_txt_blb(self.sentence_to_test))
#         # self.verify_variant(grammar_check_language_tool, 'Language_tool(Autocorrect)',
#         #                     correct_spelling_autocorrect(self.sentence_to_test))
#         # list_of_sentences = [str(k) for k in self.results.values() if k != 0]
#         # if len(list_of_sentences) > 0:
#         #     self.results['Median'] = Levenshtein.median_improve(Levenshtein.median(list_of_sentences),
#         #                                                         list_of_sentences)
#                                                                 }
#
# #reading files
# true_positives, false_postives = [], []
# with open(file) as file:
#     while True:
#         correct_sentence = file.readline()
#         wrong_sentence = file.readline()
#         if not correct_sentence:
#             break
#         else:
#             correct_sentence = re.findall(r'[^\n]+', correct_sentence)[0]
#             wrong_sentence = re.findall(r'[^\n]+', wrong_sentence)[0]
#             DataProcessing.verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, correct_sentence, false_postives)
#             DataProcessing.verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, wrong_sentence, true_positives)

#
#
import nordvpn_switcher
import pandas as pandas

import Comparer, matplotlib.pyplot as plt


# print(Comparer.correct_spelling_autocorrect('I mispel'))
true_positives = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

def create_dirs(directory_path, dict_of_subdirs: dict):
    for k in dict_of_subdirs.keys():
        path = directory_path + k
        os.mkdir(path)

# create_dirs('C:\\Users\\user\\PycharmProjects\\tool_comparer\\results\\', true_positives)

# nordvpn_switcher.initialize_VPN(save=1, area_input=None, skip_settings=None)
# nordvpn_switcher.rotate_VPN()
# nordvpn_switcher.rotate_VPN()

def merge_two_files (file_1_path, file_2_path, dest_path):
    with open(file_1_path) as first, open(file_2_path) as second, open(dest_path, "w+") as output:
        while 1:
            line_first = first.readline()  # line from file1 (header)
            line_second = second.readline()  # line from file2 (body)
            # print(line_first + line_second)
            output.write(line_first + line_second)
            if not (line_first and line_second):
                break

i = 0
import pandas
# files = ['Future_Continuous.Txt', 'Future_Perfect.Txt', 'Future_Simple.Txt', 'Going_To_1.Txt', 'Going_To_Pl.Txt', 'Going_To_Pl_2.Txt', 'Going_To_Sg.Txt', 'Going_To_Sg_2.Txt', 'Must.Txt', 'Ought_To.Txt', 'Passive_Future_Simple.Txt', 'Passive_Past_Perfect.Txt', 'Passive_Past_Simple_Pl.Txt', 'Passive_Past_Simple_Sg.Txt', 'Passive_Present_Continuous_Pl.Txt', 'Passive_Present_Continuous_Sg.Txt', 'Passive_Present_Perfect_3.Txt', 'Passive_Present_Perfect_Not_3.Txt', 'Past_Continuous_Pl.Txt', 'Past_Continuous_Sg.Txt', 'Past_Perfect.Txt', 'Past_Simple.Txt', 'Present_Continuous_1.Txt', 'Present_Continuous_Pl.Txt', 'Present_Continuous_Sg.Txt', 'Present_Perfect_3.Txt', 'Present_Perfect_Not_3.Txt', 'Present_Simple_3.Txt', 'Present_Simple_Not_3.Txt', 'Result_Cnt.Txt', 'Result_Unc.Txt', 'Should.Txt', 'Used_To.Txt', 'Will.Txt', 'Would.Txt']
# directory = 'grammar_incorrect'
# for file in files:
#     # print("'" + str(file.title()), end= '\', ')
#     with open(directory + '\\' + file) as file:
#         while i < 100:
#             print(i, end=' ')
#             i += 1
#     print('\n', file.name)

import datetime

# merge_two_files('uncountable_countable\\th', 'uncountable_countable\\unc_errors.txt', 'uncountable_countable\\result_these.txt')



# print(file.sheet_names[1].describe())

# print(file.sheet_names)
# print(file.parse(file.sheet_names[1]))
# directory =
# p = 1
# for excel_file_path in os.listdir(directory):
    # file = pd.ExcelFile(excel_file_path)
    # print(file.describe())
    # break

#     print(k)
#     for i in os.listdir(directory + '\\' + k):
#         print(i)
#         df = pandas.read_csv(directory + '\\' + k + '\\' + i)
#         df.reset_index()
#         df.columns = ['template', 'sentence_to_test', 'levenshtein_distance', 'jaro_winkler', 'damerau_levenshtein_distance', 'similarity', 'time']
#         if p < 33:
#             with pandas.ExcelWriter('C:\\Users\\user\\PycharmProjects\\tool_comparer\\first.xlsx', mode='a') as writer:
#                 df.to_excel(writer, sheet_name=k + ' ' + i[:-4], index=False)
#         else:
#             with pandas.ExcelWriter ('C:\\Users\\user\\PycharmProjects\\tool_comparer\\second.xlsx', mode='a') as writer:
#                 df.to_excel(writer, sheet_name=k + ' ' + i[:-4], index=False)
#         p += 1
# template = ''
# test_sentence = ''
# from Comparer import Tested_Sentence, correct_spelling_autocorrect
# dictionary = Tested_Sentence(str(template), str(correct_spelling_autocorrect(str(test_sentence)))).__dict__
# print(dictionary)
# print(dictionary.keys())
import nltk
from PhraseGenerator import get_dict_of_pos_tagged_word
print(nltk.corpus.conll2000.tagged_words())







