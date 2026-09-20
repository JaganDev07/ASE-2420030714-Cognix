from cce.models import Node, Relationship, Memory


alice = Node(name="Alice")

orion = Node(name="Project Orion")

sensor = Node(
    name="Sensor Service",
    memory=["Critical service"]
)

r1 = Relationship(
    source=alice,
    relation="manages",
    target=orion
)

r2 = Relationship(
    source=orion,
    relation="depends_on",
    target=sensor
)

memory = Memory(
    nodes=[alice, orion, sensor],
    relationships=[r1, r2]
)

print(memory.model_dump_json(indent=2))
