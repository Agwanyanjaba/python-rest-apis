# REST APIs by wycliffe
# 2020-06-15
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/query_params', methods=['GET', 'POST'])
def queryParams():
    lang = request.args.get('language')
    frame = request.args['framework']
    website = request.args.get('website')
    return '''<h1>The programming language is {}</h1>'
              <h1>The programming language is {}</h1>'
              <h1>The programming language is {}</h1>'''.format(lang, frame, website)


@app.route('/form_example', methods=['POST', 'GET'])
def formRequest():
    if request.method == 'POST':
        lang = request.form.get('language')
        # frame = request.form.get('framework')
        frame = request.form['framework']
        return '''<h1>Form submitted successfully</h1>
            <h1>Languange is: {} and Framework is: {}<h1>
        '''.format(lang, frame)

    return '''<form method=POST>
    Language<input type="text" name="language">
    Framework<input type="text" name="framework">
    <input type="submit" name="Submit">
    </form>   
    '''


@app.route('/form', methods=['POST'])
def formPost():
    if request.method == 'POST':
        lang = request.form['email']
        # frame = request.form.get('framework')
        frame = request.form['password']
        return '''<h1>Form submitted successfully</h1>
            <h1>Email is: {} and Password is: {}<h1>
        '''.format(lang, frame)


# Run the app on specified host and port
if __name__ == '__main__':
    app.run(host="localhost", port=7001, debug=True)
