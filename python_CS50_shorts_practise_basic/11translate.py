dictionary = {"apple":"elma", "pear":"armut", "abstraction":"soyutlama", "qwerty":"asdfg"}
dictionary[input("please enter the key:")] = input("please enter the value:")
dictionary[input("please enter the key that you want to change its value")] = input("please enter the value that you want to change")
result = dictionary.get(input("please enter a key that you want to look for: "), "there is not any key named that")
print(result)
for k, v in dictionary.items():
    print(f"key:{k}||value:{v}")
