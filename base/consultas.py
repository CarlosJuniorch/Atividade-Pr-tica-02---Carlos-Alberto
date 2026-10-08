from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    livros = session.scalars(select(Livro)).all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")
    return livros


def listar_livros_disponiveis(session):
    livros = session.scalars(select(Livro).where(Livro.disponivel == True)).all()
    for livro in livros:
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome}")
    return livros


def buscar_livros_por_titulo(session, trecho):
    livros = session.scalars(select(Livro).where(Livro.titulo.contains(trecho))).all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")
    return livros


def listar_livros_por_autor(session, nome_autor):
    autor = session.scalar(select(Autor).where(Autor.nome.contains(nome_autor)))
    if autor:
        for livro in autor.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Título: {livro.titulo} | Status: {status}")
        return autor.livros
    print("Autor não encontrado.")
    return []