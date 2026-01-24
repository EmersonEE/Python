"""
Escribe una funcion en python que reciba una lista de numeros entreos y devuelva la suma total de los
huevos que pertenecen a los dinusaurios carinivros es decir la suma de todoso los numeros pares de las liesta


"""


def count_carnivore_dinosaur_eggs(egg_list) -> int:
    """
    Esta funcion recibe una lista de numeros entreorso que respresenta la cantidad de huevos que han puesto
    diferentes dinosaurios en el parque jurasico y los de numeros par son carnivoreso.
    """
    total_carnivore_eggs = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs


egg_list = [3, 4, 7, 5, 7, 8]
print(count_carnivore_dinosaur_eggs(egg_list))
