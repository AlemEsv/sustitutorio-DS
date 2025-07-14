# objeto mediator

# registra referencias a A, B, C y define execute(data) que:
# - envía a A, recibe respuesta (o lanza excepción tras 3 intentos)
# - envía B, gestiona si B responde lento ( menos a 500ms) 
# - envía a C, realiza loggin del id en stdout
