import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

#imagem
from PIL import ImageTk,Image

#classes de controle =================
# ESTOQUE
class Estoque:
    def __init__(self):
        self.produtos = []

    def verificar_produto(self, produto):
        if produto in self.produtos:
            return True
        else:
            msg = CTkMessagebox(message=f"Produto {produto} não encontrado no estoque.",
              icon="cancel", option_1="Ok")
            
            return False

    def mostrar_estoque(self):
        if not self.produtos:
            mensagem = "Estoque vazio."
        else:
            mensagem = "Estoque atual:\n"
            for produto in self.produtos:
                mensagem += f"{produto}\n"
        CTkMessagebox(message=mensagem, icon="info", option_1="OK")

    def adicionar_produto_cancelado(self, produto):
        self.produtos.append(produto)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        msg = CTkMessagebox(message=f"Produto {produto} adicionado ao estoque.",
              icon="check", option_1="Thanks", option_2="Estoque")
        
        if msg.get()=="Estoque":
            self.mostrar_estoque()

    def remover_produto_pos_compra(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            msg = CTkMessagebox(message=f"Produto {produto} removido do estoque.",
              icon="check", option_1="Thanks",option_2="Estoque")
            
            if msg.get()=="Estoque":
                self.mostrar_estoque()
        else:
            msg = CTkMessagebox(message=f"Produto {produto} não encontrado no estoque.",
              icon="cancel", option_1="Thanks",option_2="Estoque")
            
            if msg.get()=="Estoque":
                self.mostrar_estoque()

    

# PEDIDOS
class FilaPedidos:
    def __init__(self):
        self.pedidos = []

        # IMPLEMENTAÇÃO 
        self.pilha_vendas = PilhaVendas()

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        CTkMessagebox(message=f"Pedido '{pedido}' adicionado ao carrinho.",
                icon="check", option_1="Thanks")
        

    def processar_pedido(self):
        global vendas
        if self.pedidos:
            pedido_venda = self.pedidos[0]
            self.pilha_vendas.registrar_venda(pedido_venda)
            if self.pedidos:
                pedido = self.pedidos.pop(0)
                CTkMessagebox(message=f"Pedido '{pedido}' processado com sucesso.",
                    icon="check", option_1="Thanks")
        else:
            CTkMessagebox(message="Não há pedidos para processar.",
                icon="cancel", option_1="Ok")

    def mostrar_pedidos(self):
        if not self.pedidos:
            mensagem = "Não há pedidos."
        else:
            mensagem = "Atuais pedidos:\n"
            for pedido in self.pedidos:
                mensagem += f"{pedido}\n"
        CTkMessagebox(message=mensagem, icon="info", option_1="OK")


# VENDAS
# Definindo a lista globalmente
vendas = []

# Classe PilhaVendas
class PilhaVendas:
    def registrar_venda(self, venda):
        global vendas  # Referenciando a lista global dentro do método
        vendas.insert(0, venda)

        print(vendas)
        

    def desfazer_venda(self):
        global vendas  
        if vendas:
            venda_desfeita = vendas.pop(0)
            CTkMessagebox(message=f"Venda '{venda_desfeita}' desfeita.",
                    icon="check", option_1="Ok")
            
            return True

        else:
            CTkMessagebox(message="Não há vendas para desfazer.",
                    icon="cancel", option_1="Ok")
           

    def mostrar_vendas(self):
        global vendas  
        if not vendas:
            mensagem = "Não há vendas."
        else:
            mensagem = "Atuais vendas:\n"
            for venda in vendas:
                mensagem += f"{venda}\n"
        CTkMessagebox(message=mensagem, icon="info", option_1="OK")

#  ======================================================================================================
# class PilhaVendas:
#     def __init__(self):
#         self.vendas = []

#     def registrar_venda(self, venda):
#         self.vendas.append(venda)
#         # print(f"Venda '{venda}' registrada.")

#     def desfazer_venda(self):
#         if self.vendas:
#             venda_desfeita = self.vendas.pop()
#             print(f"Venda '{venda_desfeita}' desfeita.")
#         else:
#             print("Não há vendas para desfazer.")

#     def mostrar_vendas(self):
#         if not self.vendas:
#             mensagem = "Não há vendas."
#         else:
#             mensagem = "Atuais vendas:\n"
#             for venda in self.vendas:
#                 mensagem += f"{venda}\n"
#         CTkMessagebox(message=mensagem, icon="info", option_1="OK")
    # ======================================================================================================    


class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window = self
        self.window.title("Loja")
        self.window.geometry("1050x740")
        self.window.resizable(False, False)
        ctk.set_appearance_mode("dark")

        # instâncias das classes de controle
        self.estoque = Estoque()
        self.fila_pedidos = FilaPedidos()
        self.pilha_vendas = PilhaVendas()

        self.images = {}  # Dicionário para armazenar as imagens


        self.load_images()
        self.main_screen()

        global vendas

    def load_images(self):
        img_pattern = ImageTk.PhotoImage(Image.open("imagens/pattern.png"))
        self.images['pattern'] = img_pattern
        # ----------------------------------------
        img_home = Image.open("imagens/home.png")
        img_home = img_home.resize((45,45))
        img_home = ImageTk.PhotoImage(img_home)
        self.images['home'] = img_home
        # ----------------------------------------
        img_despesa = Image.open("imagens/despesa.png")
        img_despesa = img_despesa.resize((45,45))
        img_despesa = ImageTk.PhotoImage(img_despesa)
        self.images['despesa'] = img_despesa
        # ----------------------------------------
        img_adicionar = Image.open("imagens/adicionar.png")
        img_adicionar = img_adicionar.resize((45,45))
        img_adicionar = ImageTk.PhotoImage(img_adicionar)
        self.images['adicionar'] = img_adicionar
        # ----------------------------------------
        img_lixeira = Image.open("imagens/lixeira.png")
        img_lixeira = img_lixeira.resize((45,45))
        img_lixeira = ImageTk.PhotoImage(img_lixeira)
        self.images['lixeira'] = img_lixeira
        # ----------------------------------------
        img_carrinho = Image.open("imagens/carrinho.png")
        img_carrinho = img_carrinho.resize((45,45))
        img_carrinho = ImageTk.PhotoImage(img_carrinho)
        self.images['carrinho'] = img_carrinho
        # ----------------------------------------
        img_TV = Image.open("imagens/TV.png")
        img_TV = img_TV.resize((250,250))
        img_TV = ImageTk.PhotoImage(img_TV)
        self.images['TV'] = img_TV
        # ----------------------------------------
        img_celular = Image.open("imagens/celular.png")
        img_celular = img_celular.resize((250,250))
        img_celular = ImageTk.PhotoImage(img_celular)
        self.images['celular'] = img_celular
        # ----------------------------------------
        img_maquininha = Image.open("imagens/maquininha.png")
        img_maquininha = img_maquininha.resize((250,250))
        img_maquininha = ImageTk.PhotoImage(img_maquininha)
        self.images['maquininha'] = img_maquininha
        # ----------------------------------------
        img_brinquedo = Image.open("imagens/brinquedo.png")
        img_brinquedo = img_brinquedo.resize((250,250))
        img_brinquedo = ImageTk.PhotoImage(img_brinquedo)
        self.images['brinquedo'] = img_brinquedo
        # ----------------------------------------
        img_cosmeticos = Image.open("imagens/cosmeticos.png")
        img_cosmeticos = img_cosmeticos.resize((250,250))
        img_cosmeticos = ImageTk.PhotoImage(img_cosmeticos)
        self.images['cosmeticos'] = img_cosmeticos
        # ----------------------------------------
        img_saco = Image.open("imagens/saco.png")
        img_saco = img_saco.resize((250,250))
        img_saco = ImageTk.PhotoImage(img_saco)
        self.images['saco'] = img_saco
        # ----------------------------------------
        img_iluminacao = Image.open("imagens/iluminacao.png")
        img_iluminacao = img_iluminacao.resize((250,250))
        img_iluminacao = ImageTk.PhotoImage(img_iluminacao)
        self.images['iluminacao'] = img_iluminacao
        # ----------------------------------------
        img_salto = Image.open("imagens/salto.png")
        img_salto = img_salto.resize((250,250))
        img_salto = ImageTk.PhotoImage(img_salto)
        self.images['salto'] = img_salto
        # ----------------------------------------
        img_robo = Image.open("imagens/robo.png")
        img_robo = img_robo.resize((250,250))
        img_robo = ImageTk.PhotoImage(img_robo)
        self.images['robo'] = img_robo
       
    

    def main_screen(self):
        l_pattern = ctk.CTkLabel(
            master=self.window, 
            image=self.images['pattern'])
        l_pattern.pack()
        #animação =======================================
                
        def move_frames_out(x, frame, final_x):
            if x < final_x:
                frame.place(x=x, y=60)
                x += 5  
                l_pattern.after(1, move_frames_out, x, frame, final_x)

        def move_frame_in(x, frame, final_x):
            if x > final_x:
                frame.place(x=x, y=60)
                x -= 5  
                l_pattern.after(1, move_frame_in, x, frame, final_x)

        def animate_configure():
            move_frames_out(-500, frame_carrinho, 365)
        def animate_home():
            move_frame_in(365, frame_config, -500)
            move_frame_in(365, frame_carrinho, -500)

        def animate_config():
            move_frames_out(-500, frame_config, 365)
    
        
        
        # FRAME DE CIMA =========================================
        frame_cima=ctk.CTkFrame(
            master=l_pattern, 
            width=1030, 
            height=50, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_cima.place(x=10,y=2)


        app_logo = ctk.CTkLabel(
            master=frame_cima,
            width=300,
            compound="left",
            text="LOJA",
            font=('Impact',20, "underline"))
        app_logo.place(x=350, y=7)
        
        home = ctk.CTkButton(
            master=frame_cima,
            image=self.images['home'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=animate_home
            )
        home.place(x=13, y=2)

        configuracoes = ctk.CTkButton(
            master=frame_cima,
            image=self.images['despesa'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=animate_config
            )
        configuracoes.place(x=63, y=2)

        button_estoque= ctk.CTkButton(
            master=frame_cima,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Ver estoque",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=self.estoque.mostrar_estoque
        )
        button_estoque.place(x=130, y=17)

        button_carrinho = ctk.CTkButton(
            master=frame_cima,
            image=self.images['carrinho'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=animate_configure
            )
        button_carrinho.place(x=964, y=2)

        combo_add = ctk.CTkComboBox(
            master=frame_cima,
            values=["TV", "Celular", "Cosmeticos","Iluminaria", "Saco", "Maquininha","Salto", "Robo", "Brinquedo"]
        )
        combo_add.place(x=700, y=17)

        def remover_produto_selecionado():
            produto_selecionado = combo_add.get()
            self.estoque.remover_produto(produto_selecionado)

        button_lixeira = ctk.CTkButton(
            master=frame_cima,
            image=self.images['lixeira'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=remover_produto_selecionado
            )
        button_lixeira.place(x=864, y=2)

        def adicionar_produto_selecionado():
            produto_selecionado = combo_add.get()
            self.estoque.adicionar_produto(produto_selecionado)


        button_adicionar = ctk.CTkButton(
            master=frame_cima,
            image=self.images['adicionar'],
            text="",
            width=45,
            height=45,
            fg_color="transparent",
            hover_color="#2B2B2B",
            command=adicionar_produto_selecionado
            )
        button_adicionar.place(x=914, y=2)
        # =======================================================

        frame_loja=ctk.CTkScrollableFrame(
            master=l_pattern, 
            width=995, 
            height=610, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_loja.place(x=10,y=60)

        # linha 1 ====
        img_tv = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['TV'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_tv.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")       
        
        def add_tv():
            produto = 'TV'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto)          

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_tv
        )
        button_comprar.grid(row=1, column=0, padx=5, pady=5)

        img_celular = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['celular'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_celular.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        def add_Celular():
            produto = 'Celular'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto)  

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Celular
        )
        button_comprar.grid(row=1, column=1, padx=5, pady=5)

        img_maquininha = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['maquininha'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_maquininha.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        def add_Maquininha():
            produto = 'Maquininha'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Maquininha
        )
        button_comprar.grid(row=1, column=2, padx=5, pady=5)
        # linha 2 ====
        img_saco = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['saco'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_saco.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        def add_Saco():
            produto = 'Saco'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Saco
        )
        button_comprar.grid(row=3, column=0, padx=5, pady=5)

        img_cosmeticos = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['cosmeticos'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_cosmeticos.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        def add_Cosmeticos():
            produto = 'Cosmeticos'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Cosmeticos
        )
        button_comprar.grid(row=3, column=1, padx=5, pady=5)

        img_iluminacao = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['iluminacao'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_iluminacao.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        def add_Iluminaria():
            produto = 'Iluminaria'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Iluminaria
        )
        button_comprar.grid(row=3, column=2, padx=5, pady=5)
        # linha 3
        img_brinquedo = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['brinquedo'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_brinquedo.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        def add_Brinquedo():
            produto = 'Brinquedo'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Brinquedo
        )
        button_comprar.grid(row=5, column=0, padx=5, pady=5)
        
        img_salto = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['salto'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_salto.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

        def add_Salto():
            produto = 'Salto'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Salto
        )
        button_comprar.grid(row=5, column=1, padx=5, pady=5)

        img_robo = ctk.CTkLabel(
            master=frame_loja,
            image=self.images['robo'],
            text="",
            width=300,
            height=250,
            fg_color="transparent",
            # hover_color="#2B2B2B",
            # command=carrinho
            )
        img_robo.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

        def add_Robo():
            produto = 'Robo'

            if self.estoque.verificar_produto(produto):
                self.fila_pedidos.adicionar_pedido(produto)
                self.estoque.remover_produto_pos_compra(produto) 

        button_comprar= ctk.CTkButton(
            master=frame_loja,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Adicionar ao carrinho",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            font=('Arial',15,"bold"),
            command=add_Robo
        )
        button_comprar.grid(row=5, column=2, padx=5, pady=5)
        # FRAME CONFIG =================================
        frame_config=ctk.CTkFrame(
            master=l_pattern, 
            width=500, 
            height=600, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_config.place(x=-500,y=60)

        l_configuracao = ctk.CTkLabel(
            master=frame_config,
            image=self.images['despesa'],
            width=300,
            compound="left",
            text="Vendas",
            font=('Impact',20, "underline"))
        l_configuracao.pack(padx=5, pady=20)

        def ver_vendas():
            self.pilha_vendas.mostrar_vendas()

        button_ver_vendas = ctk.CTkButton(
            master=frame_config,
            width=30,
            height=20,
            bg_color= "transparent",
            fg_color="black",
            corner_radius=15,
            text="Ver vendas",
            text_color="white",
            hover_color="#d1c7c7",
            border_color= "white",
            border_width=1,
            command=ver_vendas,
            font=('Arial',15,"bold"))
        button_ver_vendas.pack(padx=5, pady=30)

        global vendas
        
    
        def cancel_venda():
            global vendas
            if vendas:
                produto_cancelado = vendas[0]
                print(produto_cancelado)
                self.estoque.adicionar_produto_cancelado(produto_cancelado)

                if self.pilha_vendas.desfazer_venda():
                    return True
            else:
                CTkMessagebox(message="Não há vendas para desfazer.",
                        icon="cancel", option_1="Ok")
                



        button_cancelar_venda = ctk.CTkButton(
            master=frame_config,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Cancelar venda",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            command=cancel_venda,
            font=('Arial',15,"bold"))
        button_cancelar_venda.pack(padx=5, pady=40)

        # FRAME DO CARRINHO ===========================
        frame_carrinho=ctk.CTkFrame(
            master=l_pattern, 
            width=500, 
            height=600, 
            corner_radius=20,
            bg_color="transparent",
            border_color="black",
            border_width=2
            )
        frame_carrinho.place(x=-500,y=60)

        l_carrinho = ctk.CTkLabel(
            master=frame_carrinho,
            image=self.images['carrinho'],
            width=300,
            compound="left",
            text="Carrinho de Compras",
            font=('Impact',20, "underline"))
        l_carrinho.pack(padx=5, pady=20)

        def ver_pedidos():
            self.fila_pedidos.mostrar_pedidos()

        button_ver_pedidos = ctk.CTkButton(
            master=frame_carrinho,
            width=30,
            height=20,
            bg_color= "transparent",
            fg_color="black",
            corner_radius=15,
            text="Ver pedidos",
            text_color="white",
            hover_color="#d1c7c7",
            border_color= "white",
            border_width=1,
            command=ver_pedidos,
            font=('Arial',15,"bold"))
        button_ver_pedidos.pack(padx=5, pady=30)

        def finalizar_compra():
            self.fila_pedidos.processar_pedido()

        button_finalizar_compra = ctk.CTkButton(
            master=frame_carrinho,
            width=50,
            height=20,
            bg_color= "transparent",
            fg_color="white",
            corner_radius=15,
            text="Finalizar compra",
            text_color="black",
            hover_color="#d1c7c7",
            border_color= "black",
            border_width=1,
            command=finalizar_compra,
            font=('Arial',15,"bold"))
        button_finalizar_compra.pack(padx=5, pady=40)
        

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
