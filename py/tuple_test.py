a_tuple=(12,3,2,4,122)
another_tuple=12,3,2,4,122

a_list=[12,3,2,4,122]

a_list.append(0)

a_list.insert(0,0)
print(a_list)

print(a_list[0])
print(a_list.index(0))
print(a_list.count(0))
a_list.sort(reverse=True)
print(a_list)
a_list.reverse()
print(a_list)