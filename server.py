'''
Start Flask application
'''
from strike import app

if __name__ == '__main__':
    # app.run('0.0.0.0', port=80, use_reloader=False, debug=True)
    app.run('0.0.0.0', port=80, debug=True)
