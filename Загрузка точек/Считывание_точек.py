class Points:

    find = 0

    def create_point_from_input():
        data = input("Введите № x y:").split(",")
        while 'end' not in data:
            data+=input().split(",")
        return data

    def find_point(data:list):
        Points.find=int(input("Введите номер точки:"))
        Points.find=[data[Points.find*2-2], data[Points.find*2-1]]
        return Points.find

    def list_of_points(data:list):
        list=[]
        i=0
        diapason=input("Введите диапазон точек:").split(' ')

        for i in range(int(diapason[0]),int(diapason[1])+1):
            list+=[str(i),str(data[i*2-2]),str(data[i*2-1])]

        return str(list)



