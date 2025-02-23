from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from security.auth_token import obter_usuario_logado
from models.produto import Produto
from models.schemas import ProdutoCreate, ProdutoResponse

router = APIRouter()


@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return produtos


@router.post("/", response_model=ProdutoResponse, dependencies=[Depends(obter_usuario_logado)])
def adicionar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    produto_existente = db.query(Produto).filter(Produto.nome == produto.nome).first()
    if produto_existente:
        raise HTTPException(status_code=400, detail="Produto com esse nome já existe")

    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        estoque=produto.estoque,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


@router.put("/", response_model=ProdutoResponse, dependencies=[Depends(obter_usuario_logado)])
def modificar_produto(produto_id: int, produto: ProdutoCreate, db: Session = Depends(get_db)):
    produto_db = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto_db.nome = produto.nome
    produto_db.descricao = produto.descricao
    produto_db.preco = produto.preco
    produto_db.estoque = produto.estoque

    db.commit()
    db.refresh(produto_db)

    return produto_db


@router.delete("/{produto_id}", dependencies=[Depends(obter_usuario_logado)])
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_db = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto_db)
    db.commit()

    return {"mensagem": "Produto removido com sucesso"}
