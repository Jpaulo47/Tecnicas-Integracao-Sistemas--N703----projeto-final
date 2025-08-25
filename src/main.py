from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Marketplace para Artesãos do Polo de Artesanato da Beira-Mar",
    description="API de integração entre sistema de gestão de artesãos e e-commerce",
    version="1.0.0"
)

# Modelos de dados
class Artisan(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., min_length=1, description="Nome do artesão")
    craft_type: str = Field(..., min_length=1, description="Tipo de artesanato")

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., min_length=1, description="Nome do produto")
    description: str = Field(..., min_length=1, description="Descrição do produto")
    price: float = Field(..., gt=0, description="Preço do produto")
    stock_quantity: int = Field(..., ge=0, description="Quantidade em estoque")
    artisan_id: str = Field(..., description="ID do artesão responsável")

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Nome do produto")
    description: str = Field(..., min_length=1, description="Descrição do produto")
    price: float = Field(..., gt=0, description="Preço do produto")
    stock_quantity: int = Field(..., ge=0, description="Quantidade em estoque")

# Banco de dados em memória (simulado)
artisans_db = {}
products_db = {}

# Endpoints
@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Marketplace para Artesãos do Polo de Artesanato da Beira-Mar",
        "version": "1.0.0",
        "status": "online"
    }

@app.post("/artisans/{artisan_id}/products", status_code=status.HTTP_201_CREATED)
async def create_product(artisan_id: str, product_data: ProductCreate):
    """
    Cadastra um novo produto para um artesão específico.
    
    Args:
        artisan_id: ID do artesão
        product_data: Dados do produto a ser cadastrado
    
    Returns:
        Produto criado com sucesso
    """
    # Verificar se o artesão existe
    if artisan_id not in artisans_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artesão com ID {artisan_id} não encontrado"
        )
    
    # Criar o produto
    product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity,
        artisan_id=artisan_id
    )
    
    # Armazenar o produto
    products_db[product.id] = product
    
    return {
        "message": "Produto cadastrado com sucesso",
        "product": product
    }

@app.get("/products", response_model=List[Product])
async def get_products():
    """
    Lista todos os produtos disponíveis de todos os artesãos.
    
    Returns:
        Lista de todos os produtos cadastrados
    """
    return list(products_db.values())

@app.get("/artisans", response_model=List[Artisan])
async def get_artisans():
    """
    Lista todos os artesãos cadastrados.
    
    Returns:
        Lista de todos os artesãos
    """
    return list(artisans_db.values())

@app.post("/artisans", status_code=status.HTTP_201_CREATED)
async def create_artisan(artisan: Artisan):
    """
    Cadastra um novo artesão.
    
    Args:
        artisan: Dados do artesão a ser cadastrado
    
    Returns:
        Artesão criado com sucesso
    """
    artisans_db[artisan.id] = artisan
    return {
        "message": "Artesão cadastrado com sucesso",
        "artisan": artisan
    }

@app.get("/artisans/{artisan_id}", response_model=Artisan)
async def get_artisan(artisan_id: str):
    """
    Busca um artesão específico pelo ID.
    
    Args:
        artisan_id: ID do artesão
    
    Returns:
        Dados do artesão
    """
    if artisan_id not in artisans_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artesão com ID {artisan_id} não encontrado"
        )
    
    return artisans_db[artisan_id]

@app.get("/artisans/{artisan_id}/products", response_model=List[Product])
async def get_artisan_products(artisan_id: str):
    """
    Lista todos os produtos de um artesão específico.
    
    Args:
        artisan_id: ID do artesão
    
    Returns:
        Lista de produtos do artesão
    """
    if artisan_id not in artisans_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artesão com ID {artisan_id} não encontrado"
        )
    
    artisan_products = [
        product for product in products_db.values() 
        if product.artisan_id == artisan_id
    ]
    
    return artisan_products

# Tratamento de erros global
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.now().isoformat()
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
