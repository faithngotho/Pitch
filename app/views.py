from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting Pitch
    print(pitch)
    title = 'Home - Welcome to Pitch Website Online'
    return render_template('index.html', title = title,popular = Pitch)


@app.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    pitch = get_pitch(id)
    title = f'{pitch.title}'

    return render_template('pitch.html',title = title,pitch = pitch)