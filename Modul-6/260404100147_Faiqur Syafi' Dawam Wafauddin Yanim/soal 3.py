def evaluasi_pc(pc_item):
    status = pc_item[1]
    ram = int(pc_item[2]) 
    
    if status == 'Normal' and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

def sistem_inventaris_pc():
    print("\nSistem Pendataan Inventaris PC")
    try:
        jumlah_input = int(input("Masukkan jumlah PC yang ingin didata: "))
    except ValueError:
        jumlah_input = 0
        
    inventaris = []
    for i in range(jumlah_input):
        print(f"\nData PC ke-{i+1}:")
        nama_pc = input("Masukkan Nama PC: ")
        status_pc = input("Masukkan Status (Normal/Rusak): ")
        ram_pc = input("Masukkan Kapasitas RAM (GB): ")
        inventaris.append([nama_pc, status_pc, ram_pc])
        
    print("\nHasil Evaluasi Inventaris PC")
    for pc in inventaris:
        try:
            kelayakan = evaluasi_pc(pc)
        except ValueError:
            kelayakan = "Format RAM Kacau" 
            
        hasil_format = f'{{ "PC": "{pc[0]}", "Status": "{kelayakan}" }}'
        print(hasil_format)

sistem_inventaris_pc()