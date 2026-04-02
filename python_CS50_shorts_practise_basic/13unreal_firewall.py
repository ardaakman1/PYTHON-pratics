firewall_rules = {"1": "Allowed", "2": "Blocked"}
firewall_rules[input("please enter new IP (key): ")] = input("please enter new rule (value): ")
rule_to_show = firewall_rules.get(input("please enter the IP that you want to see: "), "IP could not found")
print(rule_to_show)
IP_delete = input("please enter the IP that you want to delete: ")
deleted_rule = firewall_rules.pop(IP_delete, "IP could not found")
print(f"IP {IP_delete} has been deleted, its condition was {deleted_rule}")
for k, v in firewall_rules.items():
    print(f"IP:{k}----condition:{v}")