from eo_lib.domain.entities import Initiative, Team, Role
import inspect

print("Initiative MRO:", Initiative.__mro__)
print("Is Initiative a subclass of Team?", issubclass(Initiative, Team))
print("Initiative attributes:", dir(Initiative))

print("Role defined:", Role)
