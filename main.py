import nltk
from textblob import TextBlob
from newspaper import Article
from flask import Flask, render_template, request

nltk.download('punkt')

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        analysis = TextBlob(article.text)
        sentiment = "Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"
        return render_template('index.html', title=article.title, authors=article.authors, publish_date=article.publish_date, summary=article.summary, sentiment=sentiment)
    return render_template('index.html', title='', authors='', publish_date='', summary='', sentiment='')

if __name__ == '__main__':
    app.run(debug=True)
