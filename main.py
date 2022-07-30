import Levenshtein

import Comparer

sent_1, sent_2 = 'I loves aples.', 'I love apples.'
print(Levenshtein.ratio(sent_2, sent_1))
print(Comparer.Distances(sent_1, sent_2).get_attributes())

# test_sentence = Comparer.Tested_Sentence(sent_1, sent_2)
# print(test_sentence)
# print(test_sentence)
# print(test_sentence.__dict__)
# print(Comparer.object_to_dicts(test_sentence))
# columns = [
#
#
#
#
# ]
# object = None
# index = [test_sentence.template]
# def get_attributes(obj):
#     return [name for name in dir(obj) if not name.startswith('_')]
# print(Comparer.Distances(sent_2, sent_1).get_attributes())


