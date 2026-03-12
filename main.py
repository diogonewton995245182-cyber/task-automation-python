import os
import shutil
import requests
import smtplib
from email.message import EmailMessage

# ==============================
# 1 - ORGANIZAR ARQUIVOS
# ==============================

def organizar_arquivos(pasta):

    tipos = {
        "imagens": [".png", ".jpg", ".jpeg"],
        "pdf": [".pdf"],
        "documentos": [".docx", ".txt"],
        "videos": [".mp4", ".mkv"]
    }

    for arquivo in os.listdir(pasta):

        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):

            for pasta_destino, extensoes in tipos.items():

                if any(arquivo.lower().endswith(ext) for ext in extensoes):

                    destino = os.path.join(pasta, pasta_destino)

                    os.makedirs(destino, exist_ok=True)

                    shutil.move(caminho_arquivo, os.path.join(destino, arquivo))

    print("Arquivos organizados com sucesso!")


# ==============================
# 2 - RENOMEAR ARQUIVOS
# ==============================

def renomear_arquivos(pasta):

    contador = 1

    for arquivo in os.listdir(pasta):

        caminho = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho):

            extensao = os.path.splitext(arquivo)[1]

            novo_nome = f"arquivo_{contador}{extensao}"

            novo_caminho = os.path.join(pasta, novo_nome)

            os.rename(caminho, novo_caminho)

            contador += 1

    print("Arquivos renomeados!")


# ==============================
# 3 - BAIXAR DADOS DE SITE
# ==============================

def baixar_site(url):

    resposta = requests.get(url)

    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(resposta.text)

    print("Site baixado com sucesso!")


# ==============================
# 4 - ENVIAR EMAIL AUTOMÁTICO
# ==============================

def enviar_email(remetente, senha, destinatario):

    msg = EmailMessage()

    msg["Subject"] = "Relatório Automático"
    msg["From"] = remetente
    msg["To"] = destinatario

    msg.set_content("Este é um email enviado automaticamente pelo sistema.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(remetente, senha)

        smtp.send_message(msg)

    print("Email enviado!")


# ==============================
# MENU
# ==============================

def menu():

    while True:

        print("\n===== SISTEMA DE AUTOMAÇÃO =====")
        print("1 - Organizar arquivos")
        print("2 - Renomear arquivos")
        print("3 - Baixar página de site")
        print("4 - Enviar email")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pasta = input("Digite o caminho da pasta: ")
            organizar_arquivos(pasta)

        elif opcao == "2":
            pasta = input("Digite o caminho da pasta: ")
            renomear_arquivos(pasta)

        elif opcao == "3":
            url = input("Digite a URL do site: ")
            baixar_site(url)

        elif opcao == "4":
            remetente = input("Seu email: ")
            senha = input("Senha: ")
            destinatario = input("Email destinatário: ")

            enviar_email(remetente, senha, destinatario)

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


menu()
