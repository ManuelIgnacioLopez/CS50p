# Nutrition Facts Fruits according to FDA
# Fruit - calories Dictionary

information = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": "strawberries",
    "sweet cherries": 50,
    "tangerine": 50,
    "watermelon": 80,
}
# prompt the user

prompt = input("Item: ").lower()

# give answer

if prompt in information:
	print(f"Calories: {information[prompt]}")