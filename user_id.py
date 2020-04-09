
name_for_user_id = {
    321: "Alice",
    560: "Bob",
    875: "Dilbert"
}

def gretting(userid):
    return f"Hi {name_for_user_id.get(userid, 'there')}!"

print(gretting(321))

print(greetting(872132))