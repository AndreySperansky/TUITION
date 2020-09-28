a = [[1, 2, 3], [2, 4, 6], [7, 8, 9]] # для проверки

# def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             result = [[other * x for x in y] for y in self.list2D]
#             return matrix(result)
#         elif self.dim_C != other.dim_R:
#             return 'Нельзя перемножить матрицы таких размерностей'
#         else:
#             a = range(self.dim_C)
#             b = range(self.dim_R)
#             c = range(other.dim_C)
#             result = []
#             for i in b:
#                 res = []
#                 for j in c:
#                     el, m = 0, 0
#                     for k in a:
#                         m = self.list2D[i][k] * other.list2D[k][j]
#                         el += m
#                     res.append(el)
#                 result.append(res)
#             return matrix(result)
#     def __rmul__(self, other):
#         return self.__mul__(other)