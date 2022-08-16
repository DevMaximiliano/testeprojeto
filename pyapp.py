from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "teste de app do max"

        self.contatos = ["Paii"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
    def EnviarMensagens(self):
        # <span class="matched-text i0jNr">Paii</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for contatos in self.contatos:
            contatos = self.driver.find_element_by_xpath(
                f"//span[@title='(contatos)']")
            time.sleep(3)
            contatos.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botão_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botão_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
