# SIMULADO — RaspaTec: webscraping de tecnologia em tecmundo.com.br
# ATENÇÃO: rode ESTE app.py DENTRO desta pasta (não use a pasta de outra prova).

import os
import sys
from pathlib import Path

# Garante imports da pasta desta prova (evita misturar services de outra pasta).
_RAIZ = Path(__file__).resolve().parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

from flask import Flask, jsonify

from controllers import historico_api_bp, noticias_api_bp, site_bp
from models import db

ENDPOINTS: list[dict[str, str]] = [
    {
        "metodo": "GET",
        "rota": "/api/noticias",
        "descricao": "Webscraping ao vivo (RaspaTec → tecmundo.com.br) — não grava",
        "query": "?modo=palavra ou todos",
    },
    {
        "metodo": "POST",
        "rota": "/api/noticias/sincronizar",
        "descricao": "Scraping + grava coleta no historico_noticias.db",
        "query": "?modo=palavra ou todos",
    },
    {
        "metodo": "POST",
        "rota": "/api/noticias/manual",
        "descricao": "Cadastra 1 notícia manual (JSON: titulo, url, secao)",
        "query": "",
    },
    {
        "metodo": "GET",
        "rota": "/api/historico/coletas",
        "descricao": "Lista coletas gravadas",
    },
    {
        "metodo": "GET",
        "rota": "/api/historico/coletas/<id>",
        "descricao": "Detalhe de uma coleta com notícias",
    },
]


def criar_app() -> Flask:
    """Monta Flask com templates, dois SQLite, blueprints do site e da API."""
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )
    pasta = os.path.abspath(os.path.dirname(__file__))

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "principal.db"
    )
    app.config["SQLALCHEMY_BINDS"] = {
        "historico": "sqlite:///" + os.path.join(pasta, "historico_noticias.db"),
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'prova-s-raspatec-dev'

    db.init_app(app)
    app.register_blueprint(site_bp)
    app.register_blueprint(noticias_api_bp)
    app.register_blueprint(historico_api_bp)

    with app.app_context():
        db.create_all()

    @app.route("/api")
    def api_index():
        """GET /api — índice JSON dos endpoints."""
        return jsonify(
            {
                "projeto": 'RaspaTec',
                "prova": "S — RaspaTec · tecnologia (tecmundo.com.br)",
                "modelo": "Aula 19 Webscraping",
                "site": "/",
                "fonte": 'https://www.tecmundo.com.br/',
                "porta": 5000,
                "liberacao_internet": "LIBERACAO_INTERNET.md",
                "bancos": {
                    "principal": "principal.db",
                    "historico": "historico_noticias.db",
                },
                "endpoints": ENDPOINTS,
            }
        )

    return app


app = criar_app()

if __name__ == "__main__":
    print("=" * 60)
    print("  RaspaTec  fonte=https://www.tecmundo.com.br/")
    print("  Abra: http://127.0.0.1:5000")
    print("  (rode só UMA prova por vez — pasta correta)")
    print("=" * 60)
    app.run(debug=True, port=5000)
