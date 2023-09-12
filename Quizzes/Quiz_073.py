from Quiz_071 import InternetProtocol


class RoutingTable:
    def __init__(self):
        self.routing_table = {}

    def validate(self, mac_in: str):
        return len(mac_in) == 17 and mac_in.count(":") == 5

    def get_ip(self, mac_in):
        if self.validate(mac_in):
            ip = ""
            if mac_in in self.routing_table.keys():
                ip = self.routing_table[mac_in]
                unique = False
                while unique is False:  # Validating IP
                    temp_class = InternetProtocol(1)
                    temp_ip = temp_class.ipv6machine()
                    if temp_ip != ip:
                        unique = True
                self.routing_table[mac_in].append(temp_ip[0])  # Adding new IP to the existing list

            else:
                while True:
                    temp_class = InternetProtocol(1)
                    ip = temp_class.ipv6machine()
                    if not ip in self.routing_table.values():
                        self.routing_table[mac_in] = []  # Creating an Empty list for the new MAC in the dictionary
                        self.routing_table[mac_in].append(ip[0]) #  Adding the new IP to the list
                        break
        return self.routing_table


a = RoutingTable()
a.get_ip("00:1A:2B:3C:4D:5E")
a.get_ip("12:34:56:78:90:AB")
a.get_ip("00:1A:2B:3C:4D:5E")
print(a.get_ip("FF:EE:DD:CC:BB:AA"))
