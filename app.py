from flask import Flask, request, render_template
import xmlrpc.client

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # appel XML-RPC vers votre instance Odoo
        client = xmlrpc.client.ServerProxy('https://bootons-test.odoo.com/xmlrpc/2/object')
        # exécution d’une méthode…
        result = client.execute_kw('bootons-test', 2, 'pass4api', 'hr.employee', 'search', [[]])
        return f"Résultat : {result}"
    return render_template('index.html')  # bouton dans un petit form
