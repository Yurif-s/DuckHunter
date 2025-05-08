from flask import Blueprint, request, jsonify
from services.duckduckgo_service import search_news

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["GET"])
def search():
    """
    Buscar notícias relacionadas a um tema
    ---
    parameters:
      - name: query
        in: query
        type: string
        required: true
        description: Tema a ser buscado
    responses:
      200:
        description: Lista de notícias encontradas
        schema:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              href:
                type: string
              body:
                type: string
              source:
                type: string
      400:
        description: Erro por falta de parâmetro
    """
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "O parâmetro é obrigatório."}), 400
    results = search_news(query)
    return jsonify(results), 200
