'''
List Methods
Date:27/01/23

'''

class ListMethods:
        def __init__(self):
            self.pets = []
            self.vehicles = list()
            
        def add_list_elements(self):
            self.pets.append('dog')
            self.pets.append('cat')
            print(self.pets)

        def input_data_vehicles_list(self):
            vehicles_number =int(input('cuantos'))
            for vehicle_item in range ('vehicles_n'):
                vehicle_type =input('tipo de vehiculo')
                self.vehicles.append(vehicle_type)
                #imprimir toda la lista 
            print(self.vehicles)
            #imprimir ultimo ,penultimo y antepenultimo elemento de la lista
            print(self.vehicles[-1],self.vehicles[-2], self.vehicles[-3])

            #4 extraer subconjunto de la lista 
        def show_collection_data_list(self):
                #desde posicion 2 hasta 3 
            print(self.vehicles[2:4])
                #todos los elementos de la lista 
            print(self.vehicles[:])
                #elementos desde un indice especifico : 2[2,3...]
            print(self.vehicles[2:])
                #elementos hasta un indice especifio : 2[0,1,2]
            print(self.vehicles[:2])
                #acceder a  TODOS los elementos de 2 en 2 
            print(self.vehicles[::3])
                #acceder a  UN SUBCONJUNTO los elementos de 2 en 2
            print(self.vehicles[1:5:2])


    #5 iterar los elementos de la lista con ciclo FOR 
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
        #validar si la lista contiente un valor especifico
        if "carro" in self.vehicles:
        print("si se encontro valor")
        else:
              print("no se encontro el valor")

    # 6 añadir varios elementos a la lista
    def add_elements(self):
        self.vehicles.extend(['avion', 'tractomula','otro medio'])
        self.vehicles.insert()

    #7añadir un elemento en posicion especifica de la lista 
def add_specific_elements(self):
        self.vehicles.insert(0, 'moto')
        print (self.vehicles)



        








