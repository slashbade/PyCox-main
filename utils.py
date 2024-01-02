from weight import WeylGroupElement
from chv1r6180 import coxeter
import numpy as np

def word_to_weylgroupelm(word, len_n):
    wg = WeylGroupElement(list(range(1,len_n+1)))
    for s in word:
        entry_next = list(range(1, len_n+1))
        if s == len_n - 1:
            entry_next[len_n-1] = -(len_n)
        else:
            entry_next[s], entry_next[s+1] = s+2, s+1
        wg_next = WeylGroupElement(entry_next)
        wg = wg * wg_next
        #print(wg_next)
    return wg

def cycle_to_gen(cycle, max_num):
    # represent (1,n) by (i, i+1) resursive
    def twocycle_to_gen(p):
        n = p[1]
        if n <= 2:
            return [0]
        return twocycle_to_gen((1, n-1)) + [n-2] + twocycle_to_gen((1, n-1))
    
    prod = []
    if len(cycle) == 2 and cycle[0] == -cycle[1]:
        num = abs(cycle[0])
        if num == max_num:
            prod.append((max_num, -max_num))
        elif num == 1:
            prod.extend([(1, max_num), (max_num, -max_num), (1, max_num)])
        else:
            prod.extend([(1, num), (1, max_num), (1, num),
                     (max_num, -max_num), 
                     (1, num), (1, max_num), (1, num)])
            # print(prod)
    else:
        num0 = cycle[0]
        if num0 == 1:
            for num1 in cycle[1:]:
                prod.append((1, num1))
        else:
            for num1 in cycle[1:]:
                if num1 == 1:
                    prod.append((1, num0))
                elif num1 == num0 + 1 or num1 == num0 - 1:
                    prod.append((num0, num1))
                else:
                    prod.extend([(1, num0), (1, num1), (1, num0)])
    
    # (1,n) to generators
    new_prod = []
    for cycle in prod:
        if cycle[0] == cycle[1] + 1 or cycle[0] == cycle[1] - 1:
            new_prod.append(min(cycle)-1)
        elif cycle[0] + cycle[1] == 0:
            new_prod.append(max_num-1)
        else:
            new_prod.extend(twocycle_to_gen(cycle))
    
    return new_prod


def weylgroupelm_to_word(entry: list, W):
    disjoint_cycles = []
    n = len(entry)
    entry0 = list(range(1, n+1))
    
    signed_term = []
    for index in range(n):
        num = entry[index]
        if num < 0:
            signed_term.append([-num, num])
            entry[index] = -num
        
    # same procedure as symmetry group
    while entry0:
        # get a cycle
        cycle = []
        index = 0
        index_list = [0]
        cycle.append(entry[index])
        while entry[entry0.index(entry[index])] != entry[0]:
            index = entry0.index(entry[index])
            index_list.append(index) # keep a list of index
            cycle.append(entry[index])
        # add the cycle to prod
        if len(cycle) > 1:
            disjoint_cycles.append(cycle)
        # delete the cycle from entry
        index_list.sort(reverse=True)
        for index in index_list:
            entry.pop(index)
            entry0.pop(index)
    
    disjoint_cycles.extend(signed_term)
    
    # disjoint cycles to gen
    prod = []
    print(disjoint_cycles)
    for cycle in disjoint_cycles:
        prod.extend(cycle_to_gen(cycle, n))
    # print(prod)
    return W.reducedword(prod, W)

if __name__ == "__main__":
    word = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0]
    W = coxeter("D", 4)
    cartan = np.array(W.cartan).transpose()
    W = coxeter(cartan.tolist())
    word_re = W.reducedword(word, W)
    print(word_re)
    print(word_to_weylgroupelm(word, 4))
    print(word_to_weylgroupelm(word_re, 4))
    print(word_to_weylgroupelm(weylgroupelm_to_word([1,-3,-2,-4], W), 4))
    print(weylgroupelm_to_word(word_to_weylgroupelm([0,1,0,2,1,3,0], 4).entry, W))