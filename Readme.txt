Step to run the chatbot: 
1. download the repository.
2. Locate the ChatBot.ipynb file Open it in Jupyter notebook.
3. And then run its first cell.
4. Play around with the bot.


If some error comes may be check and install following library if they are not installed.
	1.h5py
	2.numpy
	3.tensorflow
	4.json
	5.spacy
	6.nltk
	
Repository contents following files 
1. ChatBot : python code for chatbot
2. chatBot_smallTalk.h5 : it contains saved model for general talk
3. chatBotContext.h5 : it contains saved model for context specific chatbot
4. CommonIntentions : its json file which is used for context specific model computation.
5. CommonIntentions_smallTalk : its json file which is used for general talk model computation.
6. commonTalk : csv file from which common talk model is trained
7. EvaluationMetric : python code for generating evaluation metric.
8. feedback : stores sentence for re-training 
9. ProjectReport : Project Report doc file
10.LabelList : list of label for context specific model i.e. tag list 
11.LabelList_smallTalk : list of label for general talk model i.e. tag list 
12.loadingScript: for converting commonTalk csv file in json which is used for model training
13.ReadMe: which you are reading right now
14.responseDictionary: contains saved response for context specific model
15.responseDictionary_smallTalk: contains saved response for common talk model
16. test_case: for commuting evaluation metric
17. VocabularyList: json file for storing vocabulary of context specific model
18.VocabularyList_smallTalk: json file for storing vocabulary of general talk model

