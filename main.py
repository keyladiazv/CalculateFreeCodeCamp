# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main
from mean_var_std import calculate

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)

if __name__ == "__main__":
    # Prueba la función con una lista de 9 números
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)