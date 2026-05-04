
#  Sistema Construbrito

##  Equipe Responsável

- **Hugo Alexandre Carvalho Coelho Coutinho**  
  Responsável pelo levantamento de requisitos do sistema e identificação das necessidades da empresa.

- **Jeferson Machado dos Santos**  
  Responsável pelo desenvolvimento da estrutura do banco de dados e integração com o sistema.

- **Gustavo Barros Martins**  
  Responsável pela implementação das funcionalidades em Python e testes do sistema.

---

##  Introdução

O presente trabalho tem como objetivo apresentar o desenvolvimento inicial do **Sistema Construbrito**, uma solução tecnológica voltada para a gestão de uma loja de materiais de construção.

A proposta surgiu a partir da identificação de necessidades reais da empresa, principalmente relacionadas a:

- Controle de estoque  
- Cadastro de clientes  
- Registro de vendas  
- Bloqueio de clientes inadimplentes  

Nesta etapa, o foco foi a transformação da modelagem e dos requisitos levantados anteriormente em código funcional, estabelecendo a base tecnológica do projeto por meio da integração entre **Python** e **MySQL**.

---

##  Objetivo do Sistema

O sistema foi desenvolvido com o objetivo de automatizar processos internos da empresa, tornando o atendimento mais ágil e eficiente.

### Principais objetivos:

- Automatizar o cadastro de clientes  
- Facilitar a busca de clientes por nome  
- Controlar o estoque de produtos  
- Registrar vendas com múltiplos itens  
- Atualizar o estoque automaticamente após cada venda  
- Bloquear clientes com compras vencidas há mais de 30 dias  

---

##  Tecnologias Utilizadas

- **Python** → Linguagem principal do sistema  
- **MySQL** → Banco de dados  
- **VS Code** → Ambiente de desenvolvimento  
- **GitHub** → Versionamento de código  

A escolha dessas tecnologias foi baseada na facilidade de desenvolvimento e no domínio técnico da equipe.

---

##  Estrutura do Projeto

O sistema foi organizado de forma modular, visando maior organização e facilidade de manutenção.
<img width="182" height="216" alt="{0E67F969-9AFF-48AD-BD8E-D69B393A58E5}" src="https://github.com/user-attachments/assets/fd737423-babc-43f2-9dfe-ea27f62a53a2" />
---

##  Funcionalidades Implementadas

### 1. Cadastro de Clientes
Permite registrar clientes com nome e telefone.

### 2. Busca de Clientes
Permite localizar clientes pelo nome, facilitando o atendimento.

### 3. Cadastro de Produtos
Permite cadastrar produtos como parafusos, pregos, canos, martelos, entre outros.

### 4. Controle de Estoque
Atualiza automaticamente a quantidade de produtos após cada venda.

### 5. Registro de Vendas
Permite registrar vendas com múltiplos produtos e quantidades.

### 6. Bloqueio por Inadimplência
Clientes com compras vencidas há mais de 30 dias são automaticamente bloqueados.

---

##  Paradigmas de Programação

### Programação Processual
Aplicada no arquivo `main.py`, com fluxo sequencial do sistema.

### Programação Modular
Divisão em módulos:

- cliente_serviço  
- produto_serviço  
- venda_serviço  

### Persistência de Dados
Integração com MySQL para armazenamento permanente das informações.

---

##  Roteiro de Desenvolvimento (Futuro)

- Interface gráfica  
- Painel administrativo  
- Sistema de pagamentos  
- Relatórios de inadimplência  
- Histórico de compras por cliente  

---

##  Estado Atual do Sistema

O sistema já se encontra em nível **MVP (Produto Mínimo Viável)**, permitindo:

- Testes funcionais  
- Apresentação parcial  
- Demonstração prática  
- Evolução para novas funcionalidades  

---

##  Link do Repositório

https://github.com/HugoAlexandreCarvalho/construbrito-sistema

---




## Instruções para Execução do Sistema

Para executar corretamente o sistema, siga os passos abaixo:

1. Instalar o Python
Certifique-se de que o Python esteja instalado no computador.

Versão recomendada: **Python 3.10 ou superior**

Para verificar a instalação, execute no terminal:

```bash
python --version
```

---

2. Instalar as Dependências
No terminal, dentro da pasta do projeto, execute:

```bash
pip install mysql-connector-python
```

---

3. Configurar o Banco de Dados MySQL
Criar o banco de dados com o seguinte comando:

```sql
CREATE DATABASE construbrito;
USE construbrito;
```

Criar as tabelas necessárias:

```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'ativo'
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    estoque INT
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    total DECIMAL(10,2),
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE itens_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    FOREIGN KEY (venda_id) REFERENCES vendas(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

---

4. Configurar a Conexão com o Banco
No arquivo `app/database/db.py`, inserir as credenciais do MySQL:

```python
host="localhost"
user="root"
password="SUA_SENHA"
database="construbrito"
```

Substituir `SUA_SENHA` pela senha configurada no MySQL.

---

5. Executar o Sistema
No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

---

6. Funcionalidades Disponíveis
Após executar, o sistema apresentará o menu com as seguintes opções:

- Cadastro de clientes
- Listagem de clientes
- Registro de vendas
- Cadastro de produtos
- Listagem de produtos
