def count_carnivore_dinosar_egg(egg_list) -> int:
    total_carnivoro_eggs = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivoro_eggs += eggs

    return total_carnivoro_eggs


egg_list = [3, 4, 7, 8, 6]
print(count_carnivore_dinosar_egg(egg_list))
