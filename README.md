👥 Equipe Responsável
Hugo Alexandre Carvalho Coelho Coutinho
Jeferson Machado dos Santos
Gustavo Barros Martins
📌 Introdução
O presente trabalho tem como objetivo apresentar o desenvolvimento inicial do Sistema Construbrito, uma solução tecnológica voltada para a gestão de uma loja de materiais de construção.
A proposta do sistema surgiu a partir da identificação de necessidades reais da empresa, especialmente relacionadas a:
Controle de estoque
Cadastro de clientes
Registro de vendas
Bloqueio de clientes inadimplentes
Nesta etapa, o foco foi transformar a modelagem e os requisitos levantados anteriormente em código funcional, estabelecendo a base tecnológica do projeto por meio da integração entre Python e MySQL.
🎯 Objetivo do Sistema
O sistema foi desenvolvido com o objetivo de automatizar processos internos da empresa, tornando o atendimento mais ágil e eficiente.
Principais funcionalidades:
Automatizar o cadastro de clientes
Facilitar a busca de clientes por nome
Controlar o estoque de produtos
Registrar vendas com múltiplos itens
Atualizar o estoque automaticamente após cada venda
Bloquear clientes com compras vencidas há mais de 30 dias
🛠️ Tecnologias Utilizadas
As seguintes tecnologias foram utilizadas no desenvolvimento do projeto:
Python → Linguagem principal do sistema
MySQL → Sistema de gerenciamento de banco de dados
VS Code → Ambiente de desenvolvimento
GitHub → Versionamento e armazenamento remoto do código



Equipe Responsavel 
1 - Hugo Alexandre Carvalho Coelho Coutinho
2 - Jeferson Machado dos Santos
3 - Gustavo Barros Martins

Projeto: Sistema Construbrito

1. Introdução

O presente trabalho tem como objetivo apresentar o desenvolvimento inicial do sistema Construbrito, uma solução tecnológica voltada para a gestão de uma loja de materiais de construção. A proposta do sistema surgiu a partir da identificação de necessidades reais da empresa, principalmente relacionadas ao controle de estoque, cadastro de clientes, registro de vendas e bloqueio de clientes inadimplentes.

Nesta etapa, o foco foi a transformação da modelagem e dos requisitos levantados na fase anterior em código funcional, estabelecendo a base tecnológica do projeto por meio da integração entre Python e MySQL.
2. Objetivo do Sistema
O sistema foi desenvolvido com a finalidade de automatizar processos internos da empresa, tornando o atendimento mais ágil e eficiente.
Os principais objetivos são:

automatizar o cadastro de clientes;
facilitar a busca de clientes por nome;
controlar o estoque de produtos;
registrar vendas com múltiplos itens;
atualizar o estoque automaticamente após cada venda;
bloquear clientes com compras vencidas há mais de 30 dias.
3. Tecnologias Utilizadas

Para o desenvolvimento do projeto, foram utilizadas as seguintes tecnologias:

Python → linguagem principal do sistema;
MySQL → sistema de gerenciamento de banco de dados;
VS Code → ambiente de desenvolvimento;
GitHub → versionamento e armazenamento remoto do código.

A escolha dessas tecnologias foi feita com base na facilidade de desenvolvimento e no maior domínio técnico da equipe sobre essas ferramentas.

4. Estrutura do Projeto

O sistema foi organizado de forma modular, dividido em camadas, visando maior organização e facilidade de manutenção.

Estrutura do projeto:


<img width="182" height="216" alt="{0E67F969-9AFF-48AD-BD8E-D69B393A58E5}" src="https://github.com/user-attachments/assets/fd737423-babc-43f2-9dfe-ea27f62a53a2" />

5. Funcionalidades Implementadas

Nesta etapa foram implementadas as funcionalidades centrais do sistema:

5.1 Cadastro de Clientes

Permite registrar clientes com nome e telefone.

5.2 Busca de Clientes

Permite localizar clientes pelo nome, facilitando o atendimento em cenários com grande volume de registros.

5.3 Cadastro de Produtos

Permite cadastrar produtos como parafusos, pregos, canos, martelos e outros materiais da loja.

5.4 Controle de Estoque

O sistema registra a quantidade disponível de cada produto e atualiza automaticamente o estoque após a venda.

5.5 Registro de Vendas

Permite registrar vendas contendo múltiplos produtos e quantidades diferentes.

5.6 Bloqueio por Inadimplência

Clientes com compras registradas há mais de 30 dias são automaticamente bloqueados, impedindo novas compras no crediário.

6. Paradigmas de Programação Aplicados
6.1 Programação Procedural

Aplicada principalmente no arquivo main.py, por meio do fluxo sequencial de execução do menu principal.

Exemplo:

cadastro
consulta
venda
saída do sistema
6.2 Programação Modular

O sistema foi dividido em módulos especializados:

cliente_service
produto_service
venda_service

Essa abordagem melhora a organização e favorece a manutenção do código.

6.3 Persistência de Dados

A camada de persistência foi implementada por meio da integração entre Python e MySQL, permitindo o armazenamento permanente das informações.

7. Roadmap de Desenvolvimento

Como evolução futura do sistema, estão previstos:

interface gráfica;
dashboard administrativo;
sistema de pagamentos;
relatórios de inadimplência;
histórico de compras por cliente.
8. Estado Atual do Desenvolvimento

Nesta fase, o projeto já apresenta um MVP funcional, contendo as principais funcionalidades do sistema e permitindo a demonstração prática do progresso do desenvolvimento.

O sistema já está apto para:

testes funcionais;
apresentação parcial;
demonstração do código;
evolução para novas funcionalidades.
9. Link do Repositório

Inserir aqui o link do GitHub:

https://github.com/HugoAlexandreCarvalho/construbrito-sistema







Instruções para Execução do Sistema

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
