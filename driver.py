import config
import taggers

tag=taggers.tagging()

if config.tagging_model== 1:
    print("\nThe Model being used is Polyglot\n")
    tag.polyglot_tags()
elif config.tagging_model ==2:
    print("\nThe Model being used is Spacy \n")
    tag.spacy_tags()
elif config.tagging_model == 3:
    print("\nThe Model being used is NLTK \n")
    tag.nltk_tags()
else:
    print("\nPlease read the readme carefully\n")
