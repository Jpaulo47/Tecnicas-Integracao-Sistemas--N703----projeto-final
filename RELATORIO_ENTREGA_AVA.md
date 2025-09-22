# Relatório de Entrega - Técnicas de Integração de Sistemas (N703)

## Informações da Equipe

**Disciplina:** Técnicas de Integração de Sistemas (N703)  
**Projeto:** Marketplace para Artesãos do Polo de Artesanato da Beira-Mar  
**Data de Entrega:** [Data Atual]  
**Prazo Final:** 29/09/2025, às 23h59  

### Integrantes da Equipe

| Nome | Matrícula | Papel |
|------|-----------|-------|
| João Paulo da Silva Rodrigues | 2319025 | Desenvolvedor Principal |
| José William Alves de Oliveira | 2326237 | Documentação |
| Francisco Wanderson da Silva | 2323860 | Testes |
| Rayane dos Santos Silva | 2326292 | Análise de Requisitos |
| Kamilly Almeida Braz | 2323788 | Gerente de Projeto |
| Matheus de Lima Silva | 2323842 | Revisor de Código |

## Resumo do Projeto

### Objetivo
Desenvolver uma API REST que integre dois sistemas distintos com foco em uma demanda de impacto social: um sistema de gestão de artesãos e produtos, e um sistema de e-commerce para clientes, facilitando a comercialização dos produtos artesanais do Polo de Artesanato da Beira-Mar.

### Problema Identificado
A necessidade de integrar sistemas de gestão de artesãos com plataformas de e-commerce para promover o desenvolvimento econômico local e a preservação da cultura artesanal.

### Solução Proposta
API REST desenvolvida em Python com FastAPI que serve como integrador central entre:
- **Sistema de Gestão de Artesãos e Produtos**: Para cadastro e gestão de artesãos e seus produtos
- **Sistema de E-commerce**: Para visualização e comercialização dos produtos

## Arquitetura da Solução

### Tecnologias Utilizadas
- **Python 3.8+**: Linguagem de programação principal
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI para produção
- **Pytest**: Framework de testes unitários

### Endpoints Implementados
- `GET /` - Status da API
- `POST /artisans` - Cadastrar artesão
- `GET /artisans` - Listar artesãos
- `GET /artisans/{artisan_id}` - Buscar artesão por ID
- `POST /artisans/{artisan_id}/products` - Cadastrar produto para artesão
- `GET /artisans/{artisan_id}/products` - Listar produtos de um artesão
- `GET /products` - Listar todos os produtos

### Modelos de Dados
**Artesão:**
```json
{
  "id": "uuid-string",
  "name": "Nome do Artesão",
  "craft_type": "Tipo de Artesanato"
}
```

**Produto:**
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

## Requisitos Técnicos Atendidos

### ✅ Protocolo de Comunicação
- REST sobre HTTP implementado

### ✅ Endpoints Funcionais
- `POST /artisans/{artisan_id}/products` - Implementado
- `GET /products` - Implementado

### ✅ Modelos de Dados
- Artesão: id, name, craft_type - Implementado
- Produto: id, name, description, price, stock_quantity, artisan_id - Implementado

### ✅ Tratamento de Erros
- Status 400/422 para campos obrigatórios faltando - Implementado
- Status 404 para artesão não encontrado - Implementado

### ✅ Testes Unitários
- 12 testes implementados cobrindo todos os cenários
- Cobertura de endpoints principais e casos de erro

## Estrutura do Repositório

```
/
├── README.md                    # Documentação principal
├── docs/
│   └── architecture.md         # Documentação da arquitetura
├── src/
│   ├── main.py                 # Aplicação principal FastAPI
│   └── __init__.py             # Pacote Python
├── tests/
│   ├── test_main.py            # Testes unitários
│   └── __init__.py             # Pacote de testes
├── postman/
│   └── collection.json         # Coleção Postman
├── requirements.txt            # Dependências do projeto
├── run.py                      # Script de execução
└── .gitignore                  # Configuração Git
```

## Funcionalidades Implementadas

### Para Artesãos
- Cadastro no sistema com nome e tipo de artesanato
- Cadastro de produtos com informações detalhadas
- Visualização de produtos cadastrados
- Gestão de catálogo de produtos

### Para Sistema de E-commerce
- Listagem de todos os produtos disponíveis
- Acesso a informações detalhadas dos produtos
- Integração preparada para sistemas de pagamento e entrega

### Funcionalidades Técnicas
- Validação de dados com Pydantic
- Tratamento de erros padronizado
- Documentação automática com Swagger/OpenAPI
- Testes unitários abrangentes
- Coleção Postman para testes manuais

## Testes e Validação

### Testes Unitários
- **12 testes implementados** cobrindo:
  - Cenários de sucesso para todos os endpoints
  - Cenários de erro e validação
  - Tratamento de exceções
- **Todos os testes passando** ✅

### Testes Manuais
- Coleção Postman completa e funcional
- Documentação de testes com cURL
- API testada e operacional

## Impacto Social e ODS 11

O projeto está alinhado com o **Objetivo de Desenvolvimento Sustentável 11 (ODS 11) - Cidades e Comunidades Sustentáveis**, contribuindo para:

- **Preservação da cultura artesanal local**
- **Geração de renda para artesãos da comunidade**
- **Promoção do turismo cultural sustentável**
- **Fortalecimento da identidade cultural da região**
- **Desenvolvimento econômico local inclusivo**

## Instruções de Execução

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação
```bash
# 1. Clone o repositório
git clone [https://github.com/Jpaulo47/Tecnicas-Integracao-Sistemas--N703----projeto-final.git]
cd marketplace-artesaoes

# 2. Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt
```

### Execução
```bash
# Iniciar a API
python run.py

# Acessar documentação
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc

# Executar testes
pytest tests/ -v
```

## Conclusão

O projeto foi desenvolvido com sucesso, atendendo a todos os requisitos técnicos especificados no prompt-master. A API está funcional, testada e documentada, pronta para integração com sistemas de gestão de artesãos e e-commerce.

A solução implementada demonstra competência técnica na integração de sistemas, seguindo as melhores práticas de desenvolvimento de APIs REST, com foco em qualidade, manutenibilidade e impacto social positivo.

## Link do Repositório

**GitHub:** [https://github.com/Jpaulo47/Tecnicas-Integracao-Sistemas--N703----projeto-final]

