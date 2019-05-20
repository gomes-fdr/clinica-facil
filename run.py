from flask import render_template
from backend import create_app

app = create_app()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

# TODO: Criar estrutura para logar eventos importantes

if __name__ == "__main__":
    app.run(host='0.0.0.0')