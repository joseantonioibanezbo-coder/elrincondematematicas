"""Bachillerato por unidades (20 nov 2026).
EJECUTAR SIEMPRE DESPUÉS de regenerar la web con build.py:
    python3 build.py site && python3 herramientas/bach_unidades.py
Coloca los vídeos de ejercicios de 1º/2º Bach Ciencias dentro de cada unidad (según el índice del libro)
y rellena 1º/2º Bach CCSS con los vídeos de esos temas. Lo mejor sería integrarlo en build.py.
"""
import re
def topics(s):
    a=s.find('<div class="chips">'); b=s.find('<h2>Más vídeos de')
    seg=s[a:b]
    out={}
    for m in re.finditer(r'<details><summary><span>(.*?)</span><span class="n">[^<]*</span></summary><ul class="vl">(.*?)</ul></details>',seg,re.S):
        t=m.group(1); lis=re.findall(r'<li>.*?</li>',m.group(2),re.S)
        cur=out.setdefault(t,[])
        ids={re.search(r'youtu\.be/([\w-]+)',x).group(1) for x in cur}
        for x in lis:
            i=re.search(r'youtu\.be/([\w-]+)',x).group(1)
            if i not in ids: cur.append(x); ids.add(i)
    return out,a,b

import re,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
LH='Límites. Regla de L&#x27;Hopital'
NUM=['Fracciones. Operar','Operaciones combinadas','Potencias. Propiedades y operaciones','Reales. Clasificación y representación','Intervalos y semirrectas en la recta real','Notación científica. Ejercicios y problemas','Radicales. Simplificación','Radicales. Operar con radicales','Radicales. Potencias de exponente fraccionario','Radicales. Racionalizar denominadores','Radicales. Uso para resolver problemas','Logaritmos. Definición y propiedades']
POL=['Algebra. Uso del lenguaje algebraico','Polinomios. Operaciones','Polinomios. Igualdades notables','Polinomios. Valor numérico','Polinomios. División por Ruffini y algoritmo general','Polinomios. Teorema del Resto','Polinomios. Descomposición factorial','Fracciones algebraicas. Simplificar','Fracciones algebraicas. Operar','Descomposición polinómica de un número']
ECU=['Ecuación de 1º grado','Ecuación de 2º grado','Ecuación bicuadrada','Ecuación de grado superior a dos','Ecuaciones. Racionales','Ecuación racional','Ecuación Radical','Ecuación Logarítmica','Ecuación Exponencial','Inecuaciones. Resolver','Inecuaciones. Problemas']
SIS1=['Sistemas de ecuaciones lineales','Sistemas de ecuaciones lineales. Método de Gauss','Sistemas de ecuaciones lineales. Discutir y resolver con parámetros','Sistema de ecuaciones no lineales','Sistemas de inecuaciones','Sistemas. Problemas']
SISM=['Matrices. Operaciones','Matrices. Rango','Sistemas de ecuaciones lineales: Matriz inversa','Sistemas de ecuaciones. Regla de Cramer','Sistemas de ecuaciones. Teorema de Rouché Frobenius']
FUN=['Funciones. Análisis de la gráfica','Funciones. Dominio de una función','Funciones. Puntos de corte con los ejes','Funciones. Estudio de la simetría','Funciones. Representación gráfica','Funciones. Representación gráfica de una función','Funciones. Resolver problemas de la vida cotidiana']
ELEM=['Funciones. Ecuaciones de la recta','Funciones. Función cuadrática']
LIM=['Límites. Cálculo de límites','Funciones. Asíntotas','Funciones. Continuidad y derivabilidad']
DER=['Derivadas. Definición','Derivadas. Cálculo','Derivadas. Ecuación de la recta tangente a una función']
APL=['Derivadas. Aplicaciones','Funciones. Monotonía. Extremos relativos','Problemas de optimización']
PROB=['Combinatoria. Problemas','Probabilidad']
DIST=['Distribución Normal y Binomial']
B1={1:NUM,2:POL+ECU,3:SIS1+SISM,4:['Trigonometría','Trigonometría. Relaciones fundamentales','Trigonometría. Ecuaciones e identidades','Teorema de Pitágoras. Aplicaciones','Teorema de la Altura','Semejanza de triángulos. Teorema de Thales','Trigonometría. Resolución de triángulos no rectángulos','Trigonometría. Problemas'],
 5:['Números Complejos'],6:['Geometría en el plano. Vectores en el plano','Geometría en el plano. Ecuaciones de la recta','Geometría en el plano. Posición relativa'],
 8:FUN+ELEM,9:LIM+[LH],10:DER,11:APL,12:['Integrales. Integral por partes','Integrales. Integral racional']}
B1CS={1:NUM,3:POL,4:ECU+SIS1,5:FUN,6:ELEM,7:LIM,8:DER+APL,11:PROB,12:DIST}
M2=['Matrices. Operaciones','Matrices. Rango','Matrices. Cálculo de la inversa','Matrices. Ecuaciones matriciales']
D2=['Determinantes. Propiedades','Determinantes. Desarrollo por adjuntos']
S2=['Sistemas de ecuaciones lineales. Método de Gauss','Sistemas de ecuaciones. Teorema de Rouché Frobenius','Sistemas de ecuaciones. Regla de Cramer','Sistemas de ecuaciones lineales: Matriz inversa','Sistemas de ecuaciones lineales. Discutir y resolver con parámetros','Sistemas. Problemas']
REP2=['Funciones. Dominio de una función','Funciones. Asíntotas','Funciones. Análisis de la gráfica','Funciones. Función cuadrática','Funciones. Ecuaciones de la recta','Funciones. Representación gráfica','Funciones. Representación gráfica de una función']
B2={1:M2,2:D2,3:S2,4:['Geometría en el espacio. Vectores','Geometría en el plano. Vectores en el plano','Geometría en el espacio. Puntos alineados','Geometría en el espacio. Puntos coplanarios'],
 5:['Geometría en el espacio. Ecuación de la recta','Geometría en el espacio. Ecuación del plano','Geometría en el espacio. Posición relativa de dos rectas','Geometría en el espacio. Posición relativa de recta y plano','Geometría en el espacio. Posición relativa de dos planos'],
 6:['Geometría en el espacio. Punto simétrico','Geometría en el espacio. Distancia entre dos rectas','Geometría en el espacio. Problemas métricos'],
 7:['Límites. Cálculo de límites','Funciones. Continuidad y derivabilidad'],8:DER,9:APL+[LH],10:REP2,
 11:['Integrales. Integral inmediata','Integrales. Cambio de variable','Integrales. Integral por partes','Integrales. Integral racional'],12:['Integrales. Cálculo de áreas','Integrales. Resolución problemas'],13:PROB,14:DIST}
B2CS={1:M2,2:D2,3:S2,4:['Inecuaciones. Resolver','Sistemas de inecuaciones'],5:['Límites. Cálculo de límites','Funciones. Continuidad y derivabilidad'],6:DER,7:APL,8:REP2,
 9:['Integrales. Integral inmediata','Integrales. Cálculo de áreas','Integrales. Resolución problemas'],10:PROB,11:DIST}
def nv(n): return f'{n} vídeo'+('s' if n!=1 else '')
def block(t,lis): return f'<details><summary><span>{t}</span><span class="n">{nv(len(lis))}</span></summary><ul class="vl">{"".join(lis)}</ul></details>'
def build(page,src,M,leftover):
    s=open(R+page).read(); T,_,_=topics(open(src).read())
    used=set(); total=0
    def unit(m):
        nonlocal total
        u=m.group(0); n=int(re.search(r'Unidad (\d+) ·',u).group(1))
        ts=[t for t in M.get(n,[]) if t in T]; used.update(ts)
        u=u.replace('<ul class="vl"><p class="muted">🎬 Vídeo lecciones: próximamente.</p>','<p class="muted">🎬 Vídeo lecciones: próximamente.</p>')
        u=re.sub(r'<div class="ej">.*?</div>(?=<p class="ask">)','',u,flags=re.S)
        u=re.sub(r' · ▶ \d+ vídeos? de ejercicios','',u)
        if ts:
            k=sum(len(T[t]) for t in ts); total+=k
            u=re.sub(r'(<span class="n">[^<]*)</span>',lambda x:x.group(1)+f' · ▶ {nv(k)} de ejercicios</span>',u,count=1)
            ej='<div class="ej"><p class="ejt">▶ Ejercicios resueltos en vídeo de esta unidad</p>'+''.join(block(t,T[t]) for t in ts)+'</div>'
            u=u.replace('<p class="ask">',ej+'<p class="ask">',1)
        return u
    s=re.sub(r'<details class="unit".*?</details>(?=<details class="unit"|</section>)',unit,s,flags=re.S)
    # zona tras las unidades: sustituir por "Más vídeos"
    a=s.find('</section>',s.find('class="les"'))+len('</section>')
    b=s.find('</main>')
    tail=s[a:b]
    otros=re.search(r'<details><summary><span>Otros vídeos</span>.*?</details>',tail,re.S)
    rest=[t for t in T if t not in used] if leftover else []
    name=re.search(r'<h1>(.*?)</h1>',s).group(1)
    nt=''
    if rest or otros:
        nt=f'<h2>Más vídeos de {name}</h2>'+''.join(block(t,T[t]) for t in rest)+(otros.group(0) if otros else '')
    s=s[:a]+nt+s[b:]
    if '.unit .ej' not in s:
        s=s.replace('</style>','.unit .ej{margin:12px 0 4px}.unit .ejt{font-weight:700;margin:0 2px 8px;font-size:15px}.unit .ej details{margin:0 0 8px}.unit .ej summary{font-size:16px;padding:10px 14px}\n</style>',1)
    open(R+page,'w').write(s)
    return total,rest
if __name__=='__main__':
    # Lee los temas de bach1/bach2 tal como los deja build.py (con chips) ANTES de modificar nada
    import tempfile
    tmp={}
    for f in ('bach1.html','bach2.html'):
        s=open(R+f).read()
        if '<div class="chips">' not in s: raise SystemExit(f+': ya está organizado por unidades (o build.py cambió). No hago nada.')
        t=tempfile.NamedTemporaryFile('w',delete=False,suffix='.html'); t.write(s); t.close(); tmp[f]=t.name
    for p,src,M,lo in [('bach1.html',tmp['bach1.html'],B1,True),('bach2.html',tmp['bach2.html'],B2,True),('bach1cs.html',tmp['bach1.html'],B1CS,False),('bach2cs.html',tmp['bach2.html'],B2CS,False)]:
        print(p,build(p,src,M,lo))
    s=open(R+'bachillerato.html').read()
    for f,n in [('bach1cs','Matemáticas Aplicadas a las CCSS I'),('bach2cs','Matemáticas Aplicadas a las CCSS II')]:
        k=len(set(re.findall(r'youtu\.be/([\w-]+)',open(R+f+'.html').read())))
        s=re.sub(rf'(href="{f}\.html"><h3>[^<]*</h3><p>)[^<]*',rf'\g<1>{n} · {k} vídeos',s)
    open(R+'bachillerato.html','w').write(s)
