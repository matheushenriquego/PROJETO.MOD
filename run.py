SUPLIER = dict()
INVENTORY = dict()
    
class Product:
    def __init__(self, name, unit_cost, quantity, code, category):
        self.name = name
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.code = code
        self.category = category
    
    def __repr__(self):
        return (
            f"Nome: {self.name}\n"
            f"Código: {self.code}\n"
            f"Categoria: {self.category}\n"
            f"Valor unitário: {self.unit_cost}\n"
            f"Quantidade em estoque: {self.quantity}\n"
        )
        
class Employer:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    
    def __repr__(self):
        return(f"Nome: {self.name}" f" | Código: {self.code}\n")

def list_products_quantities():
    for code,product in INVENTORY.items():
        print(product)
        
def build_custom_product():
    product = Product(
        name=input("Nome do produto: "),
        code=input("Código do produto: "),
        quantity=int(input("Quantidade: ")),
        category=input("Categoria: "),
        unit_cost=float(input("Valor unitário: "))
    )
    INVENTORY[product.code] = product
    
def get_inventory_value():
    total = 0
    for code, product in INVENTORY.items():
        total += product.unit_cost * product.quantity
    print(f"Inventario atual avaliando em :R${total}\n")      

def get_supliers():
    list_employers()
    choice=input("1.adicionar\n2.remover\n")
    if choice == "1":
        employer = Employer(
            name = input("Diga o nome do funcionario\n"),
            code = input("Diga o codigo do funcionario\n")
            )
        SUPLIER[employer.code] = employer
    elif choice == "2":
        code = input("diga o codigo do funcionario\n")
        try:
            test = SUPLIER.pop(code, None)
        except ValueError:
            print(f"'{code}' não é um numero de funcionario valido.") 
    else:
        print("INVALIDO")
    
def list_employers():
    for code,employer in SUPLIER.items():
        print(employer)

should_run = True

message = """
1 - Adicionar produto
2 - Atualizar produto
3 - Verificar quantidade de produtos em estoque
4 - Verificar valor do estoque atual
5 - adicionar/remover funcionario
6 - mostrar os funcioanrios atuais
0 - Fechar programa
"""

while should_run:
    print(message)
    result = input("Próxima ação: ")
    if result == "1":
        build_custom_product()
    elif result == "2":
        code = input('Diga o codigo do produto: ')
        product = INVENTORY.pop(code, None)
        if not product:
            print("Código não existente, adicione um produto primeiro.")
        else:
            print(product)
            build_custom_product()
        
    elif result == "3":
        list_products_quantities()
        
    elif result == "4":
        get_inventory_value()
        
    elif result == "5":
        get_supliers()
    
    elif result == "6":
        list_employers()
        
    elif result == "0":
        should_run = False
        
    else:
        print("Errado")


