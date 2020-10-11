# NyaayaChatbot
ChatBot for laws on India using BERT embeddings. The dataset for the chatbot was prepared from the website https://nyaaya.org

## Create a environment in anaconda and install dependencies
```
conda create -n chatbot python=3.5

git clone https://github.com/mayankpruthii/NyaayaChatbot.git

cd NyaayaChatbot

pip install -r requirements.txt
```

## Start the bert service in the console
Download the model from here https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1
And place the folder in the project directory

Go to bert-server.py and replace the model_dir value to your downloaded folder's path
```
python bert-server.py
```

## Testing the bot
Open another anaconda prompt 
```
conda activate chatbot

cd NyaayaChatbot

python chatbot.py
```
It will ask you query. Ask your question and it will be answered.!


## Ask the bot Questions like

* Is gender based discrimination the same as sexual harassment?

* Can the landlord increase my rent?
