from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'The Dude Abides!'

@app.route('/')
def index():
    # Add 2 counters: true_visit to get actual number of times
    #that ('/') is accessed. And visit for modified count
    if 'visit' and 'true_visit' in session:
        session['true_visit'] += 1
        session['visit'] += 1
    else:
        session['true_visit'] = 0
        session['visit'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/plus2visits')
def plus2():
    session['visit'] += 1
    return redirect('/')

@app.route('/select_increment', methods=['POST'])
def select_increment():
    num = int(request.form['increment_value']) - 1
    session['visit'] += num 
    return redirect('/')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
