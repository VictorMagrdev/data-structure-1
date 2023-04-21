class SingleLinkedList:
    #Creamos una clase anidada
    class Node:
        #Creamos el metodo ejecutor
        def __init__(self,value):
            #Definimos la estructura de un nodo
            self.value = value
            self.next_node = None
#-------------------------------------------------------------------------------
        #Metodo inicialisador de la clase Single Linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.add_text_to_list()
        self.menu()

#-------------------------------------------------------------------------------
    #Metodo que imprime la lista simplemente enlasada
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f'{node_list} Cantidad de nodos {self.length}')
#-------------------------------------------------------------------------------
    #Metodo que agrega un nodo nuevo al inicio a la lista
    def prepend_node(self,value):
        new_node = self.Node(value)
        #Consultar si la lista tiene head and tail
        if self.head == None and self.tail == None:
            #En caso de que la lista este vacia, no contiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso, la lista contiene al menos un nodo
            #para este caso habria que enlazar el nodo en si
            new_node.next_node = self.head
            self.head = new_node
        self.length+= 1
    #Añadir valor al final de la lista
    def append_node(self,value):
        new_node = self.Node(value)
        #Consultar si la lista tiene head and tail
        if self.head == None and self.tail == None:
            #En caso de que la lista este vacia, no contiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso, la lista contiene al menos un nodo
            #para este caso habria que enlazar el nodo en si
            self.tail.next_node = new_node
            self.tail = new_node
        self.length+= 1
#-------------------------------------------------------------------------------
    #Eliminar el primer nodo de una lista
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #Eliminar la cabesa de la lista
            remove_node = self.head
            #El nodo que le seguia al primero pasa a ser el primero
            self.head = remove_node.next_node
            #Eliminamos el enlace que se removera de la lista
            remove_node.next_node = None
            self.length -= 1
            print(f'El valor el nodo eliminado es {remove_node.value}')
#-------------------------------------------------------------------------------
    #Eliminamos el ultimo elemento de la lista 
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #Eliminar la cabesa de la lista
            current_node = self.head
            #Creamos una nueva variableque asignara el nuevo valor de cola
            new_tail = current_node
            while current_node.next_node != None:
                new_tail = current_node
                current_node = current_node.next_node
            self.tail = new_tail
            self.tail.next_node = None
            self.length -= 1
            print(f'El valor el nodo eliminado es {current_node.value}') 
#-------------------------------------------------------------------------------           
    def reverse_list(self):
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        while current_node != None:
            next_node =current_node.next_node
            current_node.next_node = reverse_nodes
            reverse_nodes = current_node
            current_node = next_node
        self.head = reverse_nodes
        return
#-------------------------------------------------------------------------------      
    #Consultar el valor de un nodo
    def get(self,index):
        #Si el indice es el ultimo nodo de la lista nos referimos a la cola
        if index == self.length-1:
            print (self.tail.value)
            return self.tail    

        #Si el indice es el primer valor de la lista, devolvemos el valor de la cabeza
        elif index == 0:
            print(self.head.value)
            return self.head
        
        #De lo contrario, es por que el indice esta en una posicion intermedia
        #Validar que el indice se encuentre en los valores permitidos de la lista
        elif not (index >= self.length or index < 0):
            current_node = self.head
            contador = 0
            #Recorremos la lista siempre y cuando el contador sea diferente del nodo a buscar
            while contador != index:
                #Incrementamos en uno el while para visitar el siguiente nodo
                current_node = current_node.next_node
                contador += 1
            return current_node
        else:
            print('El indice no pertenece la la lista')
            return None
#-------------------------------------------------------------------------------       
    #Metodo que nos permite actualizar el valor del nodo
    def update(self,index,value):
        #Cambia el valor del un noda dado en un index
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            #Reemplazamos el valor actual del nodo suministrado por el usuario
            nodo_objetivo.value = value
        else:
            return None
#-------------------------------------------------------------------------------       
    #Agrega un elemnto en donde sea en la lista dado un index
    def insert(self,index,value):
        #Siempre que se desee crear un nuevo nodo se le solicita el valor 
        #Si el usuario quiere añadir el nodo al final de la lista se llama a la funcion
        if index == self.length+1:
            return self.append_node(value)
        #Se valida el si se valida al inicio de la lista
        elif index == 1:
            return self.prepend_node(value)
        #Se valida si el indice esta dentro de los rangos de la lista
        elif not index >= self.length+1 or index <= 0:
            new_node = self.Node(value)
            nodos_anteriores = self.get(index-2)
            nodos_siguientes = nodos_anteriores.next_node
            #Generamos los enlaces del nuevo nodo con el anterior y el siguiente
            nodos_anteriores.next_node = new_node
            new_node.next_node = nodos_siguientes
            self.length += 1
        else:
            return None
#-------------------------------------------------------------------------------
        
    def remove(self,index):
        #Saca un emento de la lista dado un indice
        if index == 1:
            return self.shift_node()
        elif index == self.length+1:
            return self.pop_node()
        elif not index > self.length or index < 1:
            nodos_anteriores = self.get(index-2)
            nodo_removido = nodos_anteriores.next_node
            nodos_anteriores.next_node = nodo_removido.next_node
            nodo_removido.next_node = None
            self.length -= 1
            return nodo_removido
        else:
            return None
        
    def add_text_to_list(self):
        with io.open('texto_prueba.txt','r+',encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while file_line != '':
                self.append_node(file_line)
                file_line = data_file.readline()
        data_file.close()
 #-------------------------------------------------------------------------------       
    def menu(self):
        print('>>>>> MENU <<<<<')
        print('1.Insertar nodo al inicio de la lista')
        print('2.Insertar nodo al final de la lista')
        if self.length > 2:
            print('3.Insertar nodo en una posicion determinada')
        while True:
            try:
                opcion = int(input('Seleccion: '))
                if(opcion == 1):
                    valor = input('Digite lo que desea añadir:\n   >>>')
                    self.prepend_node(valor)
                    self.show_nodes_list()
                elif(opcion == 2):
                    valor = input('Digite lo que desea añadir:\n   >>>')
                    self.append_node(valor)
                    self.show_nodes_list()
                elif(opcion == 3):
                    while True:
                        try:    
                            posicion = int(input('Digite la posicion en la cual desea añadir un nodo:\n   >>>'))
                            valor = input('Digite lo que desea añadir:\n   >>>')
                            self.insert(posicion,valor)
                            self.show_nodes_list()
                            break
                        except ValueError:
                            print('Se esperaba un valor numerico')       
                else:
                    raise ValueError
                break
            except ValueError:
                if(self.length <= 2):
                    print('Se esperaba un valor entre 1 y 2')
                else:
                    print('Se esperaba un valor entre 1 y 3')
            
        
