name=None

def get_val():
    if name is None:
        return None
    return name
dt={}
dt.setdefault('age',get_val())
print(dt)