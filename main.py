ItemList = [
    'Saldainiai',
    'Traškučiai',
    'Gėrimas',
    'Kramtomoji guma'
]
PriceList = [
    float(0.50),
    float(1.00),
    float(1.50),
    float(0.75)
]
MinPrice = float(min(PriceList))
Balance = float(input("Įveskite sumą, kurią norite išleisti:"))
if Balance < MinPrice:
    print("Jūsų įvestos sumos nepakanka jokiems daiktams įsigyti")
else:
    while Balance >= MinPrice:
        BuyableItems = []
        for i in range(len(ItemList)):
            if Balance >= PriceList[i]:
                BuyableItems.append(i)
        print("Galite įsigyti:")
        for i in range(len(BuyableItems)):
            print(i + 1, ItemList[i], "-", PriceList[i])
        Choice = int(input("Įveskite pasirinkimo numerį:")) - 1
        if Choice >= len(BuyableItems):
            print("Nėra tokio pasirinkimo")
        else:
            print("Pasirinkote", ItemList[Choice])
        Balance -= PriceList[Choice]
        print("Likutis:", Balance)
    print("Dėkojame už Jūsų pirkinį. Jūsų likutis yra", Balance)



