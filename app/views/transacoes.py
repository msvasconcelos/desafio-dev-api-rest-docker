from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
from ..models.contas import Contas, conta_schema, contas_schema
from ..models.pessoas import Pessoas, pessoa_schema, pessoas_schema
from ..models.transacoes import Transacoes, transacao_schema, transacoes_schema

"""Retorna lista de usuários"""

"""Cadastro de usuários com validação de existência"""


def extrato():
    idConta = request.json['idConta']

    transacoes = Transacoes.query.filter(Transacoes.idConta.like(f'%{idConta}%')).all()

    if transacoes:
        result = transacoes_schema.dump(transacoes)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})




"""Atualiza usuário baseado no ID, caso o mesmo exista."""


