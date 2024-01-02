from chv1r6180 import *
# W = coxeter("D", 4) # 定义 Coxeter 群
# conj = conjugacyclasses(W) # Coxeter 群中共轭类
# # print(conj)
# w = conj['reps'][10] # 找一个共轭类代表元

# print('Weyl群元素', w)
# print('表示为单根置换', W.wordtocoxelm(w))
# print('表示为根的置换', W.wordtoperm(w))
# print('表示为矩阵形式', W.wordtomat(w))
# an = klcellrepelm(W, w)['a']
# print('a(w)=', an)

W = coxeter("F", 4)
W.order
print(W.roots)
print(klcells(W,[2,1,1],v))
# print(W.wordtomat([0]))
# print(W.wordtomat([1]))
# print(W.wordtomat([2]))
# l = [1,2,3,4]
# w = [4,3,1,2]
# rep = klcellrepelm(W,w,pr=True)
# print(rep)


# def r():
#     pass

# for i in range(4):
#     p = [[w[i], i+1]]
#     for j in range(4):
#         if w[j] == i + 1:
#             p.append([j + 1, w[j]])


# def gpermtoword(w):
#     for wk in w:
