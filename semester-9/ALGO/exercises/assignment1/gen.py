import numpy as np


def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p


def get_lambda_ell(partitions, n):
    lambda_ell = []
    for partition in partitions:
        count = [0] * (n+1)
        for part in partition:
            count[part] += 1
        lambda_ell.append(count)

    return lambda_ell


def get_traces(A, n):
    traces = [-1]
    for ell in range(1, n+1):
        traces.append(np.trace(np.linalg.matrix_power(A, ell)))

    return traces


def get_division(lambda_ells, n, traces):
    divisions = []
    latex = "\\frac{{ {trace}^{lambda_ell} }}{{ {lambda_ell}!\\cdot(-{ell})^{lambda_ell} }}"
    for ell in range(1, n+1):
        divisions.append(latex.format(
            trace=traces[ell],
            lambda_ell=lambda_ells[ell],
            ell=ell
        ))

    return " \\cdot ".join(divisions)


if __name__ == "__main__":
    n = 4
    matrix = np.random.rand(n, n)

    n = matrix.shape[0]
    partitions_ = list(partitions(n))
    lambda_ells = get_lambda_ell(partitions_, n)
    traces = get_traces(matrix, n)

    all_products = []
    for lambda_ell in lambda_ells:
        all_products.append(get_division(lambda_ell, n, traces))

    print("(-1)^{n} \\cdot {all_products}".format(
        n=n,
        all_products=" + ".join(all_products)
    ))

    print(np.linalg.det(matrix))
