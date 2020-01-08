import csv
import json
import spacy

spacy_nlp = spacy.load('en_core_web_sm')
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
customize_stop_words = ['.', '?','!']
for w in customize_stop_words:
    spacy_nlp.vocab[w].is_stop = True


class TagSet:
   
    intent={}
    
    def __init__(self,tag,pattern,response):
        self.dict = {}
        self.dict['tag'] = response
        self.dict['patterns']=[]
        self.dict['responses']=[]
        self.dict['patterns'].append(pattern)
        self.dict['responses'].append(response)
        TagSet.intent[response]=self.dict
    

with open('CommonTalk.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    for row in readCSV:
        
        doc = spacy_nlp(row[0])
        lemmaList = [token.lemma_ for token in doc if not token.is_stop]
        print('lemmas',lemmaList)        
        
        if len(lemmaList)>0:
        
            if row[1] in TagSet.intent.keys():
                dict = TagSet.intent[row[1]]

                dict['patterns'].append(row[0])
                TagSet.intent[row[1]] = dict
            else:
                TagSet(row[1],row[0],row[1])
    
globalDict = {'intent':[]}

for key,value in TagSet.intent.items():
    globalDict['intent'].append(value)
        
        
    with open('CommonIntentions_smallTalk.json', 'w') as fl:
        json.dump(globalDict, fl)
    