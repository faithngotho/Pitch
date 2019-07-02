from flask import render_template,request,redirect,url_for
from . import main

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting Pitch
    print(pitch)

    if search_pitch:
        return redirect(url_for('search',pitch_name=search_pitch))
    else:
    title = 'Home - Welcome to Pitch Website Online'
    return render_template('index.html', title = title)


@app.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    pitch = get_pitch(id)
    title = f'{pitch.title}'

    return render_template('pitch.html',title = title,pitch = pitch)

@app.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    pitch_name_list = pitch_name.split(" ")
    pitch_name_format = "+".join(pitch_name_list)
    searched_pitch = search_pitch(pitch_name_format)
    title = f'search results for {pitch_name}'
    return render_template('search.html',pitch = searched_pitch)