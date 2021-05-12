import csv
import numpy as np

graph0 = []
graph1 = []
graph2 = []
graph3 = []

graph0_n = []
graph1_n = []
graph2_n = []
dispers = {}

with open('sin.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		graph0.append(int(row[0]))

print("Прямое преобразование: ")
graph1.append(graph0[0])
for i in range(len(graph0)-1):
	graph1.append(graph0[i+1]-graph0[i])
	
graph2.append(graph1[0])
for i in range(len(graph1)-1):
	graph2.append(graph1[i+1]-graph1[i])

graph3.append(graph2[0])
for i in range(len(graph2)-1):
	graph3.append(graph2[i+1]-graph2[i])

print("\ngraph0: ")
print(graph0)
print("\ngraph1: ")
print(graph1)
print("\ngraph2: ")
print(graph2)
print("\ngraph3: ")
print(graph3)

print("Обратное преобразование: ")

graph2_n.append(graph3[0])
for i in range(len(graph3)-1):
	graph2_n.append(graph2_n[i]+graph3[i+1])

graph1_n.append(graph2_n[0])
for i in range(len(graph2_n)-1):
	graph1_n.append(graph1_n[i]+graph2_n[i+1])

graph0_n.append(graph1_n[0])
for i in range(len(graph1_n)-1):
	graph0_n.append(graph0_n[i]+graph1_n[i+1])

print("\ngraph2_n: ")
print(graph2_n)
print("\ngraph1_n: ")
print(graph1_n)
print("\ngraph0_n: ")
print(graph0_n)

print("\n")
print("Дисперсия для graph0_n: "+str(np.var(graph0_n)))
print("Дисперсия для graph1_n: "+str(np.var(graph1_n)))
print("Дисперсия для graph2_n: "+str(np.var(graph2_n)))

dispers = {'graph0_n': np.var(graph0_n), 'graph1_n': np.var(graph1_n),'graph2_n': np.var(graph2_n)}
max_value = max(dispers.values())
final_dict = {k: v for k, v in dispers.items() if v == max_value}
final_dict = list(map(list, final_dict.items()))

print("\n")
print("Максимальная дисперсия: ")
print(str(final_dict[0][0])+" = "+str(final_dict[0][1]))
