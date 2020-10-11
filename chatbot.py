import pandas as pd
import json
from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity
from Data_preprocessing import clean_the_question_content
import pickle

def read_data():
    with open('./my_data1.json') as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    print(df.head())
    return df

def get_sentences(df):
    sentences = []
    for index, row in df.iterrows():
        sentences.append(row['question'])
    return sentences

def printAnswer(question_embedding, sentence_embedding, df, sentences, question):
    max_sim = -1
    index_sim = -1
    for index, ques_embedding in enumerate(sentence_embedding):
        sim = cosine_similarity(ques_embedding, question_embedding)[0][0]
        print(index, sim, sentences[index])
        if sim > max_sim:
            max_sim = sim
            index_sim = index

    if max_sim < 0.8:
        return("We'll get back to you soon!")
    else:
        print("\n")
        print("Question:", question)
        print("\n")
        print("Similarty:", max_sim)
        print("\n")
        print("Answer:", df.iloc[index_sim,0])
        print(df.iloc[index_sim,1])
        return(df.iloc[index_sim,1])
        

def questions_embedding_list(df):
    bc = BertClient(check_length=False)
    df_questions = get_sentences(df)
    df_question_bert_embeddings = []
    for sentence in df_questions:
        df_question_bert_embeddings.append(bc.encode([sentence]))
    
    file = open("model.pkl", "wb")
    pickle.dump(df_question_bert_embeddings, file)


def get_answer(question):
    bc = BertClient(check_length=False)
    question = clean_the_question_content(question)
    question_embedding = bc.encode([question])
    df = read_data()
    df_questions = get_sentences(df)
    
    file = open("model.pkl", 'rb')
    binary_data = file.read()
    # sio = StringIO(binary_data)
    df_question_bert_embeddings = pickle.loads(binary_data)

    Answer = printAnswer(question_embedding, df_question_bert_embeddings, df, df_questions, question)
    return Answer

if __name__ == '__main__':
    # df = read_data()
    # questions_embedding_list(df)
    text = input("Please enter your Query: ")
    get_answer(text)
