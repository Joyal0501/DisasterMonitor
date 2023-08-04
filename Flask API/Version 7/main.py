# main.py
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from db import get, update, data

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def get_main():
    return get()

@app.route('/map', methods=['POST'])
@cross_origin()
def get_latlong():
    City = request.form.get('city')
    return data(City)

@app.route('/tweet', methods=['POST'])
def Check_tweet():

    import pickle
    import pandas as pd
    import scipy
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB

    import nltk
    nltk.download('wordnet')
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer


    with open('finalized_model.pkl', 'rb') as f:
        mnb, tfidf = pickle.load(f)

    Tweet = request.form.get('tweet')
    d = {'Tweet': [Tweet]}
    input_query = pd.DataFrame(data=d)

    def lem_word(x):
        return [lem.lemmatize(w) for w in x]

    def remove_stopwords(text):
        words = [w for w in text if w not in stopwords.words('english')]
        return words

    def combine_text(list_of_text):
        combined_text = ' '.join(list_of_text)
        return combined_text

    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    input_query["Tweet"] = input_query["Tweet"].apply(lambda x: tokenizer.tokenize(x))

    input_query["Tweet"] = input_query["Tweet"].apply(lambda x: remove_stopwords(x))

    lem = WordNetLemmatizer()

    input_query["Tweet"] = input_query["Tweet"].apply(lem_word)

    input_query["Tweet"] = input_query["Tweet"].apply(lambda x: combine_text(x))



    Tweettf = tfidf.transform(input_query["Tweet"])

    result = mnb.predict(Tweettf)[0]

    return jsonify({'prediction':str(result)})


@app.route('/add', methods=['POST'])
def add_tweet():

    Tweet = request.form.get('tweet')
    Lat = request.form.get('lat')
    Long = request.form.get('long')
    City = request.form.get('city')

    update(Tweet, Lat, Long, City)

    resultx = 0

    return jsonify({'predict':str(resultx)})


if __name__ == '__main__':
    app.run()