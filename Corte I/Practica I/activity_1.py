'''
data type:list practice 
date: 25/01/23
'''

# 1 Declarar clase 

class ListPractice:
    
#2. crear funcion inicializadora de la clase
    def __init__(self):
    #Definir las variables globales de la clase
        self.student_name=""
        self.courses_list = ['POO' , 'TAD']

    #3.Funcion customizada
    def show_info_list(self):
        #Imprimir el contenido de la lista courses_list
        print(self.courses_list)
        #cantidad de elementos que tiene la lista
        print(len(self.courses_list))

    #4 funcion que solicita al usuario ingresar informacion

    def input_data_courses(self):
        #1 declaramos una varianble a nivel del metodo
        print('Ingrese la siguiente informacion:')
        #solicitud de textos
        self.student_name= input('nombre: ')
        #Solicitud de numero entero 
        courses_number= int(input('Cantidad asignaturas: '))
        #validamos si el courses number es menor que el tamaño actual de la lista
        if courses_number< len(self.courses_list):
            print('>>Error:Cursos a inscribir es menor que 2 <<')
        else:






            #solicitar nombre de las asignaturas al usuario
            for course in range(courses_number):
                #Variable que almacena el nombre de la asignatura
                courses_name=input('Nombre asignatura:')
                if courses_name== self.courses_list[course]:
                    print('la asignatura ya se encuentra inscrita')
                else:
                #añadimos nuevo elemento al final de la lista
                    self.courses_list.append(courses_name)
            #imprimir contenido de la lista 
            print(self.courses_list)












