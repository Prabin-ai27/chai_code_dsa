users=[
    {"id":1,"total":120,"coupen":"P31"},
    {"id":2,"total":170,"coupen":"P27"},
    {"id":3,"total":90,"coupen":"F31"}
]

discounts={
    "P31":(0.2,0),
    "P27":(0.3,0),
    "F31":(0,21)
}

for user in users:
    presentage,fixe=discounts.get(user["coupen"],(0,0))
    discount=user["total"]*presentage+fixe
    # print(f"{user["id"]} user {user['total']} paid and get discount {discount}")
    print(f"User {user['id']} with total {user['total']} gets a discount of {discount}")