import ply.lex as lex
import ply.yacc as yacc
import streamlit as st

st.set_page_config(
    page_title="Parcial 2"
)

st.title("Parcial 2")
st.write("Integrantes:")
st.write("338803 - Saul Fernando Rodríguez Gutiérrez")
st.write("338817 - Eric Alejandro Aguilar Marcial")
st.write("338931 - Andrés Alexis Villalba García")

# Definición de las variables globales
tokens = ['A', 'BC']
t_A = r'a'
t_BC = r'bc'
t_ignore = ' \n'
n = 0
cuenta_a = 0
count_expres = 0

# Función para manejar errores léxicos
def t_error(t):
    t.lexer.skip(1)
    st.error(f"Carácter inesperado: {t.value[0]}, la cadena no pertenece al lenguaje.")
    exit()

# Crear el analizador léxico
lexer = lex.lex()

# Reglas de la gramática para el analizador sintáctico
def p_expresion(p):
    '''
    expresion : a_expresion BC expresion 
               | 
    '''
    global count_expres
    count_expres += 1

def p_a_expresion(p):
    '''
    a_expresion : A
                 | a_expresion A
    '''
    global n, cuenta_a
    if cuenta_a == 0:
        n = len(p)+1
    cuenta_a += 1

# Función para manejar errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token: {p.type}")
    else:
        print("Error de sintaxis en la entrada")

# Crear el analizador sintáctico
parser = yacc.yacc()

# Función para ejecutar el reconocedor de cadenas
def reconocer(cadena):
    global cuenta_a, count_expres
    cuenta_a, count_expres = 0, 0
    parser.parse(cadena)
    if cuenta_a == ((count_expres - 1) * count_expres):
        print("La cadena es válida.")
    else:
        print("La cadena no pertenece al lenguaje.")

# haz una función que cuente cuantas b y c hay en la cadena
def contar_b_c(cadena):
    cuenta_b, cuenta_c = 0, 0
    for i in cadena:
        if i == "b":
            cuenta_b += 1
        elif i == "c":
            cuenta_c += 1
    return cuenta_b, cuenta_c


st.text_input("Ingresa una cadena: ", key="cadena")
if st.button("Reconocer"):
    cadena = st.session_state.cadena
    b_cant, c_cant = contar_b_c(cadena)
    reconocer(cadena)
    print(f"b: {b_cant}, c: {c_cant}, count_expres: {count_expres}")
    if cuenta_a != ((count_expres - 1) * count_expres):
        st.error("La cadena no pertenece al lenguaje.")
    else:
        st.success("La cadena es válida.")
