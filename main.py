k={}
print(type(k))

k={"123":"koushik","234":"Anchuri","345":"praTAP"}
print(type(k))
print(k["123"])
print(k)
for i in k :
    print(i)
for i in k.values() :
    print(i)

for i in k.keys() :
    print(i)
    for i in k.items():
        print(i)
k["456"]="Likitha"
print(k)


car_type1={'mercedes':1032}
car_type2={'awdi':2121}
car_type3={'bmw':98998}

car_type={'car1':car_type1,'car2':car_type2,'car3':car_type3}
print(type(car_type))
print(car_type)
print(car_type["car1"])
print(car_type["car2"])
print(car_type["car3"])
movie_list1=["rajamouli",12]
movie_list2=['atlee',5]
movie_list3=['trivikram',20]
movies={'movie':movie_list1,'movie2':movie_list2,'movie3':movie_list3}
print(movies)

print(movies['movie'])
print(movies['movie2'])
print(movies['movie3'])








