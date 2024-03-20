#
#        David Reyes Rodríguez - Entregable-01
#
#               PROYECTO ENTREGABLE 01
#             SISTEMA DE PAGO DE LA POPS®
#                ---------------------

# DEFINICION DE VARIABLE DE PRECIOS

opcion_general = "Si"
total_ventas_del_dia = 0
total_helados_vendidos = 0
total_batidos_vendidos = 0

while opcion_general == "Si":
    precio_v = 600          # v (vainilla)
    precio_c = 700          # c (chocolate)
    precio_b = 1200         # b (batidos)
    desc_pvp = float(.15)   # desc_pvp (descuento PuraVidaPops)
    totaldesc_pvp = 0       # se asigna el valor 0 para que cuando sea llamada no de error

    # PEDIDO DEL CLIENTE

    print("\nBienvenido al sistema de pago de la POPS®\n")
    print("Pedido del cliente")
    cantidad_v = int(input("Cantidad de helados de vainilla: "))     # v (vainilla)
    cantidad_c = int(input("Cantidad de helados de chocolate: "))    # c (chocolate)
    cantidad_b = int(input("Cantidad de batidos: "))                 # b (batidos)

    # OPERACIONES

    total_v = cantidad_v * precio_v         # v (vainilla)
    total_c = cantidad_c * precio_c         # c (chocolate)
    total_b = cantidad_b * precio_b         # b (batidos)
    subt_g = total_v + total_c + total_b    # subt_g (subtotal_general)

    # CONDICION

    opcion = input("\nEl cliente cuenta con una tarjeta de cliente frecuente 'PuraVidaPops' (Si/No): ")
    if opcion == "Si":
        totaldesc_pvp = subt_g * desc_pvp       # en esta variable se almacena el total del descuento
        total_g = subt_g - totaldesc_pvp
    elif opcion == "No":
        total_g = subt_g
    else:
        print("\n*La opcion que ingresó no es valida. Se interpreta como un 'No'.*")
        total_g = subt_g                        # la tomo como si fuera un "no"

    # IMPRESION DEL REPORTE

    print("\nLa cuenta total del cliente es:\n")
    print(str(total_v) + " colones por helados de vainilla.")
    print(str(total_c) + " colones por helados de chocolate.")
    print(str(total_b) + " colones por batidos.")
    print("Total sin descuento: " + str(subt_g))
    print("Descuento por PuraVidaPops: " + str(int(totaldesc_pvp)) + " colones.")
    print("Total a pagar: " + str(int(total_g)) + " colones.\n")

    total_ventas_del_dia += total_g
    total_helados_vendidos += cantidad_v + cantidad_c
    total_batidos_vendidos += cantidad_b

    opcion_general = input("Desea atender a otro cliente (Si/No): ")

print("Reporte fnal del día para Heladería POPS®")
print("-------------------------------------------")
print("Total de ventas del día: " + str(total_ventas_del_dia) + " colones.")
print("Total de helados vendidos: " + str(total_helados_vendidos))
print("Total de batidos vendidos: " + str(total_batidos_vendidos))
