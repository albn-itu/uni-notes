import numpy as np


def determinant_newton_identities(A):
    n = A.shape[0]

    # Calculate traces (power sums)
    traces = [np.trace(np.linalg.matrix_power(A, ell):

    # Initialize arrays for elementary symmetric polynomials and determinant
    e=np.zeros(n+1, dtype=np.float64)
    e[0]=1.0

    # Dynamic programming to calculate elementary symmetric polynomials
    for ell in range(1, n+1):
        for k in range(1, ell+1):
            e[ell] += (-1)**(k-1) * traces[k-1] * e[ell-k] / ell

    return e[n]


# Example usage and testing
if __name__ == "__main__":
    # Create a sample 4x4 matrix
    A=np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    # Calculate determinant using our method
    det_newton=determinant_newton_identities(A)
    print(f"Determinant calculated using Newton's identities: {det_newton}")

    # Compare with NumPy's determinant function
    det_numpy=np.linalg.det(A)
    print(f"Determinant calculated by NumPy: {det_numpy}")

    # Check the difference
    print(f"Absolute difference: {abs(det_newton - det_numpy)}")

    # Test with a larger random matrix
    n=10
    B=np.random.rand(n, n)
    det_newton_large=determinant_newton_identities(B)
    det_numpy_large=np.linalg.det(B)
    print(f"\nFor a {n}x{n} random matrix:")
    print(f"Determinant (Newton's identities): {det_newton_large}")
    print(f"Determinant (NumPy): {det_numpy_large}")
