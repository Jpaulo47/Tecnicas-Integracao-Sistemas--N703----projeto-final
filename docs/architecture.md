# Arquitetura da API - Marketplace para Artesãos

## Visão Geral

A API do Marketplace para Artesãos do Polo de Artesanato da Beira-Mar foi projetada seguindo os princípios de arquitetura REST e utiliza uma arquitetura em camadas para garantir modularidade, escalabilidade e manutenibilidade.

## Diagrama de Arquitetura

### Visão Geral do Sistema

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

### Fluxo de Dados

```
1. CADASTRO DE ARTESÃO:
   Sistema Gestão → API → Validação → Armazenamento → Resposta

2. CADASTRO DE PRODUTO:
   Sistema Gestão → API → Validação → Verificação Artesão → Armazenamento → Resposta

3. LISTAGEM DE PRODUTOS:
   Sistema E-commerce → API → Busca Dados → Serialização → Resposta JSON

4. CONSULTA DE ARTESÃO:
   Sistema E-commerce → API → Busca por ID → Validação → Resposta JSON
```

### Componentes da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENTES                                │
├─────────────────────────────────────────────────────────────────┤
│ • Artesãos (Sistema de Gestão)                                 │
│ • Clientes (Sistema de E-commerce)                             │
│ • Administradores                                               │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CAMADA DE APRESENTAÇÃO                      │
├─────────────────────────────────────────────────────────────────┤
│ • FastAPI Framework                                             │
│ • Pydantic Models (Validação)                                  │
│ • Swagger/OpenAPI (Documentação)                               │
│ • Exception Handlers (Tratamento de Erros)                     │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CAMADA DE APLICAÇÃO                         │
├─────────────────────────────────────────────────────────────────┤
│ • Controllers/Endpoints                                         │
│ • Business Logic                                                │
│ • Validation Services                                           │
│ • Error Handling                                                │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CAMADA DE DADOS                           │
├─────────────────────────────────────────────────────────────────┤
│ • In-Memory Database (artisans_db, products_db)                │
│ • Data Models (Artisan, Product)                               │
│ • Repository Pattern                                            │
└─────────────────────────────────────────────────────────────────┘
```

## Componentes da Arquitetura

### 1. Camada de Apresentação (Presentation Layer)
- **FastAPI Framework**: Responsável por receber e processar requisições HTTP
- **Pydantic Models**: Validação e serialização de dados
- **Swagger/OpenAPI**: Documentação automática da API

### 2. Camada de Aplicação (Application Layer)
- **Controllers/Endpoints**: Lógica de negócio e roteamento
- **Services**: Regras de negócio e validações
- **Exception Handlers**: Tratamento centralizado de erros

### 3. Camada de Dados (Data Layer)
- **In-Memory Database**: Armazenamento temporário em memória
- **Data Models**: Estruturas de dados para Artesãos e Produtos
- **Repository Pattern**: Abstração para acesso a dados

## Padrões Arquiteturais Utilizados

### 1. REST API
- **Recursos**: Artesãos (`/artisans`) e Produtos (`/products`)
- **Métodos HTTP**: GET, POST, PUT, DELETE
- **Status Codes**: Códigos de resposta padronizados
- **JSON**: Formato de dados para requisições e respostas

### 2. Model-View-Controller (MVC)
- **Model**: Classes Pydantic para Artisan e Product
- **View**: Respostas JSON da API
- **Controller**: Endpoints FastAPI

### 3. Repository Pattern
- Abstração da camada de dados
- Facilita testes unitários
- Permite mudança de implementação de dados

## Fluxo de Dados

### 1. Cadastro de Artesão
```
Cliente → POST /artisans → Validação → Armazenamento → Resposta
```

### 2. Cadastro de Produto
```
Cliente → POST /artisans/{id}/products → Validação → Verificação Artesão → Armazenamento → Resposta
```

### 3. Listagem de Produtos
```
Cliente → GET /products → Busca Dados → Serialização → Resposta JSON
```

## Tratamento de Erros

### Estratégia de Tratamento
- **HTTP Status Codes**: Códigos apropriados para cada tipo de erro
- **Error Response Format**: Formato padronizado de resposta de erro
- **Validation Errors**: Validação automática via Pydantic
- **Custom Exceptions**: Exceções específicas do domínio

### Códigos de Status Utilizados
- **200 OK**: Sucesso na operação
- **201 Created**: Recurso criado com sucesso
- **400 Bad Request**: Dados inválidos
- **404 Not Found**: Recurso não encontrado
- **422 Unprocessable Entity**: Erro de validação

## Segurança

### Validações Implementadas
- **Input Validation**: Validação de entrada via Pydantic
- **Data Sanitization**: Limpeza e validação de dados
- **Type Safety**: Tipagem estática com Python type hints

### Considerações Futuras
- **Authentication**: Sistema de autenticação JWT
- **Authorization**: Controle de acesso baseado em roles
- **Rate Limiting**: Limitação de requisições por IP
- **CORS**: Configuração de Cross-Origin Resource Sharing

## Escalabilidade

### Estratégias de Escalabilidade
- **Stateless Design**: API sem estado para facilitar escalabilidade horizontal
- **Modular Architecture**: Componentes independentes
- **Database Abstraction**: Facilita migração para banco de dados persistente

### Melhorias Futuras
- **Database**: Migração para PostgreSQL ou MongoDB
- **Caching**: Implementação de Redis para cache
- **Load Balancer**: Balanceamento de carga
- **Microservices**: Decomposição em serviços menores

## Monitoramento e Observabilidade

### Logs
- **Request Logging**: Log de todas as requisições
- **Error Logging**: Log detalhado de erros
- **Performance Logging**: Métricas de performance

### Métricas
- **Response Time**: Tempo de resposta dos endpoints
- **Error Rate**: Taxa de erro por endpoint
- **Throughput**: Número de requisições por segundo

## Testes

### Estratégia de Testes
- **Unit Tests**: Testes unitários para cada componente
- **Integration Tests**: Testes de integração entre camadas
- **API Tests**: Testes de endpoints via HTTP client

### Cobertura de Testes
- **Endpoint Coverage**: Todos os endpoints testados
- **Error Scenarios**: Cenários de erro cobertos
- **Data Validation**: Validação de dados testada

## Deployment

### Ambiente de Desenvolvimento
- **Local Development**: Uvicorn com reload automático
- **Hot Reload**: Recarregamento automático durante desenvolvimento

### Ambiente de Produção
- **Containerization**: Docker para containerização
- **Process Manager**: Gunicorn ou similar
- **Reverse Proxy**: Nginx para proxy reverso

## Considerações de Performance

### Otimizações Implementadas
- **Async/Await**: Operações assíncronas
- **Efficient Serialization**: Serialização otimizada com Pydantic
- **Memory Management**: Gerenciamento eficiente de memória

### Otimizações Futuras
- **Database Indexing**: Índices para consultas rápidas
- **Connection Pooling**: Pool de conexões para banco de dados
- **Caching Strategy**: Estratégia de cache inteligente

## Conclusão

A arquitetura da API foi projetada para ser simples, mas extensível, permitindo evolução futura conforme as necessidades do projeto. O uso de tecnologias modernas como FastAPI e Pydantic garante performance, segurança e facilidade de manutenção.
