def verificar_vlan(vlan_numero):

    if 1 <= vlan_numero <= 1000:
        rango = "Normal"
    elif 1001 <= vlan_numero <= 4094:
        rango = "Extendido"
    else:
        rango = "Invalido"

    return f"La VLAN {vlan_numero} pertenece al rango {rango}."

if __name__ == "__main__":
    vlan_numero = int(input("Ingrese el numero de VLAN: "))
    resultado = verificar_vlan(vlan_numero)
    print(resultado)
