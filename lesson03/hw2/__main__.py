# Используя циклы и метод:
# print("* "), print(" ", end =""), print("\n") (для перехода на новую строку).
# Выведите на экран:
# · прямоугольник
# · прямоугольный треугольник
# · равносторонний треугольник
# · ромб
def rectangle(n, m):
    for i in range (0,n, 1):
        for j in range (0, m , 1):
            if i == 0 or i == n-1 or j==0 or j==m-1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()
def triangle_p(n, m):
    for i in range (0,n, 1):
        for j in range (0, m , 1):
            if i == n-1 or j==0 or i==j:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()

if __name__ == '__main__':
    n = 20
    m = 20
    for i in range (0,n, 1):
        for j in range (0, m , 1):
            if i == n/2 or j==n/2+i or j==n/2-i :
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()
