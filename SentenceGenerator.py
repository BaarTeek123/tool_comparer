import random

from pattern3.text.en import conjugate, lemma, lexeme, PRESENT, SG, pluralize, referenced
import PhraseGenerator


def fill_verb_subject_rule(verb_inf):
    verb_forms = lexeme(verb_inf)
    # situation when past tense form is the same as past participle form.
    if len(verb_forms) == 4:
        verb_forms.append(verb_forms[-1])
        # key -> construct name
        # value -> tuple ( subject, correct verb form, incorrect verb form)
    return {'Present_Simple_Not_3': ('NP_Not_3', verb_forms[0], verb_forms[1]),
            'Present_Simple_3': ('NP_3', verb_forms[1], verb_forms[0]),
            'Present_Continuous_1': ('I', 'am ' + verb_forms[2], 'is ' + verb_forms[2]),
            'Present_Continuous_SG': ('NP_SG', 'is ' + verb_forms[2], 'are ' + verb_forms[2]),
            'Present_Continuous_PL': ('NP_PL', 'are ' + verb_forms[2], 'is ' + verb_forms[2]),
            'Present_Perfect_Not_3': ('NP_Not_3', 'have ' + verb_forms[4], 'has ' + verb_forms[4]),
            'Present_Perfect_3': ('NP_3', 'has ' + verb_forms[4], 'have ' + verb_forms[4]),
            'Past_Simple': ('NP', verb_forms[3], None),
            'Past_Continuous_SG': ('NP_SG', 'was ' + verb_forms[2], 'were ' + verb_forms[2]),
            'Past_Continuous_PL': ('NP_PL', 'were ' + verb_forms[2], 'was ' + verb_forms[2]),
            'Past_Perfect': ('NP', 'had ' + verb_forms[4], 'had ' + verb_forms[0]),
            'Future_Simple': ('NP', 'will ' + verb_forms[0], 'will ' + verb_forms[1]),
            'Future_Continuous': ('NP', 'will be ' + verb_forms[2], 'will be ' + verb_forms[1]),
            'Future_Perfect': ('NP', 'will have ' + verb_forms[4], 'will have ' + verb_forms[0]),
            'Passive_Present_Continuous_SG': ('NP_SG', 'is being ' + verb_forms[0], 'is being ' + verb_forms[1]),
            'Passive_Present_Continuous_PL': ('NP_PL', 'are being ' + verb_forms[0], 'ought to ' + verb_forms[1]),
            'Passive_Present_Perfect_Not_3': ('NP_Not_3', 'have been ' + verb_forms[4], None),
            'Passive_Present_Perfect_3': ('NP_3', 'has been ' + verb_forms[4], None),
            'Passive_Past_Simple_SG': ('NP_SG', 'was ' + verb_forms[4], 'was ' + verb_forms[0]),
            'Passive_Past_Simple_PL': ('NP_PL', 'were ' + verb_forms[4], 'were ' + verb_forms[0]),
            'Passive_Past_Perfect': ('NP', 'had been ' + verb_forms[4], None),
            'Passive_Future_Simple': ('NP', 'will be ' + verb_forms[4], 'will be ' + verb_forms[1]),
            'CAN': ('NP', 'can ' + verb_forms[0], 'can ' + verb_forms[1]),
            'COULD': ('NP', 'could ' + verb_forms[0], 'could ' + verb_forms[1]),
            'WILL': ('NP', 'will ' + verb_forms[0], 'will ' + verb_forms[1]),
            'MUST': ('NP', 'must ' + verb_forms[0], 'must ' + verb_forms[1]),
            'WOULD': ('NP', 'would ' + verb_forms[0], 'would ' + verb_forms[1]),
            'SHOULD': ('NP', 'should ' + verb_forms[0], 'should ' + verb_forms[1]),
            'OUGHT_TO': ('NP', 'ought to' + verb_forms[0], 'ought to ' + verb_forms[1]),
            'USED_TO': ('NP', 'used to ' + verb_forms[0], 'used to ' + verb_forms[1]),
            'GOING_TO_1': ('I', 'am going to ' + verb_forms[0], 'am going to ' + verb_forms[1]),
            'GOING_TO_SG': ('NP_SG', 'is go ing to ' + verb_forms[0], 'is going to ' + verb_forms[1]),
            'GOING_TO_PL': ('NP_PL', 'are going to ' + verb_forms[0], 'are going to ' + verb_forms[1]),
            'GOING_TO_SG_2': ('NP_SG', 'is going to ' + verb_forms[0], 'are going to ' + verb_forms[0]),
            'GOING_TO_PL_2': ('NP_PL', 'are going to ' + verb_forms[0], 'is going to ' + verb_forms[0]),
            }


# def generate_sentence(subject, correct_verb_phrase,incorrect_verb_phrase, noun_phrase):

# verbs_inf = PhraseGenerator.PhraseGenerator('VB').generate_phrase(1000000)


def generate_sentences(subject_tag: str, correct_verb_phrase: str, incorrect_verb_phrase: str, *args: str,
                       amount_of_elements: int = 1000):
    dictionary, rest_of_sent = {}, ''
    sub = PhraseGenerator.PhraseGenerator(subject_tag).generate_phrase(amount_of_elements)
    for tag in args:
        dictionary[tag] = PhraseGenerator.PhraseGenerator(tag).generate_phrase(amount_of_elements)
    sub_id = random.randint(0, len(sub) - 1)
    for k in dictionary.keys():
        rest_of_sent += (' ' + dictionary[k][random.randint(0, len(dictionary[k]) - 1)])
    yield PhraseGenerator.Sentence(sub[sub_id], correct_verb_phrase, rest_of_sent)
    if incorrect_verb_phrase is not None:
        yield PhraseGenerator.Sentence(sub[sub_id], incorrect_verb_phrase, rest_of_sent)
    else:
        yield '\n'
    # return PhraseGenerator.Sentence(sub[id], correct_verb_phrase, rest_of_sent), PhraseGenerator.Sentence(sub[id], incorrect_verb_phrase, rest_of_sent)


print(PhraseGenerator.PhraseGenerator('VBP').grammar_rules)

try:
    for verb in PhraseGenerator.PhraseGenerator('VB').generate_phrase(10000):
        for key in fill_verb_subject_rule(verb):
            for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0], fill_verb_subject_rule(verb)[key][1],
                                           fill_verb_subject_rule(verb)[key][2], 'RB'):
                with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                    f.write(str(sent))
                    if sent != '\n':
                        f.write('\n')
            for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0], fill_verb_subject_rule(verb)[key][1],
                                           fill_verb_subject_rule(verb)[key][2], 'JJ'):
                with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                    f.write(str(sent))
                    if sent != '\n':
                        f.write('\n')
            for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0], fill_verb_subject_rule(verb)[key][1],
                                           fill_verb_subject_rule(verb)[key][2], 'PP'):
                with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                    f.write(str(sent))
                    if sent != '\n':
                        f.write('\n')
            for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0], fill_verb_subject_rule(verb)[key][1],
                                           fill_verb_subject_rule(verb)[key][2], 'Det Adj NP'):
                with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                    f.write(str(sent))
                    f.write('\n')
except:
    pass
