import os
import sys
import PYTHON01.funciones
def main():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls') 

    print("Calcular Renta: ")    
    print("1. Calcular ISR ")        
    print("2. Calcular ISSS ")
    print("3. Calcular AFP ")
    print("4. Salir ")       
    opcion=int(input('Digite la opción: '))
    if opcion==1 and opcion<4:
        sueldo=float(input('\nDigite el sueldo: '))
    if opcion==1:
        print("El impuesto sobre la renta es de: $", PYTHON01.funciones.calculo_isr(sueldo))
        main()
    elif opcion==2:
        print("El total del seguro es de: $: ",PYTHON01.funciones.calculo_isss(sueldo))
        main()
    elif opcion==3:
        print("El total de afp es de: $: ",PYTHON01.funciones.calculo_afp(sueldo))
        main()
    else:
        sys.exit()

if __name__=="__main__":
    main()
