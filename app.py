from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # extract query term from url
    url = "https://api.tenor.com/v1/search?"
    q = request.args.get("search")
    # params dict with query term and API key
    params = {
        "q": q,
        "key": "C8UDZFA60WIT",
        "limit": 10,
        "media_filter": "minimal"
    }
    # API call to tenor
    r = requests.get(url, params)

    # gets list of gifs
    if r.status_code == 200:
        results = json.loads(r.content)['results']
    else:
        results = None

    return render_template(
        "index.html.j2",
        gifs=results
        )

if __name__ == '__main__':
    app.run(debug=True)
