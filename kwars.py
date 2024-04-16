
database = {
    'p1': {
        'primer_nombre': 'Pablo',
        'segundo_nombre': 'Diego',
        'primer_apellido': 'Ruiz',
        'segundo_apellido': 'Picasso',
    },
    'p2': {
        'primer_nombre': 'Juan Cruz',
        'primer_apellido': 'Rupcic',
        'segundo_apellido': 'Gattoni',
    },
    'p3': {
        'primer_nombre': 'Martin',
        'segundo_nombre': 'Andres',
        'primer_apellido': 'Velazquez',
        'segundo_apellido': 'Carrera',
    },
    'p4': {
        'primer_nombre': 'Pablo',
        'primer_apellido': 'Martinez',
    },
    'p5': {
        'primer_nombre': 'Delfina',
        'primer_apellido': 'Clavel',
        'segundo_apellido': 'Ruiz',
    }
    
}

def buscar_datos(*args, **kwargs):
    for k, v in kwargs.items():
        coincidencia = True
        for i, n in v.items():
            if n not in args:
                coincidencia = False
        if coincidencia:
            print(f'la persona que buscas es {k}')
            return k
    return'la persona no existe'  
        
            

buscar_datos('Pablo', 'Martinez', 'Rodriguez',**database)
