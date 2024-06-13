def greet_all(name1 , name2, *names):
    sorted_names = sorted(names)
    print(f"Здравствуй, {name1}!")
    print(f"Здравствуй, {name2}!")
    
    for name in sorted_names:
        print(f"Привет, {name}!")
    
greet_all(  "Alice","Bob","Sam" , "Jimmy"  )