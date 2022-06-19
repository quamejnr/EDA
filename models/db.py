from models.model import Product, User


INVENTORY = {
    "Playstation 5": Product("Playstation 5", 6_000.00, 5),
    "Audioengine A2+": Product("Audioengine A2+", 2_500.00, 3),
    "AOC Monitor CQ27G2": Product("AOC Monitor CQ27G2", 2_500.00, 6),
}

USERS = {
    "johndoe": User("John Doe", "jd@email.com")
}
