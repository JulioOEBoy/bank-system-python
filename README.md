# Sistema Bancário em Python

Este repositório contém dois códigos referentes ao desenvolvimento de um sistema bancário simples em Python. Ambos realizam operações básicas como depósito, saque e visualização do extrato, mas com níveis diferentes de complexidade e organização.

---

## 1. Sistema Bancário Simples (Versão 1)

### Descrição

Programa interativo que permite ao usuário realizar depósitos, saques (com limite diário e limite por saque) e consultar o extrato. Tudo gerenciado dentro de um loop com menu.

### Funcionalidades

- Depósito de valores positivos.
- Saque com limite máximo de R$ 500, limite diário de 3 saques e saldo disponível.
- Visualização do extrato com as movimentações e saldo atual.
- Validação de entradas inválidas.

### Como usar

- Execute o programa.
- Escolha a opção no menu: [d] Depositar, [s] Sacar, [e] Extrato, [q] Sair.
- Insira os valores conforme solicitado.
- O programa imprime as mensagens e o extrato formatado conforme as operações realizadas.

---

## 2. Sistema Bancário Organizado com Funções e Cadastro de Usuários e Contas (Versão 2)

### Descrição

Versão aprimorada do sistema bancário, estruturada em funções para modularidade e com a inclusão de cadastro de usuários e contas. Mantém as funcionalidades de depósito, saque e extrato, agora vinculadas a usuários e contas.

### Funcionalidades

- Cadastro de usuários via CPF e nome.
- Cadastro de contas vinculadas a usuários cadastrados.
- Operações de depósito, saque e extrato com as mesmas regras de limite e controle.
- Interface de menu para navegação entre as opções.

### Como usar

- Execute o programa.
- Use o menu para cadastrar usuários [u] e contas [c].
- Realize depósitos [d], saques [s] e consulte o extrato [e].
- Use [q] para sair do programa.

---

## Considerações Finais

- Ambos os códigos são projetos básicos que exemplificam conceitos de controle de fluxo, manipulação de dados e funções em Python.
- A versão 2 é recomendada para quem deseja uma estrutura melhor organizada e com funcionalidades expandidas.
- Pode ser facilmente expandida para incluir mais operações bancárias e persistência de dados.

---

Feito com 💻 por Júlio César Ferreira Pedrini  
