from  entrega_sll import entregasll
inst_sll=entregasll()

# Ingresamos como parametro el valor del nodo

""" Métodos para añadir nodo """
inst_sll.append_node_start("bmw")
inst_sll.append_node_start('wolskwagen')
inst_sll.append_node_start('chevrolet')
inst_sll.append_node_start('citroen')
inst_sll.append_node_start("renault")
inst_sll.append_node_end("toyota")

inst_sll.show_nodes_list()

""" Métodos de eliminar """
print('---------------------------------------------------')
print('     >> Eliminar último nodo <<')
inst_sll.pop_node()
inst_sll.show_nodes_list()



print('---------------------------------------------------')
print('\n     >> Eliminar primer nodo <<')
inst_sll.shift_node()
inst_sll.show_nodes_list()




print('---------------------------------------------------')
print('\n     >> Consultar valor de nodo <<')
inst_sll.get_node(1)
inst_sll.show_nodes_list()
print('----------------------------------------')




print('---------------------------------------------------')
print('\n     >> Actualizar valor de nodo <<')
inst_sll.update_node_value(1, "e36")
inst_sll.show_nodes_list()

