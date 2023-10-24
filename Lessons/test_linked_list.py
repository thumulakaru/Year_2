from adts import Node

my_list = Node("alice")
bob_node = Node("bob")
my_list.addNode(bob_node)


amy_node = Node("amy")
carl_node = Node("carl")
cam_node = Node("cam")

my_list.next.addNode(carl_node)
my_list.addNode(amy_node)
my_list.next.next.addNode(cam_node)