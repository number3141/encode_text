class T():

    teacher = [1, 2, 3]

    # def __init__(self) -> None:
    #     self.teacher = 'gHBDTN' 


andrey = T()

marta = T()
marta.teacher.append(14)

print(id(andrey.teacher) == id(marta.teacher))
print(andrey.teacher)
print(marta.teacher)
# print(dir(andrey))