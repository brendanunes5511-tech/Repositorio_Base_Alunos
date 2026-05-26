import pyautogui as at
def apertar_tab(qnt):

at.hotkey("win","r")# essa fução aperta duas teclas ao mesmo tempo.
at.write("mspaint", 0.2)#essa função escreve
at.press("enter")#essa função presiona a tecla
at.write("www.facebook.com", 0.1)
at.press("enter")
at.sleep(5)
email = at.prompt("digite o seu e-mail:")
at.write(email, 0.1)
apertar_tab(1)
senha = at.prompt("digite a senha: ")
at.write(senha, 0.1)
at.press("enter")