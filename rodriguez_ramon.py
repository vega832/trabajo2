#Ejercicio_01
#Detector de calidad de algodon
cliente,producto_1,producto_2,cant_1,cant_2,costo_uni_1,costo_uni_2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
cant_1=int(input("Ingrese cantidad 1:"))
cant_2=int(input("Ingrese cantidad 2:"))
costo_uni_1=float(input("Ingrese costo uni 1:"))
costo_uni_2=float(input("Ingrese costo uni 2:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2

# DETECTOR
# Sera calidad de algodon cuando el total > 180
calidad_de_algodon=(total > 180)

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Cantidad 1: ",cant_1,"           #")
print("# Cantidad 2: ",cant_2," #")
print("# CostoUnitario 1: S/. ",costo_uni_1," #")
print("# CostoUnitario 2: S/. ",costo_uni_2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Calidad de algodon: ",calidad_de_algodon,  "#")
print("###########################")

#Ejercicio_02
#Detector marca
cliente,producto_1,producto_2,producto_3,cant_1,cant_2,cant_3,costo_uni_1,costo_uni_2,costo_uni_3,total="","","","",0,0,0,0.0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
producto_3=input("Ingrese producto 3:")
cant_1=int(input("Ingrese cantidad 1:"))
cant_2=int(input("Ingrese cantidad 2:"))
cant_3=int(input("Ingrese cantidad 3:"))
costo_uni_1=float(input("Ingrese costo uni 1:"))
costo_uni_2=float(input("Ingrese costo uni 2:"))
costo_uni_3=float(input("Ingrese costo uni 3:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2+cant_3*costo_uni_3

# DETECTOR
# Sera marca cuando el total > 250
marca=(total > 250)

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA     #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Producto 3: ",producto_3,"        #")
print("# Cantidad 1: ",cant_1,"           #")
print("# Cantidad 2: ",cant_2,"           #")
print("# Cantidad 3: ",cant_3,"           #")
print("# CostoUnitario 1: S/. ",costo_uni_1," #")
print("# CostoUnitario 2: S/. ",costo_uni_2," #")
print("# CostoUnitario 3: S/. ",costo_uni_3," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# marca: ",marca,  "#")
print("###########################")

#Ejercicio_03
#Detector nota aprobatoria
nombre_del_alumno,nota_1,nota_2,nota_3,promedio="","","","",0

# INPUT
nombre_del_alumno=input("Ingrese el nombre del alumno:")
nota_1=int(input("Ingrese nota 1:"))
nota_2=int(input("Ingrese nota 2:"))
nota_3=int(input("Ingrese nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# DETECTOR
# Sera nota aprobatoria si el promedio > 11
nota_aprobatoria=(promedio > 11)

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# nombre del alumno : ",nombre_del_alumno,"  #")
print("# nota 1: ",nota_1,"        #")
print("# nota 2: ",nota_2,"        #")
print("# nota 3: ",nota_3,"        #")
print("###########################")
print("promedio:",promedio,"      #")
print("# nota aprobatoria: ",nota_aprobatoria,  "#")
print("###########################")

#Ejercicio_04
#Detector de visita compulsiva a una libreria
cliente,cantidad_de_libros,visita_por_semana,total_de_visita="",0,0,0

# INPUT
cliente=input("Ingrese nombre del cliente:")
cantidad_de_libros=int(input("Ingrese cantidad de libros:"))
visita_por_semana=int(input("Ingrese visita por semana:"))

# PROCESSING
total_de_visita=cantidad_de_libros*visita_por_semana

# DETECTOR
# Sera visita compulsiva a una libreria si el total > 20
visita_compulsiva_a_una_libreria=(total_de_visita > 20)

# OUTPUT
print("###########################")
print("#     LIBRERIA      #")
print("###########################")
print("# Cliente: ",cliente,"  #")
print("# cantidad de libros: ",cantidad_de_libros,"        #")
print("# visita por semana: ",visita_por_semana,"        #")
print("###########################")
print("total de visita:",total_de_visita,"      #")
print("# visita compulsiva a una libreria: ",visita_compulsiva_a_una_libreria,  "#")
print("###########################")

#Ejercicio_05
#Detector de adiccion de las redes sociales
usuario,red_social_1,red_social_2,red_social_3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_dia="","","","",0,0,0,0

# INPUT
usuario=input("Ingrese nombre del usuario:")
red_social_1=input("Ingrese red social 1:")
red_social_2=input("Ingrese red social 2: ")
red_social_3=input("Ingrese red social 3:")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# DETECTOR
# Sera adiccion de las redes sociales si el total de horas por dia > 15
adiccion_de_las_redes_sociales=(total_de_horas_por_dia > 15)

# OUTPUT
print("###########################")
print("#       RED SOCIAL        #")
print("###########################")
print("# Usuario: ",usuario,"  #")
print("# red social 1: ",red_social_1,"        #")
print("# red social 2: ",red_social_2,"        #")
print("# red social 3: ",red_social_3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por dia:",total_de_horas_por_dia,"      #")
print("# adiccion de las redes sociales : ",adiccion_de_las_redes_sociales,  "#")
print("###########################")

#Ejercicio_06
#Detector de gusto por el deporte
nombre,deporte1,deporte2,deporte3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_semana="","","","",0,0,0,0

# INPUT
nombre=input("Ingrese nombre:")
deporte1=input("Ingrese deporte 1: ")
deporte2=input("Ingrese deporte 2: ")
deporte3=input("Ingrese deporte 3: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# DETECTOR
# Sera gusto por el deporte si el total de horas por semana > 6
gusto_por_el_deporte=(total_de_horas_por_semana > 6 )

# OUTPUT
print("###########################")
print("#       DEPORTE        #")
print("###########################")
print("# Nombre: ",nombre,"  #")
print("# deporte 1: ",deporte1,"        #")
print("# deporte 2: ",deporte2,"        #")
print("# deporte 3: ",deporte3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# gusto por el deporte : ",gusto_por_el_deporte,  "#")
print("###########################")

#Ejercicio_07
#Detector de automedicacion
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia,total_de_medicamentos_por_semana="","","",0,0,0

# INPUT
paciente=input("Ingrese paciente:")
medicamento_1=input("Ingrese medicamento 1: ")
medicamento_2=input("Ingrese medicamento 2: ")
cant_de_medicamento1_por_dia=int(input("Ingrese cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=int(input("Ingrese cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7

# DETECTOR
# Sera automedicacion si el total de medicamento por semana > 20
automedicacion=(total_de_medicamentos_por_semana > 20 )

# OUTPUT
print("###########################")
print("#       MEDICAMENTOS       #")
print("###########################")
print("# Paciente: ",paciente,"  #")
print("# medicamento 1: ",medicamento_1,"        #")
print("# medicamento 2: ",medicamento_2,"        #")
print("# cantidad de medicamento 1 por dia : ",cant_de_medicamento1_por_dia,"        #")
print("# cantidad de medicamento 2 por dia : ",cant_de_medicamento2_por_dia,"        #")
print("###########################")
print("total de medicamento por semana:",total_de_medicamentos_por_semana,"      #")
print("# automedicacion : ",automedicacion,  "#")
print("###########################")

#Ejercicio_08
#Detector de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# DETECTOR
# Sera bajo rendimiento academico si el total de horas por semana < 35
bajo_rendimiento_academico=(total_de_horas_por_semana < 35)

# OUTPUT
print("###########################")
print("#  RENDIMIENTO ACADEMICO  #")
print("###########################")
print("# alumno: ",alumno,"  #")
print("# horas dedicadas al aestudio por dia: ",horas_dedicadas_al_estudio_por_dia,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# bajo rendimiento academico : ",bajo_rendimiento_academico,  "#")
print("###########################")

#Ejercicio_09
#Detector de comprador compulsivo
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto1=input("Ingrese producto 1:")
producto2=input("Ingrese producto 2:")
cant_de_producto1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto2=int(input("Ingrese cantidad de producto 2:"))
costo_uni1=float(input("Ingrese costo unitario 1:"))
costo_uni2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*costo_uni2

# DETECTOR
# Sera comprador compulsivo si el total > 260
comprador_compulsivo=(total < 260)

# OUTPUT
print("###########################")
print("#   PRODUCTO DE BELLEZA   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto1,"        #")
print("# Producto 2: ",producto2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto2," #")
print("# Costo Unitario 1: S/. ",costo_uni1," #")
print("# Costo Unitario 2: S/. ",costo_uni2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("###########################")

#Ejercicio_10
#Detector de comprador pasivo
cliente,producto_1,producto_2,cant_de_producto_1,cant_de_producto_2,cost_uni_1,cost_uni_2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
cant_de_producto_1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto_2=int(input("Ingrese cantidad de producto 2:"))
costo_uni_1=float(input("Ingrese costo unitario 1:"))
costo_uni_2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1+cant_de_producto2*costo_uni_2

# DETECTOR
# Sera comprador_pasivo si el total > 15
comprador_pasivo=(total > 15)

# OUTPUT
print("###########################")
print("#   PRODUCTO DE GOLOSINAS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto_2," #")
print("# Costo Unitario 1: S/. ",costo_uni_1," #")
print("# Costo Unitario 2: S/. ",costo_uni_2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador pasivo: ",comprador_pasivo,  "#")
print("###########################")



                #CONVERSORES

# Ejercicio_1
# Declaracion variables
empleado,nro_dias,costo_por_dia,horas_extra,monto_a_pagar="",0,0.0,0,0.0

# INPUT
empleado="WALTER ORTIZ"
nro_dias=7
costo_por_dia=80
horas_extra=2

# PROCESSING
monto=(nro_dias*costo_por_dia)+(horas_extra*8)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado: ",empleado,"   #")
print("# Nro Dias   : ",nro_dias,"          #")
print("# Costo por Dia : ",costo_por_dia,"         #")
print("# Horas Extra: ",horas_extra,"           #")
print("###########################")
print("# Monto a Pagar: ",monto_a_pagar,"     #")
print("###########################")

# Ejercicio_2
# Declaracion variables
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3,total="","","","",0.0,0.0,0.0,0,0,0,0.0

# INPUT
cliente="Maribel Yaipen"
producto_1="Cafe"
producto_2="Cocoa"
producto_3="Leche"
costo_uni_1=1.20
costo_uni_2=1.00
costo_uni_3=4.50
cant_de_producto_1=3
cant_de_producto_2=2
cant_de_producto_3= 1

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA      #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Producto 1   : ",producto_1,"          #")
print("# Producto 2   : ",producto_2,"          #")
print("# Producto 3   : ",producto_3,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Costo Unitario 3: ",costo_uni_3,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("# Cantidad de Producto 3: ",cant_de_producto_3,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")


# Ejercicio_3
# Declaracion variables
alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
alumno="Kinyu Rodriguez"
nota_1=13
nota_2=15
nota_3=18

# PROCESSING
total=(nota_1+nota_2+nota_3)/3

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# Alumno: ",alumno,"   #")
print("# Nota 1   : ",nota_1,"          #")
print("# Nota 2   : ",nota_2,"          #")
print("# Nota 3   : ",nota_3,"          #")
print("###########################")
print("# Promedio: ",promedio,"     #")
print("###########################")

# Ejercicio_4
# Declaracion variables
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3="","","","",0.0,0.0,0.0,0,0,0,0.0

# INPUT
cliente="Gabriel Velasquez"
producto_1="wafer"
producto_2="Choco Soda"
producto_3="Oreo"
costo_uni_1=0.60
costo_uni_2=0.70
costo_uni_3=0.80
cant_de_producto_1=25
cant_de_producto_2=38
cant_de_producto_3=50

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Producto 1   : ",producto_1,"          #")
print("# Producto 2   : ",producto_2,"          #")
print("# Producto 3   : ",producto_3,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Costo Unitario 3: ",costo_uni_3,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("# Cantidad de Producto 3: ",cant_de_producto_3,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")

# Ejercicio_5
# Declaracion variables
paciente,medicamento_1,medicamento_2,medicamento_3,cant_de_medicamento_1_por_dia,cant_de_medicamento_2_por_dia,cant_de_medicamento_3_por_dia,total_de_medicamentos_por_semana="","","","",0,0,0,0

# INPUT
paciente="Barbara Perez"
medicamento_1="ibuprofeno"
medicamento_2="diclofenaco"
medicamento_3="paracetamol"
cant_de_medicamento_1_por_dia=3
cant_de_medicamento_2_por_dia=2
cant_de_medicamento_3_por_dia=1

# PROCESSING
total=cant_de_medicamento_1_por_dia+cant_de_medicamento_2_por_dia+cant_de_medicamento_3_por_dia

# OUTPUT
print("###########################")
print("#    RECETA MEDICA   #")
print("###########################")
print("# Paciente: ",paciente,"   #")
print("# Medicamento 1   : ",medicamento_1,"          #")
print("# Medicamento 2   : ",medicamento_2,"          #")
print("# Medicamento 3   : ",medicamento_3,"          #")
print("# Cantidad de Medicamento 1 por Dia: ",cant_de_medicamento_1_por_dia,"           #")
print("# Cantidad de Medicamento 2: ",cant_de_medicamento_2_por_dia,"           #")
print("# Cantidad de Medicamento 3: ",cant_de_medicamento_3_por_dia,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")


                #Impresion_ASCII
#Ejercicio_01
## Declaracion de variables de calidad de algodon
cliente,producto_1,producto_2,producto_3,cant_1,cant_2,cant_3,costo_uni_1,costo_uni_2,costo_uni_3,total="","","","",0,0,0,0.0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
producto_3=input("Ingrese producto 3:")
cant_1=int(input("Ingrese cantidad 1:"))
cant_2=int(input("Ingrese cantidad 2:"))
cant_3=int(input("Ingrese cantidad 3:"))
costo_uni_1=float(input("Ingrese costo uni 1:"))
costo_uni_2=float(input("Ingrese costo uni 2:"))
costo_uni_3=float(input("Ingrese costo uni 3:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2+cant_1*costo_uni_3

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Producto 3: ",producto_3,"        #")
print("# Cantidad 1: ",cant_1,"           #")
print("# Cantidad 2: ",cant_2," #")
print("# Cantidad 3: ",cant_3," #")
print("# CostoUnitario 1: S/. ",costo_uni_1," #")
print("# CostoUnitario 2: S/. ",costo_uni_2," #")
print("# CostoUnitario 3: S/. ",costo_uni_3," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Calidad de algodon: ",calidad_de_algodon,  "#")
print("###########################")

#Ejercicio_02
## Declaracion de variables de marca
cliente,producto_1,producto_2,producto_3,cant_1,cant_2,cant_3,costo_uni_1,costo_uni_2,costo_uni_3,total="","","","",0,0,0,0.0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
producto_3=input("Ingrese producto 3:")
cant_1=int(input("Ingrese cantidad 1:"))
cant_2=int(input("Ingrese cantidad 2:"))
cant_3=int(input("Ingrese cantidad 3:"))
costo_uni_1=float(input("Ingrese costo uni 1:"))
costo_uni_2=float(input("Ingrese costo uni 2:"))
costo_uni_3=float(input("Ingrese costo uni 3:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2+cant_3*costo_uni_3

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA     #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Producto 3: ",producto_3,"        #")
print("# Cantidad 1: ",cant_1,"           #")
print("# Cantidad 2: ",cant_2,"           #")
print("# Cantidad 3: ",cant_3,"           #")
print("# CostoUnitario 1: S/. ",costo_uni_1," #")
print("# CostoUnitario 2: S/. ",costo_uni_2," #")
print("# CostoUnitario 3: S/. ",costo_uni_3," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# marca: ",marca,  "#")
print("###########################")

#Ejercicio_03
#Declaracion de variables de nota aprobatoria
nombre_del_alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
nombre_del_alumno=input("Ingrese el nombre del alumno:")
nota_1=int(input("Ingrese nota 1:"))
nota_2=int(input("Ingrese nota 2:"))
nota_3=int(input("Ingrese nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# nombre del alumno : ",nombre_del_alumno,"  #")
print("# nota 1: ",nota_1,"        #")
print("# nota 2: ",nota_2,"        #")
print("# nota 3: ",nota_3,"        #")
print("###########################")
print("promedio:",promedio,"      #")
print("# nota aprobatoria: ",nota_aprobatoria,  "#")
print("###########################")

#Ejercicio_04
## Declaracion de variables de visita compulsiva a una libreria
cliente,cantidad_de_libros,visita_por_semana,total_de_visita="",0,0,0

# INPUT
cliente=input("Ingrese nombre del cliente:")
cantidad_de_libros=int(input("Ingrese cantidad de libros:"))
visita_por_semana=int(input("Ingrese visita por semana:"))

# PROCESSING
total_de_visita=cantidad_de_libros*visita_por_semana

# OUTPUT
print("###########################")
print("#     LIBRERIA      #")
print("###########################")
print("# Cliente: ",cliente,"  #")
print("# cantidad de libros: ",cantidad_de_libros,"        #")
print("# visita por semana: ",visita_por_semana,"        #")
print("###########################")
print("total de visita:",total_de_visita,"      #")
print("# visita compulsiva a una libreria: ",visita_compulsiva_a_una_libreria,  "#")
print("###########################")

#Ejercicio_05
# Declaracion de variables de adiccion de las redes sociales
usuario,red_social_1,red_social_2,red_social_3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_dia="","","","",0,0,0,0

# INPUT
usuario=input("Ingrese nombre del usuario:")
red_social_1=input("Ingrese red social 1:")
red_social_2=input("Ingrese red social 2: ")
red_social_3=input("Ingrese red social 3:")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# OUTPUT
print("###########################")
print("#       RED SOCIAL        #")
print("###########################")
print("# Usuario: ",usuario,"  #")
print("# red social 1: ",red_social_1,"        #")
print("# red social 2: ",red_social_2,"        #")
print("# red social 3: ",red_social_3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por dia:",total_de_horas_por_dia,"      #")
print("# adiccion de las redes sociales : ",adiccion_de_las_redes_sociales,  "#")
print("###########################")

#Ejercicio_06
# Declaracion de variables de gusto por el deporte
nombre,deporte1,deporte2,deporte3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_semana="","","","",0,0,0,0

# INPUT
nombre=input("Ingrese nombre:")
deporte1=input("Ingrese deporte 1: ")
deporte2=input("Ingrese deporte 2: ")
deporte3=input("Ingrese deporte 3: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# OUTPUT
print("###########################")
print("#       DEPORTE        #")
print("###########################")
print("# Nombre: ",nombre,"  #")
print("# deporte 1: ",deporte1,"        #")
print("# deporte 2: ",deporte2,"        #")
print("# deporte 3: ",deporte3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# gusto por el deporte : ",gusto_por_el_deporte,  "#")
print("###########################")

#Ejercicio_07
# Declaracion de variables de automedicacion
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia,total_de_medicamentos_por_semana="","","",0,0,0

# INPUT
paciente=input("Ingrese paciente:")
medicamento_1=input("Ingrese medicamento 1: ")
medicamento_2=input("Ingrese medicamento 2: ")
cant_de_medicamento1_por_dia=int(input("Ingrese cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=int(input("Ingrese cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7

# OUTPUT
print("###########################")
print("#       MEDICAMENTOS       #")
print("###########################")
print("# Paciente: ",paciente,"  #")
print("# medicamento 1: ",medicamento_1,"        #")
print("# medicamento 2: ",medicamento_2,"        #")
print("# cantidad de medicamento 1 por dia : ",cant_de_medicamento1_por_dia,"        #")
print("# cantidad de medicamento 2 por dia : ",cant_de_medicamento2_por_dia,"        #")
print("###########################")
print("total de medicamento por semana:",total_de_medicamentos_por_semana,"      #")
print("# automedicacion : ",automedicacion,  "#")
print("###########################")

#Ejercicio_08
# Declaracion de variables de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# OUTPUT
print("###########################")
print("#  RENDIMIENTO ACADEMICO  #")
print("###########################")
print("# alumno: ",alumno,"  #")
print("# horas dedicadas al aestudio por dia: ",horas_dedicadas_al_estudio_por_dia,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# bajo rendimiento academico : ",bajo_rendimiento_academico,  "#")
print("###########################")

#Ejercicio_09
# Declaracion de variables de comprador compulsivo
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto1=input("Ingrese producto 1:")
producto2=input("Ingrese producto 2:")
cant_de_producto1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto2=int(input("Ingrese cantidad de producto 2:"))
costo_uni1=float(input("Ingrese costo unitario 1:"))
costo_uni2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*costo_uni2

# OUTPUT
print("###########################")
print("#   PRODUCTO DE BELLEZA   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto1,"        #")
print("# Producto 2: ",producto2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto2," #")
print("# Costo Unitario 1: S/. ",costo_uni1," #")
print("# Costo Unitario 2: S/. ",costo_uni2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("###########################")

#Ejercicio_10
# Declaracion de variables de comprador pasivo
cliente,producto_1,producto_2,cant_de_producto_1,cant_de_producto_2,cost_uni_1,cost_uni_2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
cant_de_producto_1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto_2=int(input("Ingrese cantidad de producto 2:"))
costo_uni_1=float(input("Ingrese costo unitario 1:"))
costo_uni_2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1+cant_de_producto2*costo_uni_2

# OUTPUT
print("###########################")
print("#   PRODUCTO DE GOLOSINAS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto_2," #")
print("# Costo Unitario 1: S/. ",costo_uni_1," #")
print("# Costo Unitario 2: S/. ",costo_uni_2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador pasivo: ",comprador_pasivo,  "#")
print("###########################")
