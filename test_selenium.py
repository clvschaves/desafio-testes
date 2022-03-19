import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures('browser')
class BasicTest:
    pass


class TestSelenium(BasicTest):
    def setup(self):
        self.action = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 20)

    @pytest.mark.text_verify
    def test_verify_text(self):
        """
            Verificando a busca por um texto específico
        :return:
        """
        url = 'http://uitestingplayground.com/verifytext'
        self.browser.get(url)
        elemento = self.browser.find_element(By.CLASS_NAME, 'bg-primary')
        assert elemento.text == 'Welcome UserName!'

    def test_text_input(self):
        """
            Verificanoo se o nome do botão é modificado após a entrada de dados
        :return:
        """
        url = 'http://uitestingplayground.com/textinput'
        self.browser.get(url)
        self.browser.find_element(By.ID, 'newButtonName').send_keys('Teste')
        botao = self.browser.find_element(By.ID, 'updatingButton')
        botao.click()

        assert botao.text == 'Teste'

    def test_load_delay(self):
        """
            Verificando se a página correta é aberta após delay
        :return:
        """
        url = 'http://uitestingplayground.com'
        self.browser.get(url)
        self.browser.find_element(By.XPATH, '//*[@id="overview"]/div/div[1]/div[4]/h3/a').click()
        self.wait.until(EC.element_to_be_clickable((By. XPATH, '/html/body/section/div/button')))
        page = self.wait.until(EC.title_is('Load Delays'))

        assert page, self.browser.title

    def test_mouse_over(self):
        """
            Verificando se o duplo click é contabilizado corretamente
        :return:
        """
        url = 'http://uitestingplayground.com/mouseover'
        self.browser.get(url)
        self.action.double_click(self.browser.find_element(By.CLASS_NAME, 'text-primary')).perform()
        result = self.browser.find_element(By.ID, 'clickCount').text
        assert result == '2', result

    def test_sample_app(self):
        """
            Verificando se ocorre a submissão de dados com sucesso
        :return:
        """
        url = 'http://uitestingplayground.com/sampleapp'
        self.browser.get(url)
        self.browser.find_element(By.NAME, 'UserName').send_keys('Usuario')
        self.browser.find_element(By.NAME, 'Password').send_keys('pwd')
        self.browser.find_element(By.ID, 'login').click()
        result = self.browser.find_element(By.ID, 'loginstatus').text
        assert result == 'Welcome, Usuario!'

    def test_client_side_delay(self):
        """
            Verificando se mensagem aparece após aguardar delay ao clicar em botão
        :return:
        """
        url = 'http://uitestingplayground.com/clientdelay'
        self.browser.get(url)
        self.browser.find_element(By.ID, 'ajaxButton').click()
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bg-success'), 'Data calculated on the client side.'))
        element = self.browser.find_element(By.CLASS_NAME, 'bg-success')
        assert element.text == 'Data calculated on the client side.', element.text

    def test_dynamic_id(self):
        """
            Verificando se o id do botão se modifica quando a página é atualizada
        :return:
        """
        url = 'http://uitestingplayground.com/dynamicid'
        self.browser.get(url)
        botao1 = self.browser.find_element(By.XPATH, '//button[contains(normalize-space(@class),"btn-primary")]').get_attribute('id')
        self.browser.refresh()
        botao2 = self.browser.find_element(By.XPATH, '//button[contains(normalize-space(@class),"btn-primary")]').get_attribute('id')
        assert botao1 != botao2, botao1
