
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CVRobot(object):

    def __init__(self, user, passwd):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get("https://www.cienciavitae.pt/cv/")

        elem = self.driver.find_element_by_name("j_username")
        elem.clear()
        elem.send_keys(user)
        elem = self.driver.find_element_by_name("j_password")
        elem.clear()
        elem.send_keys(passwd)
        elem.send_keys(Keys.RETURN)

    def atividades(self):
        return Atividades(self)

class Section(object):
    def __init__(self, robot):
        self.robot = robot
        self.driver = robot.driver
        self.wait = robot.wait

    def dropdown(self, campo, valor):
        id = "%s_label"%(campo)
        elem = self.driver.find_element_by_id(id)
        elem.click()

        elem = self.driver.find_element_by_xpath("//ul[@id='%s_items']/li[contains(text(), '%s')]"%(campo,valor))
        elem = self.wait.until(EC.visibility_of(elem))
        elem.click()

        elem = self.wait.until(EC.text_to_be_present_in_element((By.ID,id),valor))

    def data(self, campo, data):
        # FIXME: Acrescentr mês e dia
        self.dropdown(campo+'_year', str(data))
        #self.dropdown(campo+'_month', ...)
        #self.dropdown(campo+'_day', ...)

    def texto(self, campo, valor):
        elem = self.driver.find_element_by_name(campo)
        elem.clear()
        elem.send_keys(str(valor))

class Atividades(Section):
    def __init__(self, robot):
        super(Atividades,self).__init__(robot)

        elem = self.driver.find_element_by_id("f_nav:atividades")
        elem.click()

    def __adicionar(self, tipo):
        elem = self.driver.find_element_by_id("f_servicos:j_idt113")
        elem.click()

        elem = self.dropdown("f_servicos:tpo_servico", tipo)

    def __confirmar(self):
        elem = self.driver.find_element_by_name("f_servicos:servicos_confirmar")
        elem.click()

    def arbitragemCientificaEmConf(self, nome, data):

        self.__adicionar("Arbitragem científica em conferência")

        self.data("f_servicos:servicos_accordion:dta_inicio_servico:dta_inicio_servico", data)
        self.data("f_servicos:servicos_accordion:dta_fim_servico:dta_fim_servico", data)

        self.texto("f_servicos:servicos_accordion:conferencias", nome)

        self.__confirmar()

    def orientacao(self, tema, nome, tipo, datai, dataf=None):

        self.__adicionar("Orientação")

        self.data("f_servicos:servicos_accordion:dta_inicio_servico:dta_inicio_servico", datai)
        if dataf: self.data("f_servicos:servicos_accordion:dta_fim_servico:dta_fim_servico", dataf)

        self.texto("f_servicos:servicos_accordion:brv_desc", tema)
        self.texto("f_servicos:servicos_accordion:nme_aluno", nome)

        self.dropdown("f_servicos:servicos_accordion:tipo_grau", tipo)

        self.__confirmar()