# Guardia de PDF y Word (26 nov 2026).
# Si un push devuelve un archivo de pdf/ a una versión que ya tuvo antes (p. ej. una ficha antigua
# que pisa a la nueva al regenerar con un script viejo), lo deja como estaba justo antes del push.
# Para una vuelta atrás querida, poner [vuelta-atras] en el mensaje del commit.
import subprocess, sys
def g(*a): return subprocess.run(['git',*a],capture_output=True,text=True,check=True).stdout.strip()
antes, ahora = sys.argv[1], sys.argv[2]
if set(antes) == {'0'}: sys.exit(0)
msgs = g('log','--format=%B',f'{antes}..{ahora}')
if '[vuelta-atras]' in msgs: print('Vuelta atrás pedida: no toco nada'); sys.exit(0)
cambiados = [f for f in g('diff','--name-only','--diff-filter=M',antes,ahora,'--','pdf').splitlines() if f]
restaurados = []
for f in cambiados:
    nuevo = g('rev-parse',f'{ahora}:{f}')
    previo = g('rev-parse',f'{antes}:{f}')
    viejos = set(g('log','--format=%H',antes,'--',f).splitlines())
    blobs_viejos = set()
    for c in viejos:
        try: blobs_viejos.add(g('rev-parse',f'{c}:{f}'))
        except subprocess.CalledProcessError: pass
    blobs_viejos.discard(previo)
    if nuevo in blobs_viejos:
        g('checkout',antes,'--',f); restaurados.append(f)
        print('RESTAURADO',f,'(el push lo devolvía a una versión antigua)')
open('restaurados.txt','w').write('\n'.join(restaurados))
