# 🐚 Exemplos de Teste com cURL

## 📋 Pré-requisitos
- API rodando em `http://localhost:8000`
- cURL instalado (já vem no Windows 10/11, macOS e Linux)

## 🧪 Sequência de Testes com cURL

### **1. Verificar Status da API**
```bash
curl -X GET http://localhost:8000/
```

### **2. Cadastrar Artesão**
```bash
curl -X POST http://localhost:8000/artisans \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Maria Silva",
    "craft_type": "Cerâmica"
  }'
```

### **3. Listar Artesãos**
```bash
curl -X GET http://localhost:8000/artisans
```

### **4. Buscar Artesão por ID** (substitua {ID} pelo ID retornado no passo 2)
```bash
curl -X GET http://localhost:8000/artisans/{ID}
```

### **5. Cadastrar Produto** (substitua {ID} pelo ID do artesão)
```bash
curl -X POST http://localhost:8000/artisans/{ID}/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Vaso Artesanal",
    "description": "Vaso de cerâmica feito à mão",
    "price": 150.00,
    "stock_quantity": 5
  }'
```

### **6. Listar Produtos do Artesão** (substitua {ID} pelo ID do artesão)
```bash
curl -X GET http://localhost:8000/artisans/{ID}/products
```

### **7. Listar Todos os Produtos**
```bash
curl -X GET http://localhost:8000/products
```

## 🧪 Testes de Erro

### **8. Tentar Cadastrar Produto para Artesão Inexistente**
```bash
curl -X POST http://localhost:8000/artisans/artesao-inexistente/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Produto Teste",
    "description": "Descrição",
    "price": 100.00,
    "stock_quantity": 10
  }'
```

### **9. Tentar Cadastrar Artesão com Dados Inválidos**
```bash
curl -X POST http://localhost:8000/artisans \
  -H "Content-Type: application/json" \
  -d '{
    "name": ""
  }'
```

### **10. Tentar Cadastrar Produto com Preço Negativo**
```bash
curl -X POST http://localhost:8000/artisans/{ID}/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Produto Inválido",
    "description": "Descrição",
    "price": -50.00,
    "stock_quantity": 5
  }'
```

## 🔄 Fluxo Completo Automatizado

### **Script para Windows (PowerShell)**
```powershell
# 1. Verificar status
curl http://localhost:8000/

# 2. Cadastrar artesão
$artisan = curl -X POST http://localhost:8000/artisans -H "Content-Type: application/json" -d '{"name": "João Santos", "craft_type": "Madeira"}' | ConvertFrom-Json
$artisanId = $artisan.artisan.id

# 3. Cadastrar produto
curl -X POST "http://localhost:8000/artisans/$artisanId/products" -H "Content-Type: application/json" -d '{"name": "Cadeira de Balanço", "description": "Cadeira artesanal", "price": 450.00, "stock_quantity": 3}'

# 4. Listar produtos
curl http://localhost:8000/products
```

### **Script para Linux/macOS (Bash)**
```bash
#!/bin/bash

# 1. Verificar status
curl http://localhost:8000/

# 2. Cadastrar artesão
ARTISAN_RESPONSE=$(curl -s -X POST http://localhost:8000/artisans \
  -H "Content-Type: application/json" \
  -d '{"name": "João Santos", "craft_type": "Madeira"}')

ARTISAN_ID=$(echo $ARTISAN_RESPONSE | grep -o '"id":"[^"]*"' | cut -d'"' -f4)

# 3. Cadastrar produto
curl -X POST "http://localhost:8000/artisans/$ARTISAN_ID/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Cadeira de Balanço", "description": "Cadeira artesanal", "price": 450.00, "stock_quantity": 3}'

# 4. Listar produtos
curl http://localhost:8000/products
```

## 📊 Verificação dos Resultados

### **Status Codes Esperados:**
- **200**: Sucesso (GET)
- **201**: Criado com sucesso (POST)
- **404**: Não encontrado
- **422**: Erro de validação

### **Para Formatação JSON Bonita:**
```bash
# Windows (PowerShell)
curl http://localhost:8000/artisans | ConvertFrom-Json | ConvertTo-Json -Depth 10

# Linux/macOS
curl http://localhost:8000/artisans | python -m json.tool
```

## 🎯 Dicas para cURL

1. **Use aspas duplas** para JSON no Windows
2. **Use aspas simples** para JSON no Linux/macOS
3. **Escape caracteres especiais** quando necessário
4. **Use -v** para ver detalhes da requisição: `curl -v http://localhost:8000/`
5. **Use -s** para modo silencioso (sem progress bar)

## 🚨 Solução de Problemas

### **Erro de Conexão:**
```bash
# Verificar se a API está rodando
curl http://localhost:8000/
```

### **Erro de JSON:**
```bash
# Validar JSON online: jsonlint.com
# Ou usar jq para validar: echo '{"test": "value"}' | jq .
```

### **Erro de Encoding:**
```bash
# Windows: Use UTF-8
chcp 65001

# Linux/macOS: Já vem configurado
```
