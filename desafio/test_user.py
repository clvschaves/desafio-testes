import pytest
import json
from user import User


class BasicTest:
    pass


class TestUser(BasicTest):
    @pytest.mark.parametrize(
        'id, nome, user_job, user_email, user_company, user_interests',
        [(
            15,
            "Stefania Lavall",
            "Account Executive",
            "vhefforde46@fc2.com",
            "Berkshire Hathaway",
            "Skydiving"
        )]
    )
    def test_pesquisar_usuario(self, id, nome, user_job, user_email, user_company, user_interests):
        user = User()
        resposta = json.loads(user.pesquisar_usuario(nome))
        expected = [{
            "id": id,
            "fullName": nome,
            "user_job": user_job,
            "user_email": user_email,
            "user_company": user_company,
            "user_interests": user_interests
        }]
        assert resposta == expected

    @pytest.mark.parametrize(
        'nome, user_job, user_email, user_company, user_interests',
        [(
            "José",
            "CEO",
            "jose@fc2.com",
            "Microsoft",
            "Running"
        )]
    )
    def test_adicionar_usuario(self, nome, user_job, user_email, user_company, user_interests):
        user = User()
        user.adicionar_usuario(nome, user_job, user_email, user_company, user_interests)
        resposta = json.loads(user.pesquisar_usuario(nome))
        assert resposta[0]['id'] == 51

    @pytest.mark.parametrize(
        'id, nome, user_job, user_email, user_company, user_interests',
        [(
                51,
                "Hemerijk Cirilo",
                "Database Assistent",
                "iwathall42@reverbnation.com",
                "Microsoft",
                "Cooking"
        )]
    )
    def test_atualizar_usuario(self, id,  nome, user_job, user_email, user_company, user_interests):
        user = User()
        resposta = user.atualizar_usuario(id, nome, user_email, user_job, user_company, user_interests)
        expected = 200
        assert resposta == expected

    @pytest.mark.parametrize(
        'id', [51]
    )
    def test_deletar_usuario(self, id):
        user = User()
        resposta = user.deletar_usuario(id)
        assert resposta == "User deleted"



