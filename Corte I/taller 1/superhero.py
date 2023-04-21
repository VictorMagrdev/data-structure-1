from colorama import Fore,init 

class SuperheroClass:

        #se crea el metodo inicializador de la clase
        def __init__(self):
        #inicializo los atributos de la clase
            self.Superhero_list_Marvel = ''
            self.Superhero_List_DC =''
            self.value= ''
            self.index = 0
            self.menu_methods=0
            self.universe = 0 
            # inicializar metodos o funciones
            self.add_Superhero()
            self.menu_methods_f()
            self.delete_superhero()
            self.search()
            
            print(Fore.BLUE + '>>>>>>> ' + Fore.RESET+ 'listas simples ' + Fore.RESET + Fore.YELLOW + '<<<<<'+Fore.RESET )

        # FUNCION PARA PODER OBSERVAR LA LISTA 

        def menu_methods_f(self):
            self.menu_methods=int(input(Fore.RED+ ' Selecciones una opcion\n  1.Añadir  2.Eliminar'+ Fore.RESET + ' 3.Salir'+Fore.RESET+ '<<<<'+Fore.YELLOW +'>>>>>>'+ Fore.RESET))

        #FUNCION PARA AÑADIR SUPERHEROES A LA LISTA      
    

        def add_Superhero(self):
            option=int (input(Fore.CYAN+ ' Seleccione donde quiere agregar el superheroe:\n     1.Al final\n    2.Posicion especifica\n '+ Fore.RESET+ Fore.RED + '  3.salir  '+Fore.RESET+ Fore.YELLOW + '>>>>>'+Fore.RESET))

            #validar la respuesta del usuario
            while True:
                if option !=1  and option !=2  and option !=3:
                    print(Fore.RED+ '>>>>>' + Fore.RESET+ 'ERROR '+ Fore.RED+ '<<<<<<<<<'+ Fore.RESET)
                    option=int(input(Fore.CYAN+' OPCIONES:\n      1.Al final\n     2.Posicion Especifica\n '+Fore.RESET+Fore.RED+ '   3.Cancelar'+Fore.RESET+Fore.YELLOW+ '>>>>>>>>'+Fore.RESET))

                    #Insertar al final 
                elif option == 1:
                    self.universe=int(input(Fore.CYAN+ ' Seleccione el Universo\n     1.Marvel\n     2.DC\n'+Fore.RESET+Fore.YELLOW+ '>>>>>'+Fore.RESET))
                    while True:
                        if self.universe !=1 and self.universe !=2 and self.menu_methods !=3:
                            print(Fore.RED+ '>>>>>'+ Fore.RESET+ 'ERROR '+Fore.RED+'<<<<<'+Fore.RESET)
                            self.universe= int(input(Fore.CYAN+ ' Selecciona el universo:\n   1.Marvel\n     2.DC\n' + Fore.RESET+Fore.YELLOW+ '   >>>>>>>>'+Fore.RESET))

                            #si el universio que eligio fue marvel=1
                        elif self.universe ==1:
                            cant_superheroes=(int(input(Fore.CYAN+ ' Cuantos superheroes quiere añadir?\n '+Fore.RESET+Fore.YELLOW+ '<<<<<<<<<'+Fore.RESET)))
                            for item_superheroe in range (cant_superheroes):
                                self.value=input (Fore.CYAN+ 'Superheroe '+ Fore.RESET)
                            self.Superhero_list_Marvel.append(self.value)
                            print(self.Superhero_list_Marvel)
                            break

                        #si el universo que eligio fue el de Dc=2
                        else:
                            cant_superheroes= int(input(Fore.CYAN+ ' Cuantos superheroes quiere añadir?\n '+Fore.RESET+Fore.YELLOW+ '<<<<<<<<<'+Fore.RESET))
                    for item_superheroe in range (cant_superheroes):
                                self.value = input (Fore.CYAN+ 'Superheroe '+ Fore.RESET)
                                self.Superhero_List_DC.append(self.value)
                                print(self.Superhero_List_DC)
                                break
                        
                        # insertar una posicion en especifico
                elif option ==2:
                    self.universe= int (input(Fore.CYAN+ 'Seleccione el universo:\n     1.Marvel\n     2.DC\n'+Fore.RESET+Fore.YELLOW+ '>>>>>'+Fore.RESET))
                    while True:
                        if self.universe !=1 and self.universe !=2:
                            print(Fore.RED + '     >>>> ' + Fore.RESET+ 'Universo inválido' + Fore.RED + '     <<<< ' + Fore.RESET)
                            self.universe= int (input(Fore.CYAN+'    Universo:\     1.Marvel\n     2.DC\n '+Fore.RESET+Fore.YELLOW+ ' >>>>'+Fore.RESET))
                        # Si el universo seleccionado fue Marvel(1)
                        elif self.universe:
                            self.index= int(input(Fore.CYAN+ ' Indice '+Fore.RESET+Fore.YELLOW+ '>>>>>>>'+Fore.RESET))
                            while True:
                                if self.index < 0 or self.index > len(self.Superhero_list_Marvel):
                                    print(Fore.RED + '     >>>> ' + Fore.RESET+ 'Indice inválido' + Fore.RED + '     <<<< ' + Fore.RESET)
                                    self.index= int(input(Fore.CYAN + '     Indice'+ Fore.RESET + Fore.YELLOW + '     >>>> ' + Fore.RESET))
                        #si el universo seleccionado fue DC (2)
                        else:
                            self.value= input(Fore.CYAN+ '  Superheroe'+ Fore.RESET)
                            self.Superhero_list_Marvel.insert(self.index,self.value)
                            print(self.Superhero_list_Marvel)
                            break
                        break
                    
                    else:
                        
                        self.index= int (input(Fore.CYAN+ '     Indice'+ Fore.RESET + Fore.YELLOW + '     >>>> ' + Fore.RESET))
                        while True:
                            if self.index < 0 or self.index > len(self.Superhero_List_DC):
                                print(Fore.RED + '     >>>> ' + Fore.RESET+ 'Indice inválido' + Fore.RED + '     <<<< ' + Fore.RESET)
                                self.index=int (input(Fore.CYAN + '     Indice'+ Fore.RESET + Fore.YELLOW + '     >>>> ' + Fore.RESET))
                            else:   
                                self.value=(input(Fore.CYAN + '     Indice'+ Fore.RESET + Fore.YELLOW + '     >>>> ' + Fore.RESET))
                                self.Superhero_List_DC.insert (self.index,self.value)
                                print(self.Superhero_List_DC)
                                break
                            break 
                        break
                    #Salir del programa /terminar ejecucion 
                else:
                    print(Fore.RED+ '>>>>Saliendo del programa<<<<'+Fore.RESET)
                    break
                def delete_superheroe(self):
                    print('Method delete ')

                    def search (self):
                        print('Method search_f()')

                

