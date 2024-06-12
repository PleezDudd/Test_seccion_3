import csv
lista=[]
def menu():
    print("="*23)
    print("======= M E N Ú =======")
    print("1.- Agregar Producto")
    print("2.- Listar todos los Productos")
    print("3.- Eliminar un Producto por ID")
    print("4.- Generar Archivo CSV")
    print("5.- Cargar Datos desde CSV")
    print("6.- Estadísticas")
    print("0.- Salir")
def producto():
    ID=input("Ingrese ID del producto: ")
    nombre=input("Ingrese nombre del producto: ")
    precio=int(input("Ingrese precio del producto: "))
    productos=[ID,nombre,precio]
    lista.append(productos)
    print("PRODUCTO AGREGADO CORRECTAMENTE!")
def listar():
    for x in lista:
        print("ID:",x[0]," Nombre:",x[1]," Precio:",x[2])
def eliminar():
    encontrado=False
    IDD=input("Ingrese ID del producto a eliminar: ")
    for x in lista:
        if IDD==x[0]:
            lista.remove(x)
            print("Producto eliminador correctamente")
            encontrado=True
            break
    if encontrado==False:
        print("Producto no encontrado...")
def generar():
    with open("ArchivoCSV.csv","w",newline="")as Archivo:
        escribircsv=csv.writer(Archivo)
        escribircsv.writerow(["ID","Nombre","Precio"])
        escribircsv.writerows(lista)
        print("ARCHIVO GUARDADO CORRECTAMENTE")
def cargar():
    lista.clear()
    with open("ArchivoCSV.csv","r",newline="")as Archivo:
        leercsv=csv.reader(Archivo)
        for x in leercsv:
            lista.append(x)
    lista.pop(0)
    for x in lista:
        print("ID:",x[0]," Nombre:",x[1]," Precio:",x[2])    
def estadisticas():
    acum=0
    for x in lista:
        cant=len(lista)
        plata=int(x[2])
        acum=acum+plata
        prom=acum/cant
    print("Hay un total de ",cant," productos en la lista")
    print("Precio total de los productos: $",acum)
    print("Precio promedio de los productos: $",prom)
while True:
    menu()
    try:
        op=int(input("Ingrese una opción:\n"))
        if op==1:
            print("=== AGREGAR PRODUCTO ===")
            producto()
        elif op==2:
            print("=== LISTA DE LOS PRODUCTOS ===")
            listar()
        elif op==3:
            print("=== ELIMINAR UN PRODUCTO POR ID ===")
            eliminar()
        elif op==4:
            print("=== GENERAR ARCHIVO CSV ===")
            generar()
        elif op==5:
            print("=== CARGAR DATOS DESDE CSV ===")
            cargar()
        elif op==6:
            print("=== ESTADÍSTICAS ===")
            estadisticas()
        elif op==0:
            print("Gracias por usar esta plataforma!")
            break
        else:
            print("Seleccione una opción válida")
    except:
        print("SELECCIONE UNA OPCIÓN VÁLIDA")
    
