from app import app, db
from models import Algorithm

def add_algo(data):
    with app.app_context():
        algo = Algorithm(**data)
        db.session.add(algo)
        db.session.commit()
        print(f"✅ Додано: {algo.name}")
add_algo({
    "name": "Сортування вибором",
    "category": "Сортування",
    "description": "ростий алгоритм сортування лінійного масиву, на основі вставок.",
    "pseudocode": """
selectionSort(arr):
    n = length(arr)
    for i = 0 to n - 2:
        minIndex = i
        for j = i + 1 to n - 1:
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            swap(arr[i], arr[minIndex])
""",
    "implementation": """
def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList


el = [21,6,9,33,3]

print(selectionSort(el))
""",
    "complexity": "O(log n)",
    "usage": "Застосовується для швидкого пошуку у відсортованих масивах, базах даних, словниках."
})