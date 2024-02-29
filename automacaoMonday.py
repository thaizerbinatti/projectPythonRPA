from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import pyautogui as mouse
import pyautogui as teclado
import pyautogui as action
import pyautogui as loadTime

navegadorFake = webdriver.Chrome()
navegadorFake.get('https://totvs-torres.monday.com')
loadTime.sleep(2)

loginInput = navegadorFake.find_element(By.ID,'user_email').send_keys('thatazerb@gmail.com')
passwordInput = navegadorFake.find_element(By.ID, 'user_password').send_keys('teste')
loadTime.sleep(2)

loginButton = navegadorFake.find_element(By.CLASS_NAME,'next-button-component').click()
loadTime.sleep(8)

poolServiceButton = navegadorFake.find_element(By.CLASS_NAME, 'text-with-highlights').click()
loadTime.sleep(10)

menuButton = navegadorFake.find_element(By.CLASS_NAME, 'referenceWrapper_d8c3da695b').click()
loadTime.sleep(3)

actionsButton = navegadorFake.find_element(By.XPATH,'/html/body/span/div/div/div[1]/div[3]/div[4]/div/div/div/span').click()
loadTime.sleep(3)

buttonExcel = 'Exportar quadro para o Excel'
openExcelButton = navegadorFake.find_element(By.XPATH,f'//*[text()="{buttonExcel}"]').click()
loadTime.sleep(10)

selectOption = 'Incluir Subelementos'
checkoutButton = navegadorFake.find_element(By.XPATH,f'//*[text()="{selectOption}"]').click()
loadTime.sleep(5)

exportButton = navegadorFake.find_element(By.XPATH, '/html/body/div[55]/div/div/div/div/div/div/div[3]/button').click()
loadTime.sleep(10)

#checkoutImage = action.locateOnScreen("C:\\Users\\ctt\\Pictures\\imageCheck.png",1.5,confidence=0.7)
#checkboxButton = navegadorFake.find_elements(By.CLASS_NAME,'input_9fc46df967')
#for checkbox in checkboxButton:
#    if checkoutImage is not None:
#        checkbox.click()

