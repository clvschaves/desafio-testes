# SELEÇÃO PÚBLICA SIMPLIFICADA DE TRANSFORMAÇÃO DIGITAL
___
## desafio-testes

# Desafio 1:

1. Utilizando a linguagem python, elabore os seguintes métodos dentro de uma classe
chamada User:
  * Adicionar;
  * Pesquisar por um usuário pelo nome;
  * Deletar um usuário pelo id;
  * Atualizar um usuário pelo id.

2. Crie um dicionário com informações dos usuários da base de dados, de acordo com
seguinte estrutura:
  ```python
  result :[ {
    ‘nome_usuario’: fullName,
    ‘email_usuario’: user_email,
    ‘cargo_usuario’: user_job
  }, ...]
  ```

3. Crie uma suíte para validar todos os métodos criados com os testes a seguir:
* Adicionar um novo usuário (com todos os dados) e confirme se o id criado foi
51;
* Pesquisar pelo usuário com id 15, retorne e valide todos os seus dados;
* Atualize o usuário com id 51 para os seguintes dados:
  * fullName: Hemerijk Cirilo
  * user_email: iwathall42@reverbnation.com
  * user_job: Database Assistent
  * user_company: Microsoft
  * user_interests: Cooking
* Delete o usuário com id 51 e confirme que o usuário não está mais na base;

4. Utilizando qualquer biblioteca de coverage, análise e reporte a cobertura dos testes
realizados em relação ao código desenvolvido.

## Dados para o desafio 1:

**Links para conexão com a API:**

**OBS.: Escolher apenas 1 dos links abaixo (indicar qual link foi escolhido antes de fazer o desafio):** 

* https://retoolapi.dev/u2b8qG/api
* https://retoolapi.dev/FschLV/api

**Estrutura dos dados:**

![picture data](https://i.ibb.co/4SmbNdP/img.png)

**Ferramentas que podem ser utilizadas:**
* Pytest;
* Unittest.

**HTTP methods endpoints:**

Method        | Endpoint
------------- | --------------
GET           | /ID/api
GET filter    | /ID/api?fullName=value
GET by id     | /ID/api/1
GET paginate  | /ID/api?_page=2&_limit=10
POST          | /ID/api
PUT           | /ID/api/1

**Obs.:** ID = id do link da api 
* ...**u2b8qG**/api
* ...**FschLV**/api


# Desafio 2:

1. Acesse o site citado anteriormente para resolver 7 desafios. **Obs.:
Cada desafio contém uma explicação do cenário que será solicitado;**
2. Crie uma suíte de testes com o Selenium reportando todos os resultados dos testes
com sucesso;

## Dados para o desafio 2:

**Link do desafio 2:**
* http://uitestingplayground.com/

**Ferramentas que podem ser utilizadas:**
* Selenium;
* Pytest;
* Unittest.
