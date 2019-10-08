from flask import Flask, request, jsonify
# from flask_cors import CORS
from flask import request
from newsplease import NewsPlease
app = Flask(__name__)
# CORS(app)
# endpoint to create new user
@app.route("/news/toi", methods=["GET"])
def add_user():
    news=[]
    article = NewsPlease.from_url('https://economictimes.indiatimes.com/wealth/personal-finance-news/rbi-policy-why-repo-rate-cut-failed-to-cheer/articleshow/71451242.cms')
    news.append({
        "authors": article.authors,
        "date_download": article.date_download,
        "date_modify": article.date_modify,
        "date_publish": article.date_publish,
        "description": article.description,
        "filename": article.filename,
        "image_url": article.image_url,
        "language": article.language,
        "localpath": article.localpath,
        "source_domain": article.source_domain,
        "text": article.text,
        "title": article.title,
        "title_page": article.title_page,
        "title_rss": article.title_rss,
        "url": article.url
        })
    return jsonify(news)
@app.route('/url',methods=['POST','GET'])
def url():
    news=[]
    error =None
    if request.method=='POST':
        # article = NewsPlease.from_url('https://economictimes.indiatimes.com/wealth/personal-finance-news/rbi-policy-why-repo-rate-cut-failed-to-cheer/articleshow/71451242.cms')
        data=request.get_json()
        print(data['url'])
        article = NewsPlease.from_url(data['url'])
        news.append({
            "authors": article.authors,
            "date_download": article.date_download,
            "date_modify": article.date_modify,
            "date_publish": article.date_publish,
            "description": article.description,
            "filename": article.filename,
            "image_url": article.image_url,
            "language": article.language,
            "localpath": article.localpath,
            "source_domain": article.source_domain,
            "text": article.text,
            "title": article.title,
            "title_page": article.title_page,
            "title_rss": article.title_rss,
            "url": article.url
            })
    return jsonify(news)

if __name__ == '__main__':
    article = NewsPlease.from_url('https://economictimes.indiatimes.com/wealth/personal-finance-news/rbi-policy-why-repo-rate-cut-failed-to-cheer/articleshow/71451242.cms')
    print(article)
    app.run(host='0.0.0.0', port=5002)