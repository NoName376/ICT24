SAUCES = ("tomato sauce", "cheese sauce", "garlic sauce")
BREADS = ("toast",)
VEGETABLES = ("tomato", "cucumber", "onion")
MEATS = ("chicken", "beef", "bacon")

def main():
    result = []
    for bread in BREADS:
        for meat in MEATS:
            for vegetable in VEGETABLES:
                for sauce in SAUCES:
                    result.append([bread, meat, vegetable, sauce])
    for i in result:
        print(i)

if __name__ == "__main__":
    main()