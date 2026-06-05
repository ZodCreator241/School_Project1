print("Você está em uma sala escura. A luz da lua raia pela janela.")
print("Há OURO no canto da sala, junto com uma PÁ e uma CORDA.")
print("Tem uma PORTA no LESTE.")
print("Comando?")
print("Você vê uma PORTA aqui.")

# 1º comando
comando = input("> ")

if comando.upper() == "PEGAR OURO":
    print("Pegou.")

    # 2º comando
    comando = input("> ")

    if comando.upper() == "PEGAR PÁ":
        print("Pegou.")

        # 3º comando
        comando = input("> ")

        if comando.upper() == "PEGAR CORDA":
            print("Pegou.")

            # 4º comando
            comando = input("> ")

            if comando.upper() == "ABRIR PORTA":
                print("Você abriu a PORTA.")

                comando = input("> ")
                if comando.upper() == "LESTE":
                    print("Pegue sua recompensa.")
                    print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                    print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.\n")
                    print("Comando?\n")
                    comando = input("> ")

                    if comando.upper() == "NORTE":
                        print("Pegue sua recompensa.")
                        print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                        print("Você está em uma floresta. Existem caminhos para o NORTE, SUL e LESTE.\n")
                        print("Comando?\n")
                        comando = input("> ")

                        if comando.upper() == "SUL":
                            print("Pegue sua recompensa.")
                            print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                            print("Você está em uma floresta. Existem caminhos para o NORTE, SUL e OESTE.\n")
                            print("Comando?\n")
                            comando = input("> ")
                            if comando.upper() == "SUL":
                                print("Pegue sua recompensa.")
                                print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.\n")
                                print("Comando?\n")
                                comando = input("> ")

                                if comando.upper() == "LESTE":
                                    print("Pegue sua recompensa.")
                                    print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                    print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e SUL.\n")
                                    print("Comando?\n")
                                    comando = input("> ")

                                    if comando.upper() == "NORTE":
                                        print("Pegue sua recompensa.")
                                        print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                        print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.\n")
                                        print("Comando?\n")
                                        comando = input("> ")

                                        if comando.upper() == "NORTE":
                                            print("Pegue sua recompensa.")
                                            print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                            print("Você está em uma floresta. Existem caminhos para o SUL, OESTE e LESTE.\n")
                                            print("Comando?\n")
                                            comando = input("> ")

                                            if comando.upper() == "SUL":
                                                print("Pegue sua recompensa.")
                                                print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e SUL.\n")
                                                print("Comando?\n")
                                                comando = input("> ")

                                                if comando.upper() == "OESTE":
                                                    print("Pegue sua recompensa.")
                                                    print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                    print("Você está em uma floresta. Existem caminhos para o SUL, OESTE e LESTE.\n")
                                                    print("Comando?\n")
                                                    comando = input("> ")

                                                    if comando.upper() == "SUL":
                                                        print("Pegue sua recompensa.")
                                                        print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                        print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.\n")
                                                        print("Comando?\n")
                                                        comando = input("> ")

                                                        if comando.upper() == "NORTE":
                                                            print("Pegue sua recompensa.")
                                                            print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                            print("Você está em uma floresta. Existem caminhos para o LESTE, OESTE e SUL.\n")
                                                            print("Comando?\n")
                                                            comando = input("> ")

                                                            if comando.upper() == "SUL":
                                                                print("Pegue sua recompensa.")
                                                                print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                                print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.\n")
                                                                print("Comando?\n")
                                                                comando = input("> ")
                                                                if comando.upper() == "LESTE":
                                                                    print("Pegue sua recompensa.")
                                                                    print("A LUA PÁLIDA SORRI PARA VOCÊ. \n \n")
                                                                    print("Você está em uma floresta. Existem caminhos para o NORTE, OESTE e SUL.\n")
                                                                    print("Comando?\n")
                                                                    comando = input("> ")
                                                                    if comando.upper() == "LESTE":
                                                                        print("A LUA PÁLIDA SORRI LARGAMENTE.")
                                                                        print("Não há caminhos.")
                                                                        print("A LUA PÁLIDA SORRI LARGAMENTE.")
                                                                        print("O chão está macio.")
                                                                        print("A LUA PÁLIDA SORRI LARGAMENTE.")
                                                                        print("Aqui.")
                                                                        comando = input("> ")
                                                                        if comando.upper() == "CAVAR BURACO":
                                                                            print("Você cavou um buraco.")
                                                                            comando = input("> ")
                                                                            if comando.upper() == "LARGAR OURO":
                                                                                print("Você largou o ouro no buraco.")
                                                                                comando = input("> ")
                                                                                if comando.upper() == "TAPAR BURACO":
                                                                                    import time

                                                                                    def spam_congratulations():
                                                                                        for i in range(1000):
                                                                                            time.sleep(0.5)
                                                                                            print("\n")
                                                                                            print("Parabéns")
                                                                                            print("---- 40.24248 ----")
                                                                                            print("---- -121.4434 ----")
                                                                                    spam_congratulations()