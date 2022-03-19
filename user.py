import requests
import json


class User:
    """
        Classe responsável pela manipulação da base de usuários
    """
    def __init__(self):
        self.url = 'https://retoolapi.dev/u2b8qG/api'
        self.headers = {
            "Content-Type": "text"
        }

    def adicionar_usuario(self, nome, job, email, company, interests):
        """
            Método para adicionar usuário ao banco de dados
        """
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        user_data = {
            "fullName": nome,
            "user_job": job,
            "user_email": email,
            "user_company": company,
            "user_interests": interests
        }
        reposta = requests.post(self.url, data=json.dumps(user_data), headers=headers)

        return reposta.text

    def pesquisar_usuario(self, nome):
        """
            Método para pesquisar por um usuário
        :param nome:
        :return: usuario
        """
        result = ''
        parameter = '?fullName=' + nome
        resposta = requests.get(self.url + parameter, headers=self.headers)
        if resposta.text == "[]":
            result = "User not found"
        else:
            result = resposta.text

        return result

    def listar_usuarios(self):
        """
            Função para coletar e retornar todos os usuários da base de dados
        :return: lista de usuários da base
        """
        resposta = requests.get(self.url, headers=self.headers)
        data_json = json.loads(resposta.text)
        result = []
        for item in data_json:
            result.append(item)
        return result

    def atualizar_usuario(self, id, nome, email, job, company, interests):
        """
            Função para atualização de usuário
        :param id:
        :param nome:
        :param email:
        :param job:
        :param company:
        :param interests:
        :return: usuário editado
        """

        url = self.url + "/" + str(id)
        new_data = {
            "id": str(id),
            "fullName": nome,
            "user_job" : job,
            "user_email": email,
            "user_company": company,
            "user_interests": interests
        }
        resposta = requests.put(url, data=json.dumps(new_data), headers=self.headers)
        return resposta.status_code

    def deletar_usuario(self, id):
        """
            Função que deleta usuário de acordo com seu id;
        :param id:
        :return: usuário delatado
        """
        url = self.url + "/" + str(id)
        resposta = requests.delete(url, headers=self.headers)
        if resposta.status_code == 200:
            return "User deleted"
        else:
            raise Exception(resposta.json())

    def create_dict(self):
        """
            Neste método é coletado os dados da função de listar usuários
            e os dados são processados para gerar um novo dicionário;
        :return: lista com novo dicionário de dados de usuários
        """
        data = self.listar_usuarios()
        new_dict = []
        for item in data:
            result = {
                "nome_usuario": item["fullName"],
                "email_usuario": item["user_email"],
                "cargo_usuario": item["user_job"]
            }
            new_dict.append(result)
        return new_dict


if __name__ == '__main__':
    user = User()

    # teste = user.create_dict()
    # teste = user.pesquisar_usuario('Doretta McCardle')
    teste = user.listar_usuarios()
    print(teste)

