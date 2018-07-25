from flask import Flask, request, render_template

from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

articles = []


def _find_article(article_id):

    return next(iter(filter(lambda i: i["article_id"] == article_id, articles)), None)

@app.route("/article/<string:article_id>/",methods=['GET'])
def get(article_id):

    article = _find_article(article_id)

    return {"article": article}, 200 if article is not None else 404

@app.route("/article/<string:article_id>/",methods=['POST'])
def post(article_id):

    existing_article = _find_article(article_id)

    if existing_article is not None:

        return {"message": "Article already created"}, 409

    data = request.get_json()

    # set default value of 0 for integers(vote) and emtpy character for
    # strings(title, content, author) in case user did not provide those values
    new_article = {"article_id": article_id,
                   "vote": data.get("vote", 0),
                   "title": data.get("title", ""),
                   "content": data.get("content", ""),
                   "author": data.get("author", "")}

    articles.append(new_article)

    return {"article": new_article}, 201

@app.route("/article/<string:article_id>/",methods=['PUT'])
def put(article_id):

    data = request.get_json()

    existing_article = self._find_article(article_id)

    if existing_article is not None:

        existing_article["vote"]=data["vote"]

        return {"article": existing_article}, 201

    else:

        new_article = {"article_id": article_id, "vote": data["vote"]}

        articles.append(new_article)

        return {"article": new_article}, 201


@app.route("/articles",methods=['GET'])
def list():

    # sort the articles(list of dictionaries) in descending order of vote
    return {"articles": sorted(articles, key=lambda article: article["vote"], reverse=True)}, 200 



def get_article_data():
    # return articles list with each article as a list of fields to easily show in ui
    cols = ["article_id", "vote", "title", "content", "author"]
    articles_data = []
    for article in articles:
        field_list = []
        for col in cols:
            field_list.append(article[col])
        articles_data.append(field_list)
    return cols, articles_data



app.run(port=5000)
