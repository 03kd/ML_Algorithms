trip = [['Chennai', 'Bangalore'], ['Bombay','Delhi'],
        ['Goa', 'Chennai'], ['Delhi','Goa'], ['Bangalore', 'Beijing']]
my_trip =[]
for sub in trip:
    for item in sub:
        if item not in my_trip:
            my_trip.append(item)
        else:
            my_trip.remove(item)
            
start = my_trip[0]
end = my_trip[1]
flag = ''
while(flag != end):
    for item in trip:
        if start in item:
            print(item)
            start = item[1]
            flag = item[1]
        
