import polyglot
from polyglot.text import Text
import pickle
import spacy
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
import config

class tagging():


    def polyglot_tags(self):

        with open(config.file_location, errors="ignore")as r:
            inputtext = r.read()
        tok = ""
        with open("punkttokenizer_fullcorpus.pickle", 'rb')as f:  # using our custom tokenizer
            custom_sent_tokenizer = pickle.load(f)
        tokenized = custom_sent_tokenizer.tokenize(inputtext)
        tok += str(tokenized)
        text = Text(tok)
        if config.type_of_tag =="pos":
            print("\nPos tags using Polyglot\n")
            print(text.pos_tags)

        elif config.type_of_tag =="ner":
            print("\nNER tags using Polyglot\n")
            print(text.entities)
        elif config.type_of_tag =="mor":
            print("\nMorphemes using using Polyglot\n")
            # morphemes for cases where corpus is not formatted properly i.e. space between words are removed. eg "corporatebank" to "corporate" ,"bank"
            print(text.morphemes)
        else :
            print("\n Please provide correct value to type_of_tag. Refer to the instructions\n")



    def spacy_tags(self):

        nlp = spacy.load('en_core_web_sm')

        with open(config.file_location)as f:  # open the text files to be tagged
            text = f.read()
        doc = nlp(text)
        # for pos tagging
        if config.type_of_tag=="pos":
            print("\nPOS tags using SPACY\n")
            for token in doc:
                print(token.text,  token.pos_, token.tag_ )

        # for entity recognition
        elif config.type_of_tag=="ner":
            print("\nNER tags using SPACY\n")
            for ent in doc.ents:
                print(ent.text, ent.start_char, ent.end_char, ent.label_)

        # for dependency parsing
        elif config.type_of_tag=="dep_p":
            print("\ndependency parsing using SPACY\n")
            for chunk in doc.noun_chunks:
                print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
        else:
            print("\n Please provide correct value to type_of_tag. Refer to the instructions\n")

    def nltk_tags(self):
        with open("punkttokenizer_fullcorpus.pickle", 'rb')as f:  # using our custom tokenizer
            custom_sent_tokenizer = pickle.load(f)
        with open(config.file_location, errors="ignore")as r:
            inputtext = r.read()
        tokenized = custom_sent_tokenizer(inputtext)

        if config.type_of_tag=="pos":
            print("\nPOS tags using NLTK\n")

            def process_content():
                try:
                    for i in tokenized:
                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        print(tagged)

                except Exception as e:
                    print(str(e), 'error')

            process_content()

        # for entity recognition

        elif config.type_of_tag=="ner":
            print("\nNER tags using NLTK\n")
            for sentence in tokenized():
                print(ne_chunk(pos_tag(word_tokenize(sentence))))

        else:
            print("\n Please provide correct value to type_of_tag. Refer to the instructions\n")


