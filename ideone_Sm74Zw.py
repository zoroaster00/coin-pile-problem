import math
import sys

# solve [3, 5, 7] or more coin problem
# map with pile condition and result (N/A, U LOSE, U WIN)
result_map = {(0,0,0): "N/A", (0,0,1): "U LOSE"}

def operate(coin_piles):
    # can only a) select one pile b) take one to all coins
    global result_map
    o_key = get_key_from_piles(coin_piles)
    for i in range(0, len(coin_piles)):
        for c in range(1, coin_piles[i]+1):
            to_op_piles = list(coin_piles)
            to_op_piles[i] -= c
            key = get_key_from_piles(to_op_piles)
            result = result_map.get(key)
            if result is None:
                result = operate(to_op_piles)
            if result == "U LOSE":
                print "WIN: old %s new %s pile %s pile %s " % (o_key, key, coin_piles, to_op_piles)
                
                result_map[o_key] = "U WIN"
                return "U WIN"
            
    print "LOSE: old %s new %s pile %s pile %s " % (o_key, key, coin_piles, to_op_piles)
    result_map[o_key] = "U LOSE"
    return "U LOSE"


def get_key_from_piles(p):
    return tuple(sorted(p))

print operate([3,5,7])
