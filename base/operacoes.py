from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    livro = session.scalar(select(Livro).where(Livro.titulo.ilike(f"%{titulo}%")))

    if not livro:
        print("Livro não encontrado.")
    elif not livro.disponivel:
        print("Livro já está indisponível.")
    else:
        livro.disponivel = False
        session.commit()
        print("Livro emprestado com sucesso!")


def devolver_livro(session, titulo):
    livro = session.scalar(select(Livro).where(Livro.titulo.ilike(f"%{titulo}%")))

    if not livro:
        print("Livro não encontrado.")
    elif livro.disponivel:
        print("Livro já está disponível.")
    else:
        livro.disponivel = True
        session.commit()
        print("Livro devolvido com sucesso!")