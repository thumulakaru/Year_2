from Quiz_071 import InternetProtocol


class RoutingTable:
    def __init__(self, mac:str):
        self.routing_table = {}
        self.mac_in = mac

    def validate(self):
        return len(self.mac_in) == 17 and self.mac_in.count(":") == 5

    def get_ip(self):
        ip_out = "Error"
        if self.validate():
            if self.mac_in in self.routing_table.keys():
                ip_out = self.routing_table[self.mac_in]
            else:
                while True:
                    temp_class = InternetProtocol(1)
                    ip = temp_class.ipv6machine()
                    if not ip in self.routing_table.values():
                        self.routing_table[self.mac_in] = ip
                        ip_out = ip
                        break
                        print(self.routing_table)
        return ip_out


a = RoutingTable("75:C0:01:03:G4:FB")
(a.get_ip())