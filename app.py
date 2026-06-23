import os
import webbrowser
from flask import Flask, render_template, request

from indexer import InvertedIndex
from ranker import Ranker
from trie import Trie

app = Flask(__name__)

indexer = InvertedIndex()
index = indexer.build_index("documents")

ranker = Ranker()

trie = Trie()

for word in index.keys():
    trie.insert(word)


@app.route("/", methods=["GET", "POST"])

def home():

    results = []

    if request.method == "POST":

        query = request.form["query"].lower()

        query_words = query.split()

        results = ranker.rank(
            query_words,
            index
        )

    return render_template(
        "index.html",
        results=results
    )
@app.route('/document/<filename>')
def view_document(filename):

    filepath = os.path.join(
        "documents",
        filename
    )

    with open(
        filepath,
        'r',
        encoding='utf-8'
    ) as file:

        content = file.read()

    return render_template(
        "document.html",
        filename=filename,
        content=content
    )


if __name__ == "__main__":

    webbrowser.open(
        "http://127.0.0.1:5000"
    )

    app.run(debug=True)