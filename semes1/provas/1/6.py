def quadrado(nums):
    quadrados = []
    for num in range(len(nums)):
        numQuadrado = nums[num] ** 2
        quadrados.append(numQuadrado)
    return quadrados