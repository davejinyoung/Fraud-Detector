from flask import Blueprint, render_template, request
import re

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")


@views.route('/fb', methods=['GET', 'POST'])
def face():
    if request.method == 'POST':
        fb_link = request.form.get('link')
        root = 'https://www.facebook.com/marketplace/item/'
        if re.match(root, fb_link) is not None:
            print("the link is correct")

    return render_template("face.html")


@views.route('/craig', methods=['GET', 'POST'])
def craig():
    if request.method == 'POST':
        location = request.form.get('location')
        cg_link = request.form.get('link')
        root = f'https://{location}.craigslist.org/'
        if re.match(root, cg_link) is not None:
            print("the link is correct")

    return render_template("craig.html")


@views.route('/about')
def about():
    return render_template("about.html")
