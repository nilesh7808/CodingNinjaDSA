# class Table:
#     def __init__(self, tableNo, seatingCapacity, bookingDate, status):
#         self.tableNo = 4
#         self.seatingCapacity = 5
#         self.bookingDate = 12122020
#         self.status = "booked" or "available"
#
#     def updateStatus(self, ddmmyyy):
#         self.status = "available"
#         if self.status != "available":
#             self.bookingDate = "booked"
#             self.bookingDate = None
#
# class Restaurant(Table):
#     def __init__(self, tableList):
#         self.tableListData = []
#         self.tableList = tableList
#         self.tableListData.append(tableList)
#         # super().__init__(self.seatingCapacity, self.bookingDate)
#
#     def bookTable(self,n,ddmmyyyy):
#         if self.seatingCapacity == n:
#             self.updateStatus(self, ddmmyyyy)
#
# r1 = Restaurant(104)
# n = 4
# ddmmyyyy = 12122020
# print(r1.bookTable(n,ddmmyyyy))

#
# def f1(a,b)list1 = ["a", "b",["c",["d","e"]]]
# def f1(a,b):
#     square = a ** 2
#     def fun2(a, b):
#         return a + b
#     add = fun2(a,b)
#     return add + 5
#
# res = f1(5, 10)
# print(res)
#
# l = [0,1,1,2,3,5,8,13, 21, 34, 55]
# print(list(filter(lambda x: x % 2-1, l)))
# print(",".join({"x":1,"y":2}))
# a = [1, 2, 3, 4]
# b = [sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)

a = [1,2,3,4,5,6,7,8,9]
print(a[::-5])
x = abs(int(float(-4.5 + 3.2)))
print(x-1j)