
import streamlit as st

# Configuração inicial
st.set_page_config(
    page_title="Fórmula de Seleção de Monitores",
    layout="centered"
)

# Cabeçalho Institucional
st.markdown('''
<div style='text-align: center; font-family: Arial;'>
    <h2>UNIVERSIDADE FEDERAL DE CAMPINA GRANDE</h2>
    <h3>CENTRO DE FORMAÇÃO DE PROFESSORES</h3>
    <h4>UNIDADE ACADÊMICA DE ENFERMAGEM</h4>
    <h4>COORDENAÇÃO DE MONITORIA</h4>
</div>
''', unsafe_allow_html=True)

# Título do aplicativo
st.title("Fórmula de Seleção de Monitores")
st.markdown("### Calculadora de Pontuação para Disciplinas")

# Explicação da fórmula
with st.expander("📘 Explicação da Fórmula"):
    st.write("""A fórmula para decidir quais disciplinas terão monitores considera critérios que equilibram a necessidade atual e a equidade ao longo do tempo.

**Fórmula Completa:**
P = (Cp * Num / E) + B + R + S

**Termos da Fórmula:**
- **Cp**: Créditos práticos da disciplina
- **Num**: Número de alunos matriculados
- **E**: Número de turmas
- **B**: Prioridade por não ter recebido monitor no semestre anterior (1 se não teve, 0 se teve)
- **R**: Fator de rodízio (fixo, geralmente 20 para disciplinas sem monitor no semestre anterior)
- **S**: Pontuação acumulativa por semestres consecutivos sem monitor (10 * número de semestres consecutivos)""")

# Entrada de dados
st.sidebar.title("🔢 Insira os Dados")
cp = st.sidebar.number_input("Créditos Práticos (Cp):", min_value=0, step=1)
num = st.sidebar.number_input("Número de Alunos (Num):", min_value=0, step=1)
e = st.sidebar.number_input("Número de Turmas (E):", min_value=1, step=1)
b = st.sidebar.radio("Teve monitor no semestre anterior?", ["Sim", "Não"])
r = 20 if b == "Não" else 0
semestres_sem_monitor = st.sidebar.number_input("Semestres consecutivos sem monitor:", min_value=0, step=1)

# Cálculo do termo S
s = 10 * semestres_sem_monitor

# Cálculo do termo principal (Cp * Num / E)
if e > 0:
    carga_pratica = (cp * num) / e
else:
    carga_pratica = 0

# Pontuação final
p = carga_pratica + (1 if b == "Não" else 0) + r + s

# Resultado em destaque
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #007BFF;'>Resultado do Cálculo</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #28a745;'>{p}</h1>", unsafe_allow_html=True)
st.markdown("---")

# Exemplo prático
with st.expander("🔍 Exemplo Prático"):
    st.write("""**Disciplina A:**
- Créditos Práticos: 1
- Número de Alunos: 30
- Número de Turmas: 1
- Não teve monitor no semestre anterior
- Sem monitor por 2 semestres

**Cálculo:**
P = (1 * 30 / 1) + 1 + 20 + 20 = 71""")

# Rodapé
st.markdown('''
<div style='text-align: center; font-size: small; color: gray;'>
    Desenvolvido pela Coordenação de Monitoria da UAENF
</div>
''', unsafe_allow_html=True)
