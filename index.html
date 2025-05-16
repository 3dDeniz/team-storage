
from flask import Flask, render_template, request, redirect, url_for
import csv
import os

from base64 import b64encode
app = Flask(__name__)

app.jinja_env.filters['b64encode'] = lambda s: b64encode(s.encode()).decode()

BATTLE_STYLES = [
    "Hyper Offense",
    "Bulky Offense",
    "Balance",
    "Semi-Stall",
    "Stall"
]

def init_db():
    if not os.path.exists('links.csv'):
        with open('links.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['url', 'style', 'description', 'team_name'])

def get_links():
    init_db()
    links = []
    with open('links.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        links = list(reader)
    return links

def add_link_to_db(url, style, description, team_name):
    with open('links.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([url, style, description, team_name])

def delete_link(url):
    links = get_links()
    with open('links.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['url', 'style', 'description', 'team_name'])
        for link in links:
            if link['url'] != url:
                writer.writerow([link['url'], link['style'], link['description'], link['team_name']])



@app.route('/delete/<path:url>', methods=['POST'])
def delete(url):
    delete_link(url)
    return {'success': True}

@app.route('/')
def index():
    style_filter = request.args.get('style', '')
    search_query = request.args.get('search', '').lower()
    links = get_links()
    
    if style_filter:
        links = [link for link in links if link['style'] == style_filter]
    
    if search_query:
        links = [link for link in links if 
                search_query in link['team_name'].lower() or 
                (link['description'] and search_query in link['description'].lower())]
    
    return render_template('index.html', links=links, styles=BATTLE_STYLES)

@app.route('/add', methods=['POST'])
def add_link():
    url = request.form.get('url')
    style = request.form.get('style')
    description = request.form.get('description')
    team_name = request.form.get('team_name')
    
    if url and style and team_name:
        add_link_to_db(url, style, description, team_name)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
