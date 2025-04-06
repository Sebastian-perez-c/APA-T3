"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Sebastian Pérez Capitano

    Tests unitarios:
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 * v2
        Vector([4, 10, 18])
        >>> v1 @ v2
        32
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
"""

import math

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        self.vector = [valor for valor in iterable]

    def __repr__(self):
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        return str(self.vector)

    def __getitem__(self, key):
        return self.vector[key]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __len__(self):
        return len(self.vector)

    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        return -(-self + other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o realiza el producto de Hadamard con otro vector.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(valor * other for valor in self)
        else:
            return Vector(a * b for a, b in zip(self, other))

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        """
        Producto escalar entre dos vectores.
        """
        return sum(a * b for a, b in zip(self, other))

    def __rmatmul__(self, other):
        return self @ other

    def __floordiv__(self, other):
        """
        Devuelve la componente paralela (tangencial) del vector respecto a otro vector.
        """
        escalar = (self @ other) / (other @ other)
        return escalar * other

    def __mod__(self, other):
        """
        Devuelve la componente perpendicular (normal) del vector respecto a otro vector.
        """
        return self - (self // other)

# Para ejecutar los doctests al ejecutar el archivo como script
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
