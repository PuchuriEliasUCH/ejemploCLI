import manage_json
import click


@click.group()
def main():
    pass

@main.command()
def users():
    users = manage_json.read_json()['users']
    for user in users:
        print(f"{user['codigo']} - {user['name']}")

@main.command()
@click.option('--codigo', prompt = 'Código', help = 'Nombre del usuario', type = int)
@click.option('--name', prompt = 'Nombre', help = 'Nombre del usuario')
@click.option('--lastname', prompt = 'Apellido', help = "Apellido de usuario")
@click.pass_context
def add(context, codigo, name, lastname):
    if not name or not lastname:
        context.fail('El nombre y apellido del usuario son obligatorios')
    else: 
        data = manage_json.read_json()
        user = next((x for x in data['users'] if x['codigo'] == codigo), None)
        if user is None:
            new_user = {
                'codigo': codigo,
                'name': name,
                'lastname': lastname
            }
            data['users'].append(new_user)
            manage_json.write_json(data)
            print(f"Nuevo contacto agregado correctamente")
        else:
            print("Este trabajador ya está registrado")

@main.command()
@click.argument('id', type = int)
def user(id):
    data = manage_json.read_json()
    user = next((x for x in data['users'] if x['codigo'] == id), None)
    if user is None: 
        print(f"El usuario no existe")
    else:
        print(f"{user['codigo']} - {user['name']}")

@main.command()
@click.argument('id', type = int)
def delete(id):
    data = manage_json.read_json()
    user = next((x for x in data['users'] if x['codigo'] == id), None)
    if user is None: 
        print(f"El usuario no existe")
    else:
        data['users'].remove(user)
        manage_json.write_json(data)
        print("El usuario fue eliminado correctamente")

if __name__ == "__main__":
    main();