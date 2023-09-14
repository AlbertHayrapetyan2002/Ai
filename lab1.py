import numpy as np
import random

class FruitOrVegetable:
    def __init__(self, rows, columns, y, k, epsilon,*args):
        self.epsilon=epsilon
        self.columns = columns
        self.rows = rows
        self.parents_row = int(self.rows - (self.rows * 0.2))
        self.Y = y
        self.k = k
        self.X = np.column_stack(args)

    def __repr__(self):
        return f"{self.X}"

    def distance_between_points(self):
        distance_array = []
        for i in range(self.parents_row, self.rows):
            distance_list = []
            for j in range(self.parents_row):
                diff = 0
                for k in range(self.columns):
                    diff += (self.X[i, k] - self.X[j, k])**2
                distance_list.append((np.sqrt(diff), j))
            distance_array.append(distance_list)
        return distance_array

    def array_sorting(self):
        distance = self.distance_between_points()
        for i in range(len(distance)):
            distance[i].sort()
        return distance

    def getting_intermediate_y(self):
        sorted_distance = self.array_sorting()
        real_y_array = []
        for i in sorted_distance:
            temporal_array = []
            for j in range(self.k):
                temporal_array.append(i[j][1])
            real_y_array.append(temporal_array)
        return real_y_array

    def getting_appropriate_y(self):
        real_y = self.getting_intermediate_y()
        appropriate_y = []
        for i in real_y:
            temporal_array = []
            for j in i:
                temporal_array.append(self.Y[j])
            appropriate_y.append(temporal_array)
        return appropriate_y

    def getting_real_y(self):
        appropriate_y = self.getting_appropriate_y()
        real_y = []
        for i in range(len(appropriate_y)):
            real_y.append(max(appropriate_y[i], key=appropriate_y[i].count))
        return real_y

    def getting_epsilon(self):
        real_y = self.getting_real_y()
        Y = self.Y[self.parents_row:]
        diff = 0
        for i in range(len(real_y)):
            diff += (Y[i] - real_y[i])**2
        return np.sqrt((1/(self.rows * 0.2)) * diff)
    
    def comparison_results(self):
        epsilon=self.getting_epsilon()
        if epsilon<=epsilon_given:
            print("Is classified")
        else:
            print("Not Classif")

rows = int(input("rows="))
columns = int(input("columns="))
k = int(input("k="))
epsilon_given=0.9

colors_quantity = int(input("colors_quantity="))
testes_quantity = int(input("testes_quantity="))
views_quantity = int(input("views_quantity="))
results_quantity = int(input("results_quantity="))
COLOR = [input("color=") for _ in range(colors_quantity)]
TESTE = [input("test=") for _ in range(testes_quantity)]
VIEW = [input("view=") for _ in range(views_quantity)]
RESULT = [input("result=") for _ in range(results_quantity)]

y = np.array([random.randint(1, len(RESULT)) for _ in range(rows)])
x1 = np.array([random.randint(1, len(COLOR)) for _ in range(rows)])
x2 = np.array([random.randint(1, len(TESTE)) for _ in range(rows)])
x3 = np.array([random.randint(1, len(VIEW)) for _ in range(rows)])

X = FruitOrVegetable(rows, columns, y, k, epsilon_given, x1, x2, x3)

print("distance_between_array=",X.distance_between_points())

print("sorting_array=",X.array_sorting())

print("intermediate_array=",X.getting_intermediate_y())

print("appropriate_array=",X.getting_appropriate_y())

print("real_y_array=",X.getting_real_y())

print("epsilon=",X.getting_epsilon())

