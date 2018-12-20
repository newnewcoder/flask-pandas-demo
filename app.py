import numpy as np
import pandas as pd
from flask import render_template, Flask, request, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the secret'

@app.route('/', methods=['GET'])
def index():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=['學生A','學生B', '學生C'])
    df = df.append(df.agg(['sum', 'mean']))
    df.rename(index={'sum':'加總', 'mean':'平均'}, inplace=True)
    return render_template('index.html',table=df.to_html(classes='table table-striped'))

if __name__ == '__main__':
    app.run(debug=True)
