MOD = 1000000007
cache = [-1] * 101

def tiling(width : int):
    if width <= 1:
        return 1

    if cache[width] != -1:
        return cache[width]

    cache[width] = (tiling(width - 1) + tiling(width - 2)) % MOD
    
    return cache[width]

def asymmetric(width : int):
    if width % 2 == 1:
        return (tiling(width) - tiling(width // 2) + MOD) % MOD
    else:
        return ((tiling(width) - tiling(width // 2) + MOD) % MOD - tiling(width // 2 - 1) + MOD) % MOD

print(asymmetric(92))