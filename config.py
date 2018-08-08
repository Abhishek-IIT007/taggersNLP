'''
First you need to install these:
1: Polyglot
2:Spacy
3:NLTK
download all their pretrained models.

We'll use 3 tagging module here


1: Polyglot
2: Spacy
3: NLTK

select them for tagging_model
various functions can be performed:
POS tags  (pos)
Entity recognition (ner)
Dependency parsing (dep_p) (not for nltk as it is not good and uses stanford parser)
etc.

polyglot has additional feature morphemes
#morphemes for cases where corpus is not formatted properly i.e. space between words are removed. eg "corporatebank" to "corporate" ,"bank"

You'll have to select the tagger you want .
give the location of the file/files.
the tagged text will be saved in a string which you can access for your further code


For polyglot only we can do morphemes i.e. mor
'''



tagging_model=2
type_of_tag = "pos"
file_location="D:/test.txt"
list2=[]