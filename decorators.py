def permission(f):
    def decorator():
        return [user for user in f() if user['permission'] == 1]

    return decorator


@permission
def show():
    return [
        {"name": "Marcos", "permission": 1},
        {"name": "Roney", "permission": 0}
    ]


print(show())