from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config["SECRET_KEY"] = "some-secret-word"

debug = DebugToolbarExtension(app)


"""define route for forms"""


@app.route('/')
def show_form():
    inputs = story.prompts
    return render_template("form.html", inputs=inputs)


"""define route to display story"""


@app.route('/story')
def show_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)

# work in progress - need to add logic and a route to allow user to
# pick a story from a list of stories.
