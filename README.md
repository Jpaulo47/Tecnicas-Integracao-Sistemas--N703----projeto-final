# Marketplace para Artesãos do Polo de Artesanato da Beira-Mar

## Objetivo do Trabalho

Este projeto foi desenvolvido como parte da disciplina de **Técnicas de Integração de Sistemas (N703)** da faculdade. O objetivo é criar uma API REST que integre dois sistemas distintos com foco em uma demanda de impacto social:

- **Sistema de Gestão de Artesãos e Produtos**: Onde os artesãos cadastram a si mesmos e seus produtos
- **Sistema de E-commerce para Clientes**: Onde os clientes visualizam os produtos e fazem pedidos

A API serve como um integrador central entre esses dois sistemas, facilitando a comercialização dos produtos artesanais do Polo de Artesanato da Beira-Mar, promovendo o desenvolvimento econômico local e a preservação da cultura artesanal.

## Equipe e Papéis

**Integrantes:**
- [João Paulo da Silva Rodrigues] - [2319025] - Desenvolvedor Principal
- [José William Alves de Oliveira] - [2326237] - Documentação
- [Francisco Wanderson da Silva] - [2323860] - Testes
- [Rayane dos Santos Silva] - [2326292] - Análise de Requisitos
- [Kamilly Almeida Braz] - [2323788] - Gerente de Projeto
- [Matheus de Lima Silva] - [2323842] - Revisor de Código

## Descrição Funcional da Solução

A solução implementa uma API REST que permite:

### Para Artesãos:
- Cadastrar-se no sistema com nome e tipo de artesanato
- Cadastrar produtos com informações detalhadas (nome, descrição, preço, estoque)
- Visualizar seus produtos cadastrados
- Gerenciar o catálogo de produtos

### Para o Sistema de E-commerce:
- Listar todos os produtos disponíveis de todos os artesãos
- Acessar informações detalhadas dos produtos
- Integrar com sistemas de pagamento e entrega

### Funcionalidades Principais:
- **Gestão de Artesãos**: CRUD completo para artesãos
- **Gestão de Produtos**: Cadastro e listagem de produtos por artesão
- **Integração de Sistemas**: API centralizada para comunicação entre sistemas
- **Validação de Dados**: Verificação de integridade e consistência
- **Tratamento de Erros**: Respostas padronizadas para diferentes cenários de erro

## Arquitetura da API

A API foi desenvolvida seguindo os princípios REST e utiliza:

### Tecnologias:
- **Python 3.8+**: Linguagem de programação principal
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI para produção
- **Pytest**: Framework de testes unitários

### Estrutura da API:
```
/
├── src/
│   ├── main.py          # Aplicação principal FastAPI
│   └── __init__.py      # Pacote Python
├── tests/
│   ├── test_main.py     # Testes unitários
│   └── __init__.py      # Pacote de testes
├── docs/
│   └── architecture.md  # Documentação da arquitetura
├── postman/
│   └── collection.json  # Coleção Postman
└── requirements.txt     # Dependências do projeto
```

### Diagrama de Arquitetura:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MARKETPLACE DE ARTESÃOS                     │
│                Polo de Artesanato da Beira-Mar                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   SISTEMA DE    │    │   SISTEMA DE    │    │   SISTEMA DE    │
│   GESTÃO DE     │    │   E-COMMERCE    │    │   INTEGRAÇÃO    │
│   ARTESÃOS      │    │   PARA CLIENTES │    │   (API REST)    │
│                 │    │                 │    │                 │
│ • Cadastro de   │    │ • Visualização  │    │ • FastAPI       │
│   Artesãos      │    │   de Produtos   │    │ • Endpoints     │
│ • Cadastro de   │    │ • Catálogo      │    │   REST          │
│   Produtos      │    │ • Pedidos       │    │ • Validação     │
│ • Gestão de     │    │ • Carrinho      │    │ • Tratamento    │
│   Estoque       │    │ • Checkout      │    │   de Erros      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   API GATEWAY   │
                    │   (FastAPI)     │
                    │                 │
                    │ • Autenticação  │
                    │ • Rate Limiting │
                    │ • Logging       │
                    │ • Monitoramento │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │  CAMADA DE      │
                    │  APLICAÇÃO      │
                    │                 │
                    │ • Controllers   │
                    │ • Services      │
                    │ • Business      │
                    │   Logic         │
                    │ • Validation    │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │  CAMADA DE      │
                    │  DADOS          │
                    │                 │
                    │ • In-Memory     │
                    │   Database      │
                    │ • Models        │
                    │ • Repositories  │
                    │ • Data Access   │
                    └─────────────────┘
```

### Modelos de Dados:

**Artesão (Artisan):**
```json
{
  "id": "uuid-string",
  "name": "Nome do Artesão",
  "craft_type": "Tipo de Artesanato"
}
```

**Produto (Product):**
```json
{
  "id": "uuid-string",
  "name": "Nome do Produto",
  "description": "Descrição detalhada",
  "price": 100.00,
  "stock_quantity": 10,
  "artisan_id": "uuid-do-artesao"
}
```

## Instruções para Execução

### Pré-requisitos:
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação:

1. **Clone o repositório:**
```bash
git clone []
cd marketplace-artesaoes
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Execução:

1. **Iniciar a API:**
```bash
# Opção 1: Usando uvicorn diretamente
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Opção 2: Usando o script principal
python src/main.py
```

2. **Acessar a documentação:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

3. **Executar testes:**
```bash
pytest tests/ -v
```

### Endpoints Disponíveis:

A API estará disponível em `http://localhost:8000` com os seguintes endpoints:

- `GET /` - Status da API
- `POST /artisans` - Cadastrar artesão
- `GET /artisans` - Listar artesãos
- `GET /artisans/{artisan_id}` - Buscar artesão por ID
- `POST /artisans/{artisan_id}/products` - Cadastrar produto para artesão
- `GET /artisans/{artisan_id}/products` - Listar produtos de um artesão
- `GET /products` - Listar todos os produtos

## Documentação das Rotas

### 1. Status da API
```
GET /
```
**Resposta:**
```json
{
  "message": "Marketplace para Artesãos do Polo de Artesanato da Beira-Mar",
  "version": "1.0.0",
  "status": "online"
}
```

### 2. Cadastrar Artesão
```
POST /artisans
```
**Corpo da Requisição:**
```json
{
  "name": "Maria Silva",
  "craft_type": "Cerâmica"
}
```
**Resposta (201 Created):**
```json
{
  "message": "Artesão cadastrado com sucesso",
  "artisan": {
    "id": "uuid-string",
    "name": "Maria Silva",
    "craft_type": "Cerâmica"
  }
}
```

### 3. Listar Artesãos
```
GET /artisans
```
**Resposta (200 OK):**
```json
[
  {
    "id": "uuid-string",
    "name": "Maria Silva",
    "craft_type": "Cerâmica"
  }
]
```

### 4. Buscar Artesão por ID
```
GET /artisans/{artisan_id}
```
**Resposta (200 OK):**
```json
{
  "id": "uuid-string",
  "name": "Maria Silva",
  "craft_type": "Cerâmica"
}
```
**Erro (404 Not Found):**
```json
{
  "error": "Artesão com ID {artisan_id} não encontrado",
  "status_code": 404,
  "timestamp": "2025-08-25T15:30:00"
}
```

### 5. Cadastrar Produto
```
POST /artisans/{artisan_id}/products
```
**Corpo da Requisição:**
```json
{
  "name": "Vaso Artesanal",
  "description": "Vaso de cerâmica feito à mão",
  "price": 150.00,
  "stock_quantity": 5
}
```
**Resposta (201 Created):**
```json
{
  "message": "Produto cadastrado com sucesso",
  "product": {
    "id": "uuid-string",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
}
```

### 6. Listar Produtos de um Artesão
```
GET /artisans/{artisan_id}/products
```
**Resposta (200 OK):**
```json
[
  {
    "id": "uuid-string",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
]
```

### 7. Listar Todos os Produtos
```
GET /products
```
**Resposta (200 OK):**
```json
[
  {
    "id": "uuid-string",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
]
```

## Códigos de Status HTTP

- **200 OK**: Requisição processada com sucesso
- **201 Created**: Recurso criado com sucesso
- **400 Bad Request**: Dados inválidos na requisição
- **404 Not Found**: Recurso não encontrado
- **422 Unprocessable Entity**: Erro de validação de dados

## Relação com ODS 11

Este projeto está alinhado com o **Objetivo de Desenvolvimento Sustentável 11 (ODS 11) - Cidades e Comunidades Sustentáveis**, especificamente com a meta 11.4 que visa "fortalecer esforços para proteger e salvaguardar o patrimônio cultural e natural do mundo".

O marketplace contribui para:
- **Preservação da cultura artesanal local**
- **Geração de renda para artesãos da comunidade**
- **Promoção do turismo cultural sustentável**
- **Fortalecimento da identidade cultural da região**
- **Desenvolvimento econômico local inclusivo**

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
