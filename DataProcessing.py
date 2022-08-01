import os.path

import pandas as pd
import Comparer, time, re
import MisspellGenerator


def verify_sentences(foo, template: str, test_sentence: str, result_list: list):
    start_time = time.time()
    dictionary = Comparer.Tested_Sentence(template, str(foo(test_sentence))).__dict__
    dictionary['time'] = time.time() - start_time
    result_list.append(dictionary)


sent_1, sent_2, sent_3 = 'I love apples.', 'I loves apples.', 'I love aples.'


# spellchecker_results, textblob_results, autocorrect_results, gingerit_results, language_tool, gingerit_spellchecker, gingerit_textblob, gingerit_autocorrect, language_tool_spellchecker, language_tool_textblob, language_tool_autocorrect, median = [], [], [], [], [], [], [], [], [], [], [], []


def write_pd_to_csv(path_to_file: str, list_of_dictionaries: list):
    pd.json_normalize(list_of_dictionaries).to_csv(path_to_file, mode='a+', index=False, header=False)


# true_negatives = {
#     "spellchecker": (Comparer.correct_spelling_spell_checker), "textblob": (correct_spelling_txt_blb), "autocorrect": (), "gingerit_results": (), "language_tool": (),
#     "gingerit_spellchecker": (), "gingerit_textblob": [], "gingerit_autocorrect": [],
#     "language_tool_spellchecker": (), "language_tool_textblob": (), "language_tool_autocorrect": (), "median": ()

true_positives = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

false_positives = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

one_misspell = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

two_misspells = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

three_misspells = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

four_misspells = {
    "spellchecker": [], "textblob": [], "autocorrect": [], "gingerit": [], "language_tool": [],
    "gingerit_spellchecker": [], "gingerit_textblob": [], "gingerit_autocorrect": [],
    "language_tool_spellchecker": [], "language_tool_textblob": [], "language_tool_autocorrect": []
}

file = 'grammar_incorrect\\CAN.txt'

with open(file) as file:
    while True:
        correct_sentence = file.readline()
        wrong_grammar_sentence = file.readline()
        if not correct_sentence:
            break

        else:
            correct_sentence = re.findall(r'[^\n]+', correct_sentence)[0]
            wrong_grammar_sentence = re.findall(r'[^\n]+', wrong_grammar_sentence)[0]
            misspells = [MisspellGenerator.misspell_sentence(correct_sentence, k) for k in range(1, 4)]
            print(misspells)

            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, correct_sentence,
                             false_positives['spellchecker'])
            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, wrong_grammar_sentence,
                             true_positives['spellchecker'])
            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[0],
                             one_misspell['spellchecker'])
            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[1],
                             two_misspells['spellchecker'])
            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[2],
                             three_misspells['spellchecker'])
            verify_sentences(Comparer.correct_spelling_spell_checker, correct_sentence, misspells[3],
                             four_misspells['spellchecker'])

            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, correct_sentence,
                             false_positives['textblob'])
            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, wrong_grammar_sentence,
                             true_positives['textblob'])
            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[0],
                             one_misspell['textblob'])
            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[1],
                             two_misspells['textblob'])
            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[2],
                             three_misspells['textblob'])
            verify_sentences(Comparer.correct_spelling_txt_blb, correct_sentence, misspells[3],
                             four_misspells['textblob'])

            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, correct_sentence,
                             false_positives['autocorrect'])
            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, wrong_grammar_sentence,
                             true_positives['autocorrect'])
            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[0],
                             one_misspell['autocorrect'])
            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[1],
                             two_misspells['autocorrect'])
            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[2],
                             three_misspells['autocorrect'])
            verify_sentences(Comparer.correct_spelling_autocorrect, correct_sentence, misspells[3],
                             four_misspells['autocorrect'])

            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, correct_sentence,
                             false_positives['gingerit'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, wrong_grammar_sentence,
                             true_positives['gingerit'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[0],
                             one_misspell['gingerit'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[1],
                             two_misspells['gingerit'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[2],
                             three_misspells['gingerit'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence, misspells[3],
                             four_misspells['gingerit'])

            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, correct_sentence,
                             false_positives['language_tool'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, wrong_grammar_sentence,
                             true_positives['language_tool'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[0],
                             one_misspell['language_tool'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[1],
                             two_misspells['language_tool'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[2],
                             three_misspells['language_tool'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence, misspells[3],
                             four_misspells['language_tool'])

            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(correct_sentence),
                             false_positives['gingerit_spellchecker'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(wrong_grammar_sentence),
                             true_positives['gingerit_spellchecker'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[0]),
                             one_misspell['gingerit_spellchecker'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[1]),
                             two_misspells['gingerit_spellchecker'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[2]),
                             three_misspells['gingerit_spellchecker'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[3]),
                             four_misspells['gingerit_spellchecker'])

            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(correct_sentence),
                             false_positives['gingerit_textblob'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(wrong_grammar_sentence),
                             true_positives['gingerit_textblob'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[0]),
                             one_misspell['gingerit_textblob'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[1]),
                             two_misspells['gingerit_textblob'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[2]),
                             three_misspells['gingerit_textblob'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[3]),
                             four_misspells['gingerit_textblob'])

            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(correct_sentence),
                             false_positives['gingerit_autocorrect'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(wrong_grammar_sentence),
                             true_positives['gingerit_autocorrect'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[0]),
                             one_misspell['gingerit_autocorrect'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[1]),
                             two_misspells['gingerit_autocorrect'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[2]),
                             three_misspells['gingerit_autocorrect'])
            verify_sentences(Comparer.grammar_check_gingerit, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[3]),
                             four_misspells['gingerit_autocorrect'])

            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_spell_checker(correct_sentence),
                             false_positives['language_tool_spellchecker'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_spell_checker(wrong_grammar_sentence),
                             true_positives['language_tool_spellchecker'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer .correct_spelling_spell_checker(misspells[0]),
                             one_misspell['language_tool_spellchecker'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[1]),
                             two_misspells['language_tool_spellchecker'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[2]),
                             three_misspells['language_tool_spellchecker'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_spell_checker(misspells[3]),
                             four_misspells['language_tool_spellchecker'])

            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(correct_sentence),
                             false_positives['language_tool_textblob'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(wrong_grammar_sentence),
                             true_positives['language_tool_textblob'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[0]),
                             one_misspell['language_tool_textblob'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[1]),
                             two_misspells['language_tool_textblob'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[2]),
                             three_misspells['language_tool_textblob'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_txt_blb(misspells[3]),
                             four_misspells['language_tool_textblob'])

            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(correct_sentence),
                             false_positives['language_tool_autocorrect'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(wrong_grammar_sentence),
                             true_positives['language_tool_autocorrect'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[0]),
                             one_misspell['language_tool_autocorrect'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[1]),
                             two_misspells['language_tool_autocorrect'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[2]),
                             three_misspells['language_tool_autocorrect'])
            verify_sentences(Comparer.grammar_check_language_tool, correct_sentence,
                             Comparer.correct_spelling_autocorrect(misspells[3]),
                             four_misspells['language_tool_autocorrect'])

            for k in false_positives:
                print(pd.json_normalize(false_positives[k]))
                print(pd.json_normalize(true_positives[k]))

for k in false_positives:
    print(pd.json_normalize(false_positives[k]))
    print(pd.json_normalize(true_positives[k]))

# print(true_negatives['spellchecker'])
# write_pd_to_csv('results\\spellchecker.csv', true_negatives['spellchecker'] )
