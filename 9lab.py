import json
import os, csv
from PIL import Image


def z1():
    if not os.path.exists('processed_images'):
        os.makedirs('processed_images')

    for filename in os.listdir(r'D:/UserFolders/Desktop/lab/processed_images'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            with Image.open(os.path.join(r'D:/UserFolders/Desktop/lab/processed_images', filename)) as img:
                img = img.resize((500, 500))
                img.save(os.path.join('processed_images', filename))

def z2():
    if not os.path.exists('processed_images'):
        os.makedirs('processed_images')

    for filename in os.listdir(r'D:/UserFolders/Desktop/lab/processed_images'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            with Image.open(os.path.join(r'D:/UserFolders/Desktop/lab/processed_images', filename)) as img:
                img = img.resize((500, 500))
                img.save(os.path.join('processed_images', filename))

def z3():
    total_cost = 0

    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        print("Нужно купить:")
        for row in reader:
            product = row[0]
            quan = int(row[1])
            price = int(row[2])
            cost = quan * price
            total_cost += cost

            print(f"{product} - {quan} шт. за {price} руб.")

        print(f"Итоговая сумма: {total_cost} руб.")

z1()
z2()
z3()