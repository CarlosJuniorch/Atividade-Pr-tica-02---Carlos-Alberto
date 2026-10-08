# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?

Para que serve o campo disponivel?
Servirá para saber se o livro pode ser emprestado ou não. Se for True, significa que o livro está na biblioteca; se for False, significa que ele já foi emprestado.

Por que usar session.commit()?
Serve para salvar de verdade a alteração no banco de dados. Quando mudamos livro.disponivel, a alteração fica só na memória, e o commit() é o que grava a mudança no arquivo do banco.

Onde é usado o relacionamento entre Livro e Autor?
Na função listar_livros, para mostrar o nome do autor pegando livro.autor.nome, e na função listar_livros_por_autor, para pegar todos os livros de um autor usando autor.livros.