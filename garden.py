import spacy

nlp = spacy.load('en_core_web_sm')

garden_1 = "The sour drink from the ocean."
garden_2 = "Mary gave the child the dog bit a Band-Aid."
garden_3 = "That Jill is never here hurts."
garden_4 = "The man who whistles tunes pianos."
garden_5 = "Fat people eat accumulates."
garden_6 = "Helen is expecting tomorrow to be a bad day."

garden_list = [garden_1, garden_2, garden_3, garden_4, garden_5, garden_6]

def tokenize(x):
    doc = nlp(x)
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])


def entity_rec(x):
    nlp_doc = nlp(x)
    print([(i, i.label_) for i in nlp_doc.ents])


for i in garden_list:
    tokenize(i)
    entity_rec(i)

# 2 unexpected entities:

# Both occured in the "garden_6" sentence, firstly the name Helen was classified as GPE, which turned out to be a
# "Geopolitical entity", meaning a city, country or place. There are locations in the world called Helen, so this may
# be why.
# The second anomoly was found in the same string, where it classified "a bad day" as a DATE entity.  The
# expression relates to an abstract feeling or expectation, rather than a fixed day.
# The thing I found most surprised was the overall lack of recognition for most sentences, beyond identifying two names
# correctly as "PERSON" entities.

