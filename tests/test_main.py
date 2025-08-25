import pytest
from fastapi.testclient import TestClient
from src.main import app, artisans_db, products_db

client = TestClient(app)

# Fixture para limpar o banco de dados antes de cada teste
@pytest.fixture(autouse=True)
def clear_database():
    """Limpa o banco de dados antes de cada teste"""
    artisans_db.clear()
    products_db.clear()
    yield

class TestArtisanEndpoints:
    """Testes para endpoints relacionados a artesãos"""
    
    def test_create_artisan_success(self):
        """Teste de criação de artesão com sucesso"""
        artisan_data = {
            "name": "Maria Silva",
            "craft_type": "Cerâmica"
        }
        
        response = client.post("/artisans", json=artisan_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Artesão cadastrado com sucesso"
        assert data["artisan"]["name"] == artisan_data["name"]
        assert data["artisan"]["craft_type"] == artisan_data["craft_type"]
        assert "id" in data["artisan"]
    
    def test_create_artisan_missing_fields(self):
        """Teste de criação de artesão com campos obrigatórios faltando"""
        artisan_data = {
            "name": "João"
            # craft_type faltando
        }
        
        response = client.post("/artisans", json=artisan_data)
        
        assert response.status_code == 422  # Validation Error
    
    def test_get_artisans_empty(self):
        """Teste de listagem de artesãos quando não há nenhum cadastrado"""
        response = client.get("/artisans")
        
        assert response.status_code == 200
        assert response.json() == []
    
    def test_get_artisan_by_id_success(self):
        """Teste de busca de artesão por ID com sucesso"""
        # Primeiro criar um artesão
        artisan_data = {
            "name": "Ana Costa",
            "craft_type": "Bordado"
        }
        create_response = client.post("/artisans", json=artisan_data)
        artisan_id = create_response.json()["artisan"]["id"]
        
        # Buscar o artesão criado
        response = client.get(f"/artisans/{artisan_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == artisan_data["name"]
        assert data["craft_type"] == artisan_data["craft_type"]
        assert data["id"] == artisan_id
    
    def test_get_artisan_by_id_not_found(self):
        """Teste de busca de artesão por ID inexistente"""
        response = client.get("/artisans/nonexistent-id")
        
        assert response.status_code == 404
        assert "não encontrado" in response.json()["error"]

class TestProductEndpoints:
    """Testes para endpoints relacionados a produtos"""
    
    def test_create_product_success(self):
        """Teste de criação de produto com sucesso"""
        # Primeiro criar um artesão
        artisan_data = {
            "name": "Pedro Santos",
            "craft_type": "Madeira"
        }
        artisan_response = client.post("/artisans", json=artisan_data)
        artisan_id = artisan_response.json()["artisan"]["id"]
        
        # Criar produto para o artesão
        product_data = {
            "name": "Cadeira de Balanço",
            "description": "Cadeira artesanal de madeira maciça",
            "price": 450.00,
            "stock_quantity": 5
        }
        
        response = client.post(f"/artisans/{artisan_id}/products", json=product_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Produto cadastrado com sucesso"
        assert data["product"]["name"] == product_data["name"]
        assert data["product"]["price"] == product_data["price"]
        assert data["product"]["artisan_id"] == artisan_id
        assert "id" in data["product"]
    
    def test_create_product_artisan_not_found(self):
        """Teste de criação de produto para artesão inexistente"""
        product_data = {
            "name": "Produto Teste",
            "description": "Descrição do produto",
            "price": 100.00,
            "stock_quantity": 10
        }
        
        response = client.post("/artisans/nonexistent-id/products", json=product_data)
        
        assert response.status_code == 404
        assert "não encontrado" in response.json()["error"]
    
    def test_create_product_invalid_data(self):
        """Teste de criação de produto com dados inválidos"""
        # Primeiro criar um artesão
        artisan_data = {
            "name": "Carlos Lima",
            "craft_type": "Metal"
        }
        artisan_response = client.post("/artisans", json=artisan_data)
        artisan_id = artisan_response.json()["artisan"]["id"]
        
        # Tentar criar produto com preço negativo
        product_data = {
            "name": "Produto Inválido",
            "description": "Descrição",
            "price": -50.00,  # Preço negativo
            "stock_quantity": 5
        }
        
        response = client.post(f"/artisans/{artisan_id}/products", json=product_data)
        
        assert response.status_code == 422  # Validation Error
    
    def test_get_products_empty(self):
        """Teste de listagem de produtos quando não há nenhum cadastrado"""
        response = client.get("/products")
        
        assert response.status_code == 200
        assert response.json() == []
    
    def test_get_products_with_data(self):
        """Teste de listagem de produtos com dados cadastrados"""
        # Criar artesão
        artisan_data = {
            "name": "Lucia Ferreira",
            "craft_type": "Tecelagem"
        }
        artisan_response = client.post("/artisans", json=artisan_data)
        artisan_id = artisan_response.json()["artisan"]["id"]
        
        # Criar produtos
        product1_data = {
            "name": "Tapete Artesanal",
            "description": "Tapete feito à mão",
            "price": 200.00,
            "stock_quantity": 3
        }
        product2_data = {
            "name": "Mantinha",
            "description": "Mantinha de crochê",
            "price": 80.00,
            "stock_quantity": 8
        }
        
        client.post(f"/artisans/{artisan_id}/products", json=product1_data)
        client.post(f"/artisans/{artisan_id}/products", json=product2_data)
        
        # Listar produtos
        response = client.get("/products")
        
        assert response.status_code == 200
        products = response.json()
        assert len(products) == 2
        assert any(p["name"] == "Tapete Artesanal" for p in products)
        assert any(p["name"] == "Mantinha" for p in products)
    
    def test_get_artisan_products(self):
        """Teste de listagem de produtos de um artesão específico"""
        # Criar artesão
        artisan_data = {
            "name": "Roberto Alves",
            "craft_type": "Couro"
        }
        artisan_response = client.post("/artisans", json=artisan_data)
        artisan_id = artisan_response.json()["artisan"]["id"]
        
        # Criar produto para o artesão
        product_data = {
            "name": "Carteira de Couro",
            "description": "Carteira artesanal",
            "price": 120.00,
            "stock_quantity": 15
        }
        client.post(f"/artisans/{artisan_id}/products", json=product_data)
        
        # Listar produtos do artesão
        response = client.get(f"/artisans/{artisan_id}/products")
        
        assert response.status_code == 200
        products = response.json()
        assert len(products) == 1
        assert products[0]["name"] == "Carteira de Couro"
        assert products[0]["artisan_id"] == artisan_id

class TestRootEndpoint:
    """Testes para o endpoint raiz"""
    
    def test_root_endpoint(self):
        """Teste do endpoint raiz da API"""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert "Marketplace para Artesãos" in data["message"]
        assert data["version"] == "1.0.0"
        assert data["status"] == "online"
