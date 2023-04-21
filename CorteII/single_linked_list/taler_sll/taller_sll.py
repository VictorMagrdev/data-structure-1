from re import search

class tallersll:
    #crear la clase

    class Node:
        #crear metodo para ejecutar
        def __init__(self,value):
            #estructural del nodo
            self.value =value
            self.next=None
            
    #metodo para poder inicializar la lase taller_sll
        def __init__(self):
            self.head= None
            self.tail =None
            self.lenght=0
#--------------------------------------------------------------------
#0 imprimir la lista 
        def show_list(self):
            array_with_nodes_value=list()
            current_node=self.head
            while(current_node!=None):
                array_with_nodes_value.__add__(current_node.value)
                current_node=current_node.next
                print(array_with_nodes_value)
#-----------------------------------------------------------------------
#1. Agregar un elemento al principio de la lista simplemente enlazada

    def add_node(self,value):
        new_node=self.Node(value) 
        #Consultamos si la lista tiene head y tail 
        if self.head== None and self.tail == None:   
            #Si la lista esta vacia se deben crear nuevos nodos
            self.head=new_node
            self.tail=new_node
        else:
            #Si la lista tiene un nodo se debe enlazar 
            new_node.next_node=self.head
            self.head=new_node
            self.lenght +=1 

#-----------------------------------------------------------------------
#2. Agregar un elemento al final de la lista simplemente enlazada

    def app_node(self,value):
        new_node=self.Node(value)
        if self.head == None and self.tail== None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next_node=self.tail
            self.tail=new_node
            self.lenght +=1 
#-------------------------------------------------------------------------
#3. Eliminar el primer elemento de la lista simplemente enlazada. 
#shift _node_sll para eliminar el primer elemento de la lista lo nombre delete 

    def delete_node (self):
        if self.lenght ==0: 
            self.head=None
            self.tail=None
        else: #Eliminar la cabeza de la lista 
            remove_node=self.head
            #El nodo que esta despues de la cabeza pasa a ser la cabeza (primer nodo)
            self.head= remove_node.next_node
            #Se debe eliminar el enlace para poderlo remover de la lista 
            remove_node.next_node=None
            self.lenght -=1 
            #Imprimir para saber cual fue el nodo que se elimino 
            print(f'El valor del nodo que fue eliminado es{remove_node.value}')
#-------------------------------------------------------------------------
#4. Eliminar el último elemento de la lista simplemente enlazada. 

    def pop_node(self):
        if self.lenght ==0:
            self.head=None
            self.tail=None
        else: #se debe eliminar la cabeza de la lista 
            current_node=self.head
            #Crear la variable que asignara el valor de tail
            new_tail=current_node
            while current_node.next_node!= None:
                new_tail=current_node
                current_node=current_node.next_node
                self.tail=new_tail
                self.tail.next_node=None
                self.lenght -=1
                print(f'El valor del nodo que se elimino fue {current_node.value}')
#------------------------------------------------------------------------------------
#5. Obtener el tamaño de la lista simplemente enlazada. No
    
    def show__nodes_List(self):
        node_list=[]
        current_node=self.head
        while(current_node != None):
            node_list.append(current_node.value)
            current_node=current_node.next_node
            print(f'{node_list}La cantidad de Nodos{self.lenght}')

#------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------
#7. Devolver el elemento en una determinada posición de la lista simplemente enlazada. 
#nodo previo = nodo_previos
#nodo removido = node_remove

    def remove(self,index):
        if index==1:
            return self.delete_node()
        elif index==self.lenght+1:
            return self.pop_node()
        elif not index >self.length or index <1:
            node_previous=self.get(index-2)
            node_remove=node_previous.next_node
            node_previous.next_node=node_remove.next_node
            node_remove.next_node=None
            self.lenght -=1
            return node_remove
        else:
            return None
#-------------------------------------------------------------------------------------------------
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
        
#---------------------------------------------------------------------------------------------
#9. Eliminar todos los elementos de la lista simplemente enlazada. No

#Establecer el primer nodo de la lista enlazada como el nodo actual.
    def delete_node(self):
        current_node=self.add_node
        while current_node:
            node_siguiente =current_node.node_siguiente
            delete_node=current_node
            current_node=node_siguiente
            self.add_node=None

#----------------------------------------------------------------------------------------------
#10. Ordenar los elementos de la lista simplemente enlazada. No

#ordenar los elementos de la lista utilizando el algoritmo de seleccion
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
#-------------------------------------------------------------------------------------------------
#11. Eliminar un elemento en una posición determinada de la lista simplemente enlazada. Si
    def remove(self,index):
        if index==1:
            return  self.delete_node()
        elif index==self.lenght+1:
            return self.pop_node()
        elif not index > self.lenght or index <1:
            node_previous =self.get(index-2)
            node_remove=node_previous.next_node
            node_previous.next_node=node_remove.next_node
            node_remove.next_node =None
            self.lenght-=1
            return node_remove
        else:
            return None
        
#-------------------------------------------------------------------------------------------------
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









#--------------------------------------------------------------------------------------------
#13. Actualizar el valor de un elemento en una posición determinada de la lista simplemente enlazada. Si

    def update(self,index,value):
        #CAMBIAR EL VALOR DEL NODE DANDO UN INDEX
        node_objective=self.get(index)
        if node_objective != None:
            #reemplazar el node actual por el que ingreso el usuario 
            node_objective.value=value
            return None