from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_file('index.html')

@app.route('/navigate')
def navigate():
    query = request.args.get('q', 'home').lower()

    if query.startswith('projects/'):
        project_name = query.split('/', 1)[1]
        return render_template('navigate.html', section='project_detail', project=project_name)

    elif query in ['home', 'about', 'links', 'projects']:
        return render_template('navigate.html', section=query)

    return render_template('navigate.html', section='home')

if __name__ == '__main__':
    app.run(debug=True)
