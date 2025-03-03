# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1300,1000',
                '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

nome =  input('digite seu nome: ')
driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
# 1) Salvar nossa janela atual
janela_inicial = driver.current_window_handle
print(f'primeira janela: {janela_inicial}')
# 2) Abrir um nova janela
driver.execute_script('window.scrollTo(0,600);')
sleep(3)
botao_abrir_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir Janela']")
sleep(1)
driver.execute_script('arguments[0].click()', botao_abrir_janela)
sleep(1)
# 3) quais janelas estão abertas
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        # alterar para essa nova janela
        driver.switch_to.window(janela)
        sleep(2)
        campo_pesquisa = driver.find_element(By.ID, "campo_pesquisa")
        sleep(2)
        campo_pesquisa.send_keys(nome)
        sleep(2)
        botao_pesquisar = driver.find_element(By.ID, "fazer_pesquisa")
        sleep(2)
        botao_pesquisar.click()
        sleep(2)
        driver.close()
driver.switch_to.window(janela_inicial)

input('')