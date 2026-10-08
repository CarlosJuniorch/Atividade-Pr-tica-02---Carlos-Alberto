from models import Autor, Livro


def popular_banco(session):
    autor1 = Autor(nome="George Orwell", pais="Reino Unido")
    autor2 = Autor(nome="Gabriel García Márquez", pais="Colômbia")
    autor3 = Autor(nome="Agatha Christie", pais="Reino Unido")

    session.add(autor1)
    session.add_all([autor2, autor3])

    livro1 = Livro(titulo="1984", ano=1949, disponivel=True, autor=autor1)
    livro2 = Livro(titulo="A Revolução dos Bichos", ano=1945, disponivel=False, autor=autor1)
    livro3 = Livro(titulo="A Flor da Inglaterra", ano=1936, disponivel=True, autor=autor1)
    livro4 = Livro(titulo="Cem Anos de Solidão", ano=1967, disponivel=True, autor=autor2)
    livro5 = Livro(titulo="O Amor nos Tempos do Cólera", ano=1985, disponivel=False, autor=autor2)
    livro6 = Livro(titulo="E Não Sobrou Nenhum", ano=1939, disponivel=True, autor=autor3)

    session.add(livro1)
    session.add_all([livro2, livro3, livro4, livro5, livro6])

    session.commit()