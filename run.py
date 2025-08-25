#!/usr/bin/env python3
"""
Script para executar a API do Marketplace para Artesãos
"""

import uvicorn
from src.main import app

if __name__ == "__main__":
    print("🚀 Iniciando API do Marketplace para Artesãos...")
    print("📍 Endpoints disponíveis:")
    print("   - GET  /                    - Status da API")
    print("   - POST /artisans            - Cadastrar artesão")
    print("   - GET  /artisans            - Listar artesãos")
    print("   - GET  /artisans/{id}       - Buscar artesão por ID")
    print("   - POST /artisans/{id}/products - Cadastrar produto")
    print("   - GET  /artisans/{id}/products - Listar produtos do artesão")
    print("   - GET  /products            - Listar todos os produtos")
    print("\n📚 Documentação:")
    print("   - Swagger UI: http://localhost:8000/docs")
    print("   - ReDoc:      http://localhost:8000/redoc")
    print("\n" + "="*50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
