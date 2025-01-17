import flet as ft

def main(pagina: ft.Page):

    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enivar_mensagem(event):
        if campo_enviar_mensagem.value != "":
            user = p_caixa.value
            mensagem = ft.Text(f"{user}: {campo_enviar_mensagem.value}")
            pagina.pubsub.send_all(mensagem)
            campo_enviar_mensagem.value = ""
            pagina.update()

    title = ft.Text("Whatsapp", text_align="CENTER", size=32)
    pagina.add(title)

    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.START

    campo_enviar_mensagem = ft.TextField(label="Digitar mensagem...", border_color="#ffffff")
    btn_enviar = ft.Button(text=">", on_click=enivar_mensagem)

    linha_enviar =  ft.Row([campo_enviar_mensagem, btn_enviar])

    chat = ft.Column()

    def entrar_chat(event):
        if p_caixa.value == "":
            popup.open = False
            pagina.overlay.append(popup_erro)
            popup_erro.open = True
            pagina.update()
        else:
            popup_erro.open = False
            popup.open = False
            pagina.remove(title, button)
            pagina.add(chat, linha_enviar)
            user = p_caixa.value
            texto_entrou = ft.Text(f"{user} entrou no chat")
            pagina.pubsub.send_all(texto_entrou)
            pagina.update()
        

    p_title = ft.Text("Bem-vindo")
    p_caixa = ft.TextField(label="Digite seu nome", border_color="#ffffff")
    p_btn = ft.Button("Entrar", width=100, on_click=entrar_chat)

    popup = ft.AlertDialog(
        title=p_title, content=p_caixa, actions=[p_btn]
    )

    def open_popup(event):
        pagina.overlay.append(popup)
        popup.open = True
        pagina.update()



    button = ft.Button("Entrar no chat", width=150, height=40, on_click=open_popup)
    pagina.add(button)

    p2_title = ft.Text("Erro: sem nome")
    p2_btn = ft.Button("OK", width=100, on_click=open_popup)
    popup_erro = ft.AlertDialog(title=p2_title, actions=[p2_btn])

    pagina.update()

ft.app(main, view=ft.WEB_BROWSER)