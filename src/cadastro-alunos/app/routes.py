from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Aluno

main = Blueprint("main", __name__)


@main.route("/")
def index():
    alunos = Aluno.query.all()
    return render_template("alunos.html", alunos=alunos)


@main.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        aluno = Aluno(
            nome=request.form["nome"],
            cpf=request.form["cpf"],
            data_nascimento=request.form["data_nascimento"],
            email=request.form["email"],
            telefone=request.form["telefone"],
            curso=request.form["curso"],
            matricula=request.form["matricula"]
        )

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("cadastrar.html")

    @main.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    aluno = Aluno.query.get_or_404(id)

    if request.method == "POST":
        aluno.nome = request.form["nome"]
        aluno.cpf = request.form["cpf"]
        aluno.data_nascimento = request.form["data_nascimento"]
        aluno.email = request.form["email"]
        aluno.telefone = request.form["telefone"]
        aluno.curso = request.form["curso"]
        aluno.matricula = request.form["matricula"]

        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("editar.html", aluno=aluno)