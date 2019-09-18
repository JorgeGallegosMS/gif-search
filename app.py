from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    q = request.args.get("search")
    url = 'https://api.tenor.com/v1/search?'

    params = {
        "q": q,
        "key": 'C8UDZFA60WIT',
        "limit": 10,
        "media_filter": "minimal"
    }


    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(url, params)
    # TODO: Get the first 10 results from the search results
    if r.status_code == 200:
        results = json.loads(r.content)['results']
    else:
        results = None
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    print(results)

    return render_template(
    "index.html.j2",
    gifs=results
    )

if __name__ == '__main__':
    app.run(debug=True)
