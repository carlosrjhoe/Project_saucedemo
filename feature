Feature: Tela de Login - Laboratórios Swag
  Como usuário do sistema
  Quero me autenticar na tela de login
  Para acessar as funcionalidades do sistema

  Background:
    Dado que estou na tela de login

  Scenario: Login com usuário padrão válido
    Quando eu informar o nome de usuário "usuário_padrão"
    E a senha "molho_secreto"
    E clicar em "Conecte-se"
    Então devo acessar o sistema com sucesso

  Scenario: Login com usuário bloqueado
    Quando eu informar o nome de usuário "usuário_bloqueado"
    E a senha "molho_secreto"
    E clicar em "Conecte-se"
    Então devo visualizar a mensagem de erro "Usuário bloqueado"

  Scenario: Login com usuário com problemas de desempenho
    Quando eu informar o nome de usuário "usuário_problema_desempenho"
    E a senha "molho_secreto"
    E clicar em "Conecte-se"
    Então devo visualizar lentidão no carregamento do sistema

  Scenario: Login com usuário que gera falha
    Quando eu informar o nome de usuário "falha_usuário"
    E a senha "molho_secreto"
    E clicar em "Conecte-se"
    Então devo visualizar a mensagem de erro "Falha no login"

  Scenario: Login com usuário de erro visual
    Quando eu informar o nome de usuário "erro_usuário_visual"
    E a senha "molho_secreto"
    E clicar em "Conecte-se"
    Então devo visualizar erros visuais na interface do sistema

  Scenario: Login com credenciais inválidas
    Quando eu informar o nome de usuário "invalido"
    E a senha "senha_errada"
    E clicar em "Conecte-se"
    Então devo visualizar a mensagem "Nome de usuário ou senha incorretos"
