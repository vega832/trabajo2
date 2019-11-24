#ejercicio 1
#calcular la renumeracion renta anual del trabajador
#Donde la renumeracion bruta anual  se calcula de la siguiente manera
#renumeracion mensual x numero de meses que falta para terminar el año
#mostrar la renumeracion bruta anual

#Dectector impuesto mensual
trabajador,renumeracion_mensual,numero_de_meses,monto="",0.0,0,0.0

#INPUT
trabajador=input("ingrese nombre del trabajador")
renumeracion_mensual=float(input("ingrese renumeracion mensual"))
numero_de_meses=int(input("ingrese numero de meses"))
#PROCESSING
monto=renumeracion_mensual*numero_de_meses

#Dectector
# sera impuesto mensual cuando el monto  >300
impuesto_mensual=(monto>300)
#Output
print("####################")
print("#   Renumeracion Bruta Anual   #")
print("####################")
print(" # trabajador:", trabajador,"  #")
print("# renumeracion mensaul:", renumeracion_mensual,"   #")
print("# numero de meses:", numero_de_meses, "     #")
print("# monto:",monto,"    #")
print("#impuesto mensual:", impuesto_mensual,"    #")
print("####################")


# ejercicio 2
#calcular total de utiles escolares
#donde el total de utiles escolares se calcula de la siguiente manera
#cantidad x costo unidad
# mostrar la boleta de pago

#Dectector de comprador impulsivo
cliente,producto,cantidad,costo_de_unidad,total="","",0,0.0,0.0

#INPUT
cliente=input("ingrese nombre del cliente")
producto=input(input("ingrese nomnre del  producto "))
cantidad=int(input("ingrese cantidad "))
costo_de_unidad=float(input("ingrese el costo de unidad"))
#PROCESSING
total=cantidad*costo_de_unidad

#Dectector
# sera comprador impulsivo >250
comprador_impulsivo =(total>250)
#Output
print("####################")
print("#   boleta de pago   #")
print("####################")
print(" # cliente:", cliente,"  #")
print("# producto:", producto,"   #")
print("# cantidad:", cantidad, "     #")
print("# costo de unidad:",costo_de_unidad,"    #")
print("# total:",total,"    #")
print("# comprador impulsivo:",comprador_impulsivo,"   #")
print("####################")

# ejercicio 3
#calcular el trabajo por dia
#donde el trabajo por dia se calcula
#unidades producidas x costo por trabajo por unidad
# mostrar el trabajo por dia

#Dectector calidad de trabajo
empleado,unidad_producida,costo_por_trabajo,monto="",0,0.0,0.0

#INPUT
empleado=input("ingrese nombre del empleado")
unidad_producida=int(input("ingrese unidad producida"))
costo_por_trabajo=float(input("ingrese el costo por trabajo"))

#PROCESSING
monto=unidad_producida*costo_por_trabajo

#Dectector
# sera calidad de trabajo >400
calidad_de_trabajo =(monto>400)
#Output
print("####################")
print("#   trabajo por dia #")
print("####################")
print(" # cliente:", cliente,"  #")
print("# unidad producida:",unidad_producida,"   #")
print("# costo por trabajo:",costo_por_trabajo, "     #")
print("# monto:",monto,"    #")
print("# calidad de trabajo :",calidad_de_trabajo,"   #")
print("####################")

# ejercicio 4
#calcular el impuesto anual del trabajador
#donde el impuesto anual se calcula de la siguiente manera
#renumeracion neta anual x tasa
# mostrar el impuesto mensual

#Dectector impuesto mensual
trabajador,renumeracion_neta_anual,tasa,total="",0.0,0.0,0.0

#INPUT
trabajador=input("ingrese nombre del trabajador")
renumeracion_neta_anual=float(input("ingrese renumeracion neta anual"))
tasa=float(input("ingrese tasa "))

#PROCESSING
total=renumeracion_neta_anual*tasa

#Dectector
# sera impuesto mensual >100
impuesto_mensual =(total>100)
#Output
print("####################")
print("#   impuesto anual  #")
print("####################")
print(" # trabajador:", trabajador,"  #")
print("# renumeracion neta anual:", renumeracion_neta_anual,"   #")
print("# tasa:",tasa, "     #")
print("# total:",total,"    #")
print("# impuesto mensual :",impuesto_mensual,"   #")
print("####################")

#Ejercicio 5
#calcular el porcentaje de alumnos rubios
#donde el porcentaje de alumnos rubios se calcula de la siguiente manera
#cantidad de rubios x 100
#se le divide total de alumnos
# mostrar el porcentaje de alumnos rubios

#Dectector alumnos rubios
cantidad_de_rubios,total_de_alumnos,porcentaje=0,0,0.0

#INPUT
cantidad_de_rubios=int(input("ingrese la cantidad de rubios"))
total_de_alumnos=int(input("ingrese el total de alumnos"))

#PROCESSING
porcentaje=(cantidad_de_rubios*100)/total_de_alumnos
#Dectector
# seran rubios si es >0.15
alumnos_rubios =(porcentaje>0.15)
#Output
print("####################")
print("#   porcentaje de alumnos rubios #")
print("####################")
print(" # cantidad de rubios:",cantidad_de_rubios,"  #")
print("# total de alumnos:",total_de_alumnos,"   #")
print("# porcentaje:",porcentaje,"    #")
print("# alumnos rubios :",alumnos_rubios,"   #")
print("####################")

#Ejercicio 6

#calcular el total de un descuento de un producto
#donde el descuento de un producto se calcula de la siguiente manera
#costo_de_producto x descuento
# mostrar el descuento

#Dectector descuento
producto,costo_de_producto,descuento,total="",0.0,0.0,0.0

#INPUT
producto=input("ingrese el nombre del producto")
costo_de_producto=float(input("ingrese costo de producto"))
descuento=float(input("ingrese descuento"))
#PROCESSING
total=costo_de_producto*descuento
#Dectector
# seran descuento si es >1000
descuento =(total>1000)
#Output
print("####################")
print("#   total de un descuento de un producto #")
print("####################")
print(" # producto:",producto,"  #")
print("# costo de producto:",costo_de_producto,"   #")
print("# descuento:",descuento,"    #")
print("# total :",total,"   #")
print("# decuento:",descuento,"    #")
print("####################")

#Ejercicio 7
#calcular el pago total de iva
#donde el pago total de iva se calcula
#precio x iva
# mostrar el pago de iva

#Dectector iva
precio,iva,pago_total_de_iva=0.0,0.0,0.0

#INPUT
precio=float(input("ingrese el precio"))
iva=float(input("ingrese iva"))

#PROCESSING
pago_total_de_iva=precio*iva
#Dectector
# seran iva>100
iva=(pago_total_de_iva>100)
#Output
print("####################")
print("#   psgo total de iva #")
print("####################")
print(" # precio:",precio,"  #")
print("# iva:",iva,"   #")
print("# pago total de iva :",pago_total_de_iva,"   #")
print("# iva:",iva,"    #")
print("####################")


#Ejercicio 8
#calcular el precio iva incluido
#donde el precio iva incluido se calcula
#total-precio sin iva
# mostrar el precio iva incluido

#Dectector iva
precio_sin_iva,total,total_iva=0.0,0.0,0.0

#INPUT
precio_sin_iva=float(input("ingrese el precio sin iva"))
total=float(input("ingrese total"))

#PROCESSING
total_iva=total-precio_sin_iva
#Dectector
# seran iva incluido>200
iva_incluido=(iva>200)
#Output
print("####################")
print("#   precio iva incluido#")
print("####################")
print(" # precio sin iva:",precio_sin_iva,"  #")
print("# total:",total,"   #")
print("# iva :",iva,"   #")
print("# iva incluido:",iva_incluido,"    #")
print("####################")

#Ejercicio 9
#calcular el costo total valor en libro
#donde el costo total valor en libro se calcula
#valor en libro1+valor en libro2
#mostrar la calidad del libro

#Detector calidad del libro
valor_en_libro1,valor_en_libro2,total=0.0,0.0,0.0

#input
valor_en_libro1=float(input("ingrese el valor del libro 1"))
valor_en_libro2=float(input("ingrese el valor del libro 2"))

#PROCESSING
total=valor_en_libro1+valor_en_libro2

#Detector
# sera calidad del libro>20
calidad_del_libro=(total>20)

#OUTPUT
print("####################")
print(" costo del valor en libros  ")
print("####################")
print("valor en libro 1:",valor_en_libro1,"     #")
print("valor en libro 2",valor_en_libro2,"      #")
print("total:",total,"     #")
print("calidad del libro:",calidad_del_libro,"      #")
print("####################")

#Ejercicio 10
#calcular la suma total danzas folklorica
#donde la suma total danzas folklorica se calcula
# total danza carnavalesca+total danza tijera
#mostrar participacion danza folklorica

#Detector participacion folklorica
total_danza_carnavalesca,total_danza_de_tijera,total_de_participacion=0,0,0
#input
total_danza_carnavalesca=int(input("ingrese el total danza carnavalesca"))
total_danza_de_tijera=int(input("ingrese el total danza de tijera"))
#PROCESSING
total_de_participacion=total_danza_carnavalesca+total_danza_de_tijera

#Detector
# sera participacion folklorica>5
participacion_folklorica=(total_de_participacion>5)

#OUTPUT
print("####################")
print(" total de danza folklorica ")
print("####################")
print("total danza carnavalesca:",total_danza_carnavalesca,"    #")
print("total danza de tijera",total_danza_de_tijera,"    #" )
print("total de participacion:",total_de_participacion,"       #")
print("participacion folkloricas:",participacion_folklorica,"    #")
print("####################")
