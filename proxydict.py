"""
Proxy Dictionary:

    dictionary - d can be see through d_proxy

    changes cannot be made through d_proxy

    d_proxy is dynamic; if any changes in d will reflected automatically.

"""


from types import MappingProxyType


d = {"name": "felix"}
d_proxy = MappingProxyType(d)
print(d_proxy)

print(d_proxy['name'])
d['last'] = "stephen"
print(d_proxy)

d_proxy['age'] = 22


