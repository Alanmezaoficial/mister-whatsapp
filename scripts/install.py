from pathlib import Path
import argparse,shutil,sys
p=argparse.ArgumentParser(description='Instala la carpeta completa sin reemplazar versiones existentes')
p.add_argument('--edition',choices=['claude','codex'],required=True);p.add_argument('--destination',type=Path,required=True);a=p.parse_args()
source=Path(__file__).resolve().parents[1]/a.edition/'mister-whatsapp'
target=a.destination.expanduser().resolve()
if target.exists():p.error('El destino ya existe; revisa su versión. No se ha modificado.')
if not (source/'SKILL.md').is_file():p.error('Paquete incompleto')
shutil.copytree(source,target)
print('Skill copiada en '+str(target)+'. Abre una sesión nueva. El agente de negocio todavía no se ha construido.')
