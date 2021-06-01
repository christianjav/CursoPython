
def main():
    input("Digite una palabra: ")

if (__name__=='__main__'):
    try:
        main()
    except KeyboardInterrupt as e:
        print(f"\nSaliendo... {e}")
        exit()
    except ZeroDivisionError as e:
        print(f"\n error {e}")
    except TypeError as e:
        print(f"\n error {e}")
    else:
        print("no hubo errores")
    finally:
        print("Seguimos")

    suma=4+6
    print(f'la suma es: {suma}')
    # try:
    #     main()
    # except:
    #     print("\nSaliendo...")
    #     exit()
    