import os, json, nltk, re
# spell checkers
import time

from spellchecker import SpellChecker
from autocorrect import Speller
import textblob

import Levenshtein
# grmma
from gingerit.gingerit import GingerIt
import language_tool_python

import itertools


class Distances:
    def __init__(self, str_1, str_2):
        self.__word_1 = str_1
        self.__word_2 = str_2
        # self.type_of_damerau_lev_operations = {"insert": 0,
        #                                        "replace": 0,
        #                                        "delete": 0,
        #                                        "transpose": 0}
        # self.type_of_lev_operations = {"insert": 0,
        #                                "replace": 0,
        #                                "delete": 0}
        self.levenshtein_distance = Levenshtein.distance(str_1, str_2)
        self.jaro_winkler = Levenshtein.jaro_winkler(self.__word_1, self.__word_2)
        # self.__set_operations()
        self.damerau_levenshtein_distance = len(self.get_string_oprations())
        self.similarity = Levenshtein.ratio(self.__word_1, self.__word_2)

    def __str__(self):
        return f'1. {self.__word_1} \n2. {self.__word_2}\n\t-D-L distance: {self.damerau_levenshtein_distance}' \
               f'\n\t\tD-L distance operations: {self.type_of_damerau_lev_operations}\n\t-L distance: ' \
               f'{self.levenshtein_distance}\n\t\t-L distance operations: {self.type_of_lev_operations}'

    def __set_operations(self):
        for operation in Levenshtein.editops(self.__word_1, self.__word_2):
            self.type_of_lev_operations[operation[0]] += 1
        for operation in self.get_string_oprations(is_damerau=True):
            self.type_of_damerau_lev_operations[operation[0]] += 1

    def get_string_oprations(self, is_damerau=True):
        dist_matrix = self.__get_damerau_levenshtein_distance_matrix(is_damerau=is_damerau)
        i, j = len(dist_matrix), len(dist_matrix[0])
        i -= 1
        j -= 1
        operations_list = []
        while i != -1 and j != -1:
            if is_damerau and i > 1 and j > 1 and self.__word_1[i - 1] == self.__word_2[j - 2] and self.__word_1[i - 2] \
                    == self.__word_2[j - 1]:
                if dist_matrix[i - 2][j - 2] < dist_matrix[i][j]:
                    operations_list.insert(0, ('transpose', i - 1, i - 2))
                    i -= 2
                    j -= 2
                    continue
            tmp = [dist_matrix[i - 1][j - 1], dist_matrix[i][j - 1], dist_matrix[i - 1][j]]
            index = tmp.index(min(tmp))
            if index == 0:
                if dist_matrix[i][j] > dist_matrix[i - 1][j - 1]:
                    operations_list.insert(0, ('replace', i - 1, j - 1))
                i -= 1
                j -= 1
            elif index == 1:
                operations_list.insert(0, ('insert', i - 1, j - 1))
                j -= 1
            elif index == 2:
                operations_list.insert(0, ('delete', i - 1, i - 1))
                i -= 1
        return operations_list

    def __get_damerau_levenshtein_distance_matrix(self, is_damerau=False):
        distance_matrix = [[0 for _ in range(len(self.__word_2) + 1)] for _ in range(len(self.__word_1) + 1)]
        for i in range(len(self.__word_1) + 1):
            distance_matrix[i][0] = i
        for j in range(len(self.__word_2) + 1):
            distance_matrix[0][j] = j
        for i in range(len(self.__word_1)):
            for j in range(len(self.__word_2)):
                if self.__word_1[i] == self.__word_2[j]:
                    cost = 0
                else:
                    cost = 1
                distance_matrix[i + 1][j + 1] = min(distance_matrix[i][j + 1] + 1,  # insert
                                                    distance_matrix[i + 1][j] + 1,  # delete
                                                    distance_matrix[i][j] + cost)  # replace
                if is_damerau:
                    if i and j and self.__word_1[i] == self.__word_2[j - 1] and self.__word_1[i - 1] == self.__word_2[
                        j]:
                        distance_matrix[i + 1][j + 1] = min(distance_matrix[i + 1][j + 1],
                                                            distance_matrix[i - 1][j - 1] + cost)  # transpose
        return distance_matrix


def save_punctuation(sentence: str):
    pass


def correct_spelling_spell_checker(word_or_list_of_words='') -> str:
    """ A function which returns corrected spelling (by SpellChecker)"""
    if isinstance(word_or_list_of_words, list):
        return " ".join([SpellChecker().correction((word)) for word in word_or_list_of_words])
    elif isinstance(word_or_list_of_words, str) and re.compile(r'[^\s]').search(word_or_list_of_words):
        return SpellChecker().correction(word_or_list_of_words)

    # if isinstance(word_or_list_of_words, str) and ' ' not in word_or_list_of_words and len(word_or_list_of_words) > 1:
    #     return str(SpellChecker().correction(word_or_list_of_words.lower()))
    # elif isinstance(word_or_list_of_words, list):
    #     return [SpellChecker().correction(word.lower()) for word in
    #             list(filter(lambda x: len(x) > 1, word_or_list_of_words))]


def correct_spelling_autocorrect(sentence: str) -> str:
    """ A function which returns corrected spelling (by Speller from autocorrect)"""
    return Speller()(sentence)


def correct_spelling_txt_blb(sentence) -> str:
    """ A function which returns corrected spelling (by TextBlob)"""
    return textblob.TextBlob(sentence).correct()


def get_pos_for_word(word: str) -> str:
    """ Method that returns a POS tag for lemmatization """
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": nltk.corpus.wordnet.ADJ,
                "N": nltk.corpus.wordnet.NOUN,
                "V": nltk.corpus.wordnet.VERB,
                "R": nltk.corpus.wordnet.ADV}
    return tag_dict.get(tag, nltk.corpus.wordnet.NOUN)


def lemmatize_word(word: str) -> str:
    return nltk.stem.WordNetLemmatizer().lemmatize(word, get_pos_for_word(word))


def grammar_check_gingerit(sentence: str) -> str:
    return GingerIt().parse(sentence)['result']


def grammar_check_language_tool(sentence: str) -> str:
    return language_tool_python.LanguageTool('en-US').correct(sentence)


class Word:
    def __init__(self, word: str, correct_word: str):
        self.original_word = word
        self.lemmatized_word = lemmatize_word(word)
        if correct_word != word:
            self.corrected_word = correct_word

    def __str__(self):
        if self.corrected_word:
            return f'{self.original_word} coorected tp: {self.corrected_word}'
        else:
            return f'{self.original_word} is correct.'


class Tested_Sentence:
    def __init__(self, template_sentence, test_sent: str):
        self.template = template_sentence
        self.sentence_to_test = test_sent
        self.results = {}
        self.verify_variant(correct_spelling_spell_checker, 'SpellChecker', self.sentence_to_test)
        self.verify_variant(correct_spelling_txt_blb, 'TextBlob', self.sentence_to_test)
        self.verify_variant(correct_spelling_autocorrect, 'Autocorrect', self.sentence_to_test)
        self.verify_variant(grammar_check_gingerit, 'GingerIt', self.sentence_to_test)
        self.verify_variant(grammar_check_language_tool, 'Language_tool', self.sentence_to_test)
        self.verify_variant(grammar_check_gingerit, 'GingerIt(SpellChecker)',
                            correct_spelling_spell_checker(self.sentence_to_test))
        self.verify_variant(grammar_check_gingerit, 'GingerIt(TextBlob)',
                            correct_spelling_txt_blb(self.sentence_to_test))
        self.verify_variant(grammar_check_gingerit, 'GingerIt(Autocorrect)',
                            correct_spelling_autocorrect(self.sentence_to_test))
        self.verify_variant(grammar_check_language_tool, 'Language_tool(SpellChecker)',
                            correct_spelling_spell_checker(self.sentence_to_test))
        self.verify_variant(grammar_check_language_tool, 'Language_tool(TextBlob)',
                            correct_spelling_txt_blb(self.sentence_to_test))
        self.verify_variant(grammar_check_language_tool, 'Language_tool(Autocorrect)',
                            correct_spelling_autocorrect(self.sentence_to_test))
        list_of_sentences = [str(k) for k in self.results.values() if k != 0]
        if len(list_of_sentences) > 0:
            self.results['Median'] = Levenshtein.median_improve(Levenshtein.median(list_of_sentences),
                                                                list_of_sentences)

    def __str__(self):
        tmp = ''
        for k in self.results.keys():
            tmp += f'{k}: {self.results[k]}\n'
        return 'Template: ' + str(self.template) + '\n sentence to check: ' + self.sentence_to_test + '\n' + tmp

    def verify_variant(self, variant_foo, label: str, sentence):
        start_time = time.time()
        if variant_foo(sentence) != self.template:
            self.results[label] = (variant_foo(sentence), Distances(variant_foo(sentence), self.template),
                                   time.time() - start_time)


def object_to_dicts(objct):
    if isinstance(objct, dict):
        return {k: object_to_dicts(v) for k, v in objct.items()}
    elif not isinstance(objct, str) and hasattr(objct, "__iter__"):
        return [object_to_dicts(v) for v in objct]
    elif hasattr(objct, "_ast"):
        return object_to_dicts(objct._ast())
    elif hasattr(objct, "__dict__"):
        return {
            key: object_to_dicts(value)
            for key, value in objct.__dict__.items()
            if not callable(value) and not key.startswith('_')
        }
    else:
        return objct


def read_json_file(path_to_file):
    with open(path_to_file, 'r') as f:
        data = json.load(f)
    return data


def write_object_to_json_file(path_to_file, key, main_dictionary):
    if os.path.isfile(path_to_file) and os.path.getsize(path_to_file) > 0:
        # open file
        data = read_json_file(path_to_file)
        # clear file
        open(path_to_file, 'w').close()
        # add data
        file = open(path_to_file, 'a+')
        data[key].append(main_dictionary)
        file.seek(0)
        json.dump(data, file, indent=4)
    else:
        file = open(path_to_file, 'w+')
        tmp = {key: [main_dictionary]}
        json.dump(tmp, file, indent=4)
    file.close()


def add_simple_dict_to_json_file(path_to_file, key, dict_obj):
    # check if is empty
    if os.path.isfile(path_to_file) and os.path.getsize(path_to_file) > 0:
        data = read_json_file(path_to_file)
        print(data)
        print(type(data['Sentence']))
        open(path_to_file, 'w').close()
        file = open(path_to_file, 'a+')
        if isinstance(dict_obj, dict) and dict_obj.keys():
            if key in data.keys():
                for k in dict_obj.keys():
                    if k not in data[key].keys():
                        data[key][k] = dict_obj[k]
                    elif k in data[key].keys() and (isinstance(data[key][k], int) or isinstance(data[key][k], float)):
                        data[key][k] += dict_obj[k]
            else:
                data[key] = dict_obj
        json.dump(data, file, indent=4)
        file.close()


def check_sentences(source_txt_file_path: str, destination_file_path: str):
    i = 0
    if os.path.isfile(source_txt_file_path) and os.path.getsize(source_txt_file_path) > 0:
        with open(source_txt_file_path) as file:
            for correct_sent, incorrect_sent in itertools.zip_longest(*[file] * 2):
                i += 1


sent_1, sent_2 = 'I love apples.', 'I loves aples.'
print(Tested_Sentence(sent_1, sent_2))

# import pandas as pd
#
# def write_to_pandas_frame():
#     columns = []