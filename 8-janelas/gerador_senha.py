# Importando a biblioteca e nomeando de tk
import tkinter as tk
import random
import string

ALTURA = "450"
LARGURA = "400"

#==================================
# 7. Funções do Sistema (A Lógica)
#==================================

def gerar_senha():
    try:
        tamanho = int(entry_tamanho_senha.get())
        # Verificando se a quantidade de caracteres definida é menor do que 4 
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: Mínimo de 4 caracteres!",
                fg="#ff5555"
            )
            return
        
        caracteres = ""
        if var_maiusculas.get():
            caracteres += string.ascii_uppercase
        if var_minusculas.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation
        
        if not caracteres:
            lbl_resultado.config(
                text = "Erro: Selecione ao menos uma opção!",
                fg = "#ff5555"
            )
            return

        senha = "".join(random.choice(caracteres) for i in range(tamanho))

        lbl_resultado.config(
            text= f"Senha: {senha}",
            fg= "#50fa7b"
       )

    

    except ValueError:
        lbl_resultado.config(
            text = "Erro: Digite um número válido!",
            fg = "#ff5555"
            )

def copiar_senha():
    texto_resultado = lbl_resultado.cget("text")

    if "Senha: " in texto_resultado:
        senha_pura = texto_resultado.replace("Senha: ","")

        janela.clipboard_clear()
        janela.clipboard_append(senha_pura)
    else:
        lbl_status_copia.config(
            text ="É necessário gerar uma senha primeiro!",
            fg = "#ff5555" 
        )

#===================================
#1. Configuração da Janela Principal
#===================================
janela = tk.Tk()
janela.title("Senha Segura")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#295764")



# 2. Título principal do aplicativo
titulo = tk.Label(
    text="Gerador de Senhas",
    font=("Modern no. 20",18,"bold"),
    bg="#295764",
    fg="#0c2e02"
)
titulo.pack(pady=20)

#3. Label Tamnho Senha
lbl_tamanho_senha = tk.Label(
    text="Tamanho da Senha",
    font=("Arial",11),
    bg="#295764",
    fg="#cccccc"
)
lbl_tamanho_senha.pack(pady=15)

#4. Entrada Tamanho Senha
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Arial",12),
    justify="center"
)
entry_tamanho_senha.pack(pady=5)

#5. Criando as variáveis de controle True or False
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=False)
var_simbolos = tk.BooleanVar(value=False)

#5. Criando as caixinhas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiúscula (A-Z)",
    variable=var_maiusculas,
    bg="#295764",
    fg="#cccccc",
    selectcolor="#295764",
    activebackground="#295764",
    activeforeground="#cccccc"
)
chk_maiuscula.pack(anchor="w", padx=60,pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minúsculas (a-z)",
    variable=var_minusculas,
    bg="#295764",
    fg="#cccccc",
    selectcolor="#295764",
    activebackground="#295764",
    activeforeground="#cccccc"
)
chk_minuscula.pack(anchor="w", padx=60,pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text="Números (0-9)",
    variable=var_numeros,
    bg="#295764",
    fg="#cccccc",
    selectcolor="#295764",
    activebackground="#295764",
    activeforeground="#cccccc"
)
chk_numero.pack(anchor="w", padx=60,pady=2)

chk_simbolo = tk.Checkbutton(
    janela,
    text="Caracteres Especiais (!@#$%¨&*)",
    variable=var_simbolos,
    bg="#295764",
    fg="#cccccc",
    selectcolor="#295764",
    activebackground="#295764",
    activeforeground="#cccccc"
)
chk_simbolo.pack(anchor="w", padx=60,pady=2)

# 6. Criar botão gerador de senha 
btn_gerar = tk.Button(
    janela,
    text="Gerar senha segura",
    command=gerar_senha,
    bg="#0c2e02",
    fg="#cccccc",
    padx=10,
    pady=5
)
btn_gerar.pack(pady=15)

# Label que apresenta o resultado no programa
lbl_resultado = tk.Label(
    janela,
    text="A senha aparecerá aqui",
    font=("Arial",11,"bold"),
    bg="#295764",
    fg="#cccccc" 
)
lbl_resultado.pack(pady=5)

btn_copiar = tk.Button(
    janela,
    text = "Copiar",
    command=copiar_senha,
    font=("Arial",10,"bold"),
    bg="#918989",
    fg="#cccccc",
    padx= 10,
    pady= 3
)
btn_copiar.pack(pady=5)

lbl_status_copia = tk.Label(
    janela,
    text="",
    font=("Arial,9"),
    bg="#295764",
    fg="#cccccc"    
)
lbl_status_copia.pack(pady=2)

janela.mainloop()