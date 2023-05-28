import ply.lex as lex
import ply.yacc as yacc
import streamlit as st

st.set_page_config(
    page_title="Parcial 2"
)

st.title("Parcial 2")
st.write("338803 - Saul Fernando Rodríguez Gutiérrez")
st.write("338803 - Eric Alejandro Aguilar Marcial")
st.write("338931 - Andrés Alexis Villalba García")

tokens = ['PARDER', 'PARIZQ', 'ABC']

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_ABC = r'abc'
t_ignore = '\n'

contar_der = 0
contar_izq = 1

def t_error(t):
    t.lexer.skip(1)
    print(f"Carácter inesperado: {t.value[0]}")
    exit()
   

# Crear el analizador léxico
lexer = lex.lex()

# Reglas de la gramática para el analizador sintáctico
def p_expression(p):
    '''
    expression : p_left_expression ABC p_right_expression
    '''

def p_par_izq_expression(p):
    '''
    p_left_expression : PARIZQ
                 | p_left_expression PARIZQ
    '''
    # Contamos el numero de parentecis izquierdos
    global contar_izq
    contar_izq += 1

def p_par_der_expression(p):
    '''
    p_right_expression : PARDER p_right_expression
                 | 
    '''
    # Contamos el numero de parentecis derechos
    global contar_der
    contar_der += 1

# Función para manejar errores sintácticos
def p_error(p):
    if p:
        st.error(f"Error de sintaxis en el token")
    else:
        st.error("Error de sintaxis en la entrada")

# Crear el analizador sintáctico
parser = yacc.yacc()

# Función para ejecutar el reconocedor de cadenas
def analizar(cadena):
    # Definición de variables globales
    global contar_izq, contar_der
    # Inicializamos las variables globales en 0's
    contar_izq, contar_der = 1,0
    parser.parse(cadena, lexer=lexer)
    # Condicional para verificar si la cadena es válida o no
    if contar_izq > 1 and  contar_izq - (contar_der) == 1:
        st.success("La cadena es válida.")
    else:
        st.error("La cadena no pertenece al lenguaje.")


entrada = st.text_input("Ingresa la cadena a analizar")
if st.button("Analizar"):
    analizar(entrada)