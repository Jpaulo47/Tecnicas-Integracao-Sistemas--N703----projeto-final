# 🚀 Guia Completo: Como Testar a API no Postman

## 📋 Pré-requisitos

1. **API rodando**: Certifique-se de que a API está executando em `http://localhost:8000`
2. **Postman instalado**: Baixe em [postman.com](https://www.postman.com/downloads/)
3. **Coleção importada**: Importe o arquivo `postman/collection.json`

## 🔧 Configuração Inicial

### 1. Importar a Coleção
```
File → Import → Selecionar postman/collection.json
```

### 2. Configurar Variáveis
```
Coleção → Variables
- base_url: http://localhost:8000
- artisan_id: (deixar vazio)
```

## 🧪 Sequência de Testes

### **Teste 1: Verificar Status da API**
- **Endpoint**: `GET /`
- **URL**: `http://localhost:8000/`
- **Resultado Esperado**: Status 200
```json
{
  "message": "Marketplace para Artesãos do Polo de Artesanato da Beira-Mar",
  "version": "1.0.0",
  "status": "online"
}
```

### **Teste 2: Cadastrar Primeiro Artesão**
- **Endpoint**: `POST /artisans`
- **URL**: `http://localhost:8000/artisans`
- **Headers**: `Content-Type: application/json`
- **Body (raw JSON)**:
```json
{
  "name": "Maria Silva",
  "craft_type": "Cerâmica"
}
```
- **Resultado Esperado**: Status 201
```json
{
  "message": "Artesão cadastrado com sucesso",
  "artisan": {
    "id": "uuid-gerado-automaticamente",
    "name": "Maria Silva",
    "craft_type": "Cerâmica"
  }
}
```
- **⚠️ IMPORTANTE**: Copie o `id` do artesão retornado!

### **Teste 3: Listar Artesãos**
- **Endpoint**: `GET /artisans`
- **URL**: `http://localhost:8000/artisans`
- **Resultado Esperado**: Status 200
```json
[
  {
    "id": "uuid-do-artesao",
    "name": "Maria Silva",
    "craft_type": "Cerâmica"
  }
]
```

### **Teste 4: Buscar Artesão por ID**
- **Endpoint**: `GET /artisans/{artisan_id}`
- **URL**: `http://localhost:8000/artisans/COLE_AQUI_O_ID_DO_TESTE_2`
- **Resultado Esperado**: Status 200
```json
{
  "id": "uuid-do-artesao",
  "name": "Maria Silva",
  "craft_type": "Cerâmica"
}
```

### **Teste 5: Cadastrar Produto para o Artesão**
- **Endpoint**: `POST /artisans/{artisan_id}/products`
- **URL**: `http://localhost:8000/artisans/COLE_AQUI_O_ID_DO_TESTE_2/products`
- **Headers**: `Content-Type: application/json`
- **Body (raw JSON)**:
```json
{
  "name": "Vaso Artesanal",
  "description": "Vaso de cerâmica feito à mão",
  "price": 150.00,
  "stock_quantity": 5
}
```
- **Resultado Esperado**: Status 201
```json
{
  "message": "Produto cadastrado com sucesso",
  "product": {
    "id": "uuid-gerado-automaticamente",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
}
```

### **Teste 6: Listar Produtos do Artesão**
- **Endpoint**: `GET /artisans/{artisan_id}/products`
- **URL**: `http://localhost:8000/artisans/COLE_AQUI_O_ID_DO_TESTE_2/products`
- **Resultado Esperado**: Status 200
```json
[
  {
    "id": "uuid-do-produto",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
]
```

### **Teste 7: Listar Todos os Produtos**
- **Endpoint**: `GET /products`
- **URL**: `http://localhost:8000/products`
- **Resultado Esperado**: Status 200
```json
[
  {
    "id": "uuid-do-produto",
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5,
    "artisan_id": "uuid-do-artesao"
  }
]
```

## 🧪 Testes de Erro

### **Teste 8: Tentar Cadastrar Produto para Artesão Inexistente**
- **Endpoint**: `POST /artisans/artesao-inexistente/products`
- **URL**: `http://localhost:8000/artisans/artesao-inexistente/products`
- **Body**: Mesmo JSON do Teste 5
- **Resultado Esperado**: Status 404
```json
{
  "error": "Artesão com ID artesao-inexistente não encontrado",
  "status_code": 404,
  "timestamp": "2025-08-25T..."
}
```

### **Teste 9: Tentar Cadastrar Artesão com Dados Inválidos**
- **Endpoint**: `POST /artisans`
- **URL**: `http://localhost:8000/artisans`
- **Body (raw JSON)**:
```json
{
  "name": ""
}
```
- **Resultado Esperado**: Status 422 (Validation Error)

### **Teste 10: Tentar Cadastrar Produto com Preço Negativo**
- **Endpoint**: `POST /artisans/{artisan_id}/products`
- **URL**: `http://localhost:8000/artisans/COLE_AQUI_O_ID_DO_TESTE_2/products`
- **Body (raw JSON)**:
```json
{
  "name": "Produto Inválido",
  "description": "Descrição",
  "price": -50.00,
  "stock_quantity": 5
}
```
- **Resultado Esperado**: Status 422 (Validation Error)

## 🔄 Fluxo Completo de Teste

### **Cenário: Cadastrar Múltiplos Artesãos e Produtos**

1. **Cadastrar Artesão 1**:
```json
{
  "name": "João Santos",
  "craft_type": "Madeira"
}
```

2. **Cadastrar Produto para Artesão 1**:
```json
{
  "name": "Cadeira de Balanço",
  "description": "Cadeira artesanal de madeira maciça",
  "price": 450.00,
  "stock_quantity": 3
}
```

3. **Cadastrar Artesão 2**:
```json
{
  "name": "Ana Costa",
  "craft_type": "Bordado"
}
```

4. **Cadastrar Produto para Artesão 2**:
```json
{
  "name": "Toalha de Mesa",
  "description": "Toalha bordada à mão",
  "price": 120.00,
  "stock_quantity": 8
}
```

5. **Listar Todos os Produtos** - Deve retornar 2 produtos

## 📊 Verificação dos Resultados

### **Status Codes Esperados:**
- **200**: Sucesso (GET)
- **201**: Criado com sucesso (POST)
- **404**: Não encontrado
- **422**: Erro de validação

### **Estrutura das Respostas:**
- Todas as respostas devem ser JSON válido
- IDs devem ser UUIDs válidos
- Preços devem ser números positivos
- Quantidades devem ser números inteiros não-negativos

## 🎯 Dicas Importantes

1. **Copie os IDs**: Sempre copie os IDs retornados para usar nos próximos testes
2. **Verifique Headers**: Certifique-se de que `Content-Type: application/json` está presente
3. **Teste Cenários de Erro**: Não esqueça de testar casos de erro
4. **Use Variáveis**: Configure as variáveis da coleção para facilitar os testes
5. **Documentação**: Acesse `http://localhost:8000/docs` para ver a documentação Swagger

## 🚨 Solução de Problemas

### **API não responde:**
- Verifique se está rodando: `python run.py`
- Confirme a URL: `http://localhost:8000`

### **Erro 422:**
- Verifique se o JSON está válido
- Confirme se todos os campos obrigatórios estão presentes

### **Erro 404:**
- Verifique se o ID do artesão está correto
- Confirme se o artesão foi cadastrado primeiro

### **Erro de Conexão:**
- Verifique se a API está rodando
- Confirme se a porta 8000 está livre
