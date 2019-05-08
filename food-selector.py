import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=False, port=port, host='0.0.0.0')