from random import sample 

from colorama import Fore, init 

init() 

class SortAlgorithms: 

    def __init__(self): 

        self.number_list = range(100) 

        self.list_burble_sort = sample(self.number_list, 8) 

        self.list_select_sort = sample(self.number_list, 8) 

        self.list_insert_sort = sample(self.number_list, 8) 

        self.list_merge_sort = sample(self.number_list, 8) 

        self.list_quick_sort = sample(self.number_list, 8) 

        self.list_radix_sort = sample(self.number_list, 8) 



    # Ordenamiento burbuja 

    def burble_sort_function(self): 

        # Comparación por pares, iniciamos comparando los 2 primeros elem 

        print(Fore.CYAN + "------------------------------------------" + Fore.RESET) 

        print(Fore.GREEN + '            Ordenamiento burbuja' + Fore.RESET) 

        # Crear un contador para conocer la cantidad de elementos de la lista 

        count_item_list = 0 

        # Recorremos la lista self.list_burble_sort 

        for i in self.list_burble_sort: 

            # al contador de elemntos, cada vez que visitemos una posición le sumamos 1 

            count_item_list += 1 

        print(self.list_burble_sort) 



        # Recorremos la lista e iniciamos la comparación de valor 

        print("Primer for contador - 1: ", count_item_list-1) 

        for j in range(count_item_list-1): 

            print(Fore.RED + str(j) + Fore.RESET) 

            for k in range(count_item_list-j-1): 

                print(Fore.BLUE + str(k) + ' - ' + str(k+1) + Fore.RESET) 

                # Comparamos el valor de la posición actual con el valor de la sgte 

                if self.list_burble_sort[k] > self.list_burble_sort[k+1]: 

                    # Transposición de valores 

                    self.list_burble_sort[k], self.list_burble_sort[k + 

                                                                    1] = self.list_burble_sort[k+1], self.list_burble_sort[k] 

        print(self.list_burble_sort) 



    def burble_sort_function_refactor(self): 

        change_position = True 

        while change_position: 

            change_position = False 

            for i in range(len(self.list_burble_sort)-1): 

                if self.list_burble_sort[i] > self.list_burble_sort[i+1]: 

                    self.list_burble_sort[i], self.list_burble_sort[i + 

                                                                    1] = self.list_burble_sort[i+1], self.list_burble_sort[i] 

                    change_position = True 

        print(self.list_burble_sort) 

 
 

    def select_sort_function(self): 

        # Debemos encontrar el valor menor de la lista y compararla con los demás valores 

        print(Fore.CYAN + "------------------------------------------" + Fore.RESET) 

        print(Fore.GREEN + '            Ordenamiento selección' + Fore.RESET) 

        count_item_list = 0 

        # Inicializamos el contador 

        for i in self.list_select_sort: 

            count_item_list += 1 

        print(self.list_select_sort) 

        # Recorremos la lista y generamos la comparación de valores entre posiciones 

        for i in range(count_item_list): 

            min = i 

            print(Fore.RED + str(i) + Fore.RESET) 

            for j in range(i + 1, count_item_list): 

                print(Fore.BLUE + str(j) + Fore.RESET) 

                # Comparación de valores 

                print('Comparación: ' + Fore.BLUE + str(self.list_select_sort[min]) + ' - ' + str(self.list_select_sort[j]) + Fore.RESET) 

                if self.list_select_sort[min] > self.list_select_sort[j]: 

                    min = j 

            # Generamos el intercambio, la transposición 

            # Cambiamos el elemento de menor valor de la lista con el primero 

            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i] 

            print(self.list_select_sort) 

        print(self.list_select_sort) 