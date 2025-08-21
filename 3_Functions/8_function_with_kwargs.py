#function with **kwargs

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(a="b",ram="prasad",hari="hari")
        
