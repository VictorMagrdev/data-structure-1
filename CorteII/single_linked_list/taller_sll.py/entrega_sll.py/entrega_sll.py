class entregasll:

    class Node:
        def __init__(self,value):
            #estructura del nodo 
            self.value = value
            self.next_node = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

#----------------------------IMPRIMIR LA LISTA ------------------------------------
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f'{node_list} Cantidad de nodos {self.length}')

#------------------------AGREGAR NODO AL INICIO--------------------------------------------------

    def append_node_start(self,value):
        new_node = self.Node(value)

        #Consultar si la lista tiene head and tail
        if self.head == None and self.tail == None:

            self.head = new_node
            self.tail = new_node
        else:
#ENLAZAR EL NODE
            new_node.next_node = self.head
            self.head = new_node
        self.length+= 1
#-----------------------AGREGAR NODO AL FINAL DE LA LISTA----------------------------------------

    def append_node_end(self,value):
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

#------------------------------ELIMINAR PRIMER NODE DE LA LIST------------------------------------------------------------

    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #delete head de la lista
            remove_node = self.head

            #El nodo que le seguia al primero pasa a ser el primero
            self.head = remove_node.next_node

            remove_node.next_node = None
            self.length -= 1
            print(f'El valor el nodo eliminado es {remove_node.value}')

#--------------------------------ELIMINAR ULTIMO ELEMENTO DE LA LISTA-------------------------------------------------------

    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #DELETE HEAD  de la lista
            current_node = self.head
    
            new_tail = current_node
            while current_node.next_node != None:
                new_tail = current_node
                current_node = current_node.next_node
            self.tail = new_tail
            self.tail.next_node = None
            self.length -= 1
            print(f'El valor el nodo eliminado es {current_node.value}') 
            
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
        
#---------------------------ACTUALIZAR VALOR DEL NODE --------------------------------------
# #Metodo que nos permite actualizar el valor del nodo
#13. Actualizar el valor de un elemento en una posición determinada de la lista simplemente 
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            print(f'Actualizando el valor del nodo ...\n           >> {search_node.value} << a\n           >>{new_value}<<')
            search_node.value = new_value
        else:
            print("     >> No se encontro el nodo <<") 

        
#---------------------------------AGREGAR VALOR DADO UN INDICE -------------------------------------------------------

    def insert(self,index,value):
        
        if index == self.length+1:
            return self.append_node(value)

        elif index == 1:
            return self.prepend_node(value)
        #Se valida si el indice esta dentro del rango  de la lista

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
#-----------------11. Eliminar un elemento en una posición determinada de la lista simplemente enlazada.--------------------------------------------------------      
    def remove_node(self, index):
        if index == 1:
            self.shift_node()
        elif index == self.length:
            self.remove_node_pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node!= None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next =remove_node
                remove_node.next = None
            else:
                print('     >> No se encontro el nodo <<')

#---------------------------------------------------------------------------------------        
#devolver el elemento en una determinada posición de la lista simplemente enlazada. Si

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

#------------#metodos que faltan por completar---------------------------
#6. Buscar un elemento en la lista simplemente enlazada y devolver su posición. No

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
#-----------------------------------------------------------------------
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

#12.---------------- Insertar un elemento en una posición determinada de la lista simplemente enlazada. --------------
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
        



