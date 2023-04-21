from re import search


class pruebasll:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head 
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        print(array_with_nodes_value)

#------------------------------------------------------------------
#1. Agregar un elemento al principio de la lista simplemente enlazada. Si


    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1
#--------------------------------------------------------------------
#2. Agregar un elemento al final de la lista simplemente enlazada. Si
#          CREAR NODO AL FINAL DE LA LISTA 


    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1
#----------------------------------------------------------------------------------------
#3. Eliminar el primer elemento de la lista simplemente enlazada. Si

    '''Eliminar nodo al inicio de la lista'''
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -=1
#----------------------------------------------------------------------------------------
#4. Eliminar el último elemento de la lista simplemente enlazada. Si

    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print(f'Valor del nodo a eliminar es: {self.tail.value}')
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
#----------------------------------------------------------------------------------------
#7. Devolver el elemento en una determinada posición de la lista simplemente enlazada. Si
    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)
#------------------------------------------------------------------------------

#11. Eliminar un elemento en una posición determinada de la lista simplemente enlazada. Si
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll!= None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                print('     >> No se encontro el nodo <<')  







#-----------------------NO ESTA FUNCIONANDO ------ ENSAYAR DESPUES --------------------------------------------------

#5. Obtener el tamaño de la lista simplemente enlazada. No
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f'{node_list} Cantidad de nodos {self.length}')


#--------------------CONSULTAR EL VALOR DE UN NODO ---------------------------------------------------------
#seis 
    def get(self,index):
        #Cuando el indice es el ultimo nodo este es =tail
        if index == self.lenght -1:
            print(self.tail.value)
            return self.tail
        #Si el indice es el primer valor se devuelve head
        elif index ==0:
            print(self.head.value)
            return self.head
        #En caso contrario el indice deberia estar en una posicion indeterminada 
        # En este caso se debe validar que el indice se encuentre en los valores permitidos de la lista
        elif not(index>= self.lenght or index <0):
            current_node= self.head
            contador=0
            #Se debe recorrer la lista con la condicion de que el contador sea difente al nodo que se busca
            while contador != index:
                #Se implementa el while  para ver el siguiente node
                current_node=current_node.next_node
                contador+=1
                return current_node
            else:
                print('EL inidice no pertenece a la lista')
                return None




#----------------------------ENSAYAR DESPUES ---------------------------------------------------------------------
#8. Invertir la lista simplemente enlazada. No

    def reverse_list(self):
        reverse_nodes=None
        current_node=self.head
        self.tail=current_node
        while current_node!= None:
            next_node=current_node.next_node
            current_node.next_node=reverse_nodes
            reverse_nodes=current_node
            current_node=next_node
            self.head=reverse_nodes
            return

#-------------------------------------------------------------------------------------
#13. Actualizar el valor de un elemento en una posición determinada de la lista simplemente enlazada. Si
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            print(f'Actualizando el valor del nodo ...\n        >> {search_node.value} << a\n           >>{new_value}<<')
            search_node.value = new_value
        else:
            print("     >> No se encontro el nodo <<")      
#-------------------------------------------------------------------------------------
#9. Eliminar todos los elementos de la lista simplemente enlazada. No
    def delete_node(self):
        current_node=self.add_node
        while current_node:
            node_siguiente =current_node.node_siguiente
            delete_node=current_node
            current_node=node_siguiente
            self.add_node=None



#-------------------------------------------------------------------------------------
#10. Ordenar los elementos de la lista simplemente enlazada. No

def selection_sort(self):
        if self.lenght ==0:
            self.head=None
            self.tail=None
            current_node=self.head
            while current_node.next ==None:
                small_node=current_node
                next_node=current_node.next
                while next_node.value < small_node.value:
                    small_node=next_node
                    next_node=next_node.next
                    current_node.value,small_node.value=small_node.value,current_node.value
                    current_node=current_node.next

#12. Insertar un elemento en una posición determinada de la lista simplemente enlazada. No
def insert(self,value,index):
        #SPara crear un new_node se debe solicitar el valor 
        #Si el usuario quiere añadir el node al final de la lista se llama a la funcion
        if index ==self.lenght+1:
            return self.app_node(value)
        #se valida si es al inicio de la lista
        elif index==1:
            return self.add_node(value)
        #se debe validar si el indice esta dentro del rango de la lista 
        elif not index >= self.lenght+1 or index <=0:
            new_node=self.Node(value)
            node_previous=self.get(index-2)
            nodos_siguientes=node_previous.next_node
            #generar el enlace del new_node con el anterior y el siguiente
            node_previous.next_node=new_node
            new_node.next_node=nodos_siguientes
            self.lenght+=1
        else:
                return None



