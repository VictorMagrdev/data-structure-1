from double_linked_list import DoublyLinkedList
inst_dll = DoublyLinkedList()
inst_dll.add_node_at_end('A')
inst_dll.add_node_at_end('B')
inst_dll.add_node_at_start('C')
inst_dll.add_node_at_end('D')
inst_dll.add_node_at_end('E')
inst_dll.print_list()

inst_dll.add_node_in_position(5, "Prueba")
inst_dll.print_list()

inst_dll.add_node_in_position(1, "NewNode1")
inst_dll.add_node_in_position(2, "NewNode2")
inst_dll.print_list()

print('\nEliminar cuarto nodo')
inst_dll.remove_node_by_position(4)
inst_dll.print_list()

print('\nEliminar segundo nodo')
inst_dll.remove_node_by_position(2)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar último nodo')
inst_dll.remove_node_by_position(5)
inst_dll.print_list()


print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()



print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()


print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()
#pasar el resto del codigo main 
print('\nAñadiendo nodos nuevamente')
inst_dll.add_node_at_start('C')
inst_dll.add_node_in_position(1, "NewNode1")
inst_dll.print_list()

inst_dll.remove_node_by_value("G")
inst_dll.print_list()

inst_dll.get_node_at_index(1)
#   inst_dll.get_node_at_index(4) este es el que saca error 



#calcular complejidad del codigo 
#en tiempo y complejida en espacio 
print('\añadiendo nuevos nodos')
inst_dll.add_node_at_start(' C')
inst_dll.add_node_at_start('A')
inst_dll.add_node_at_start('B')
inst_dll.add_node_at_start('F')
inst_dll.add_node_at_start('G')

inst_dll.add_node_in_position(1, "NewNode1")
inst_dll.print_list()

inst_dll.remove_node_by_value("NewNode1")
inst_dll.print_list()

inst_dll.get_node_by_value("G")
inst_dll.print_list()

inst_dll.get_node_at_index(1)
inst_dll.get_node_at_index(4)
inst_dll.get_node_at_index(2)
inst_dll.get_node_at_index(3)

print('Modificar valor del nodo 3 ')
inst_dll.update_node_at_index(3, "NewNode3")
inst_dll.print_list()

print('Modificar valor del nodo 2 ')
inst_dll.update_node_at_index(2, "NewNode2")
inst_dll.print_list()

inst_dll.update_node_by_value("NewValueNode2", "Node2")
inst_dll.print_list()




#----------------------------- CODIGO DE HOY--------------------------------    
print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nAñadiendo nodos nuevamente')
inst_dll.add_node_at_start("a")
inst_dll.add_node_at_start("2")
inst_dll.add_node_at_start("3")
inst_dll.add_node_at_start("0")
inst_dll.add_node_at_start("-6")
inst_dll.add_node_at_start("1")
inst_dll.add_node_at_start("A")
inst_dll.add_node_at_start("3")
inst_dll.add_node_at_start("0")
inst_dll.add_node_at_start("0")
inst_dll.print_list()
inst_dll.reverse()
inst_dll.print_list()
inst_dll.sort_asc()
inst_dll.print_list()
inst_dll.has_duplicates_with_information_v2()




