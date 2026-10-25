jarak=100
total_jarak = jarak * 2
liter = 1.5
harga_liter =10.000
total_liter= int (total_jarak/40)
perjalanan= total_liter - liter
biaya= int (perjalanan* harga_liter)


print("total perjalanan pulang-pergi :",total_jarak,"km")
print("total bahan bakar yang harus dibeli :",perjalanan,"liter")
print ("total keseluruhan bensin:",total_liter,"liter")
print("total biaya untuk membeli bensin:",biaya)