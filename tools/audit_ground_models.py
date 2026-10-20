"""Read-only model binding audit; emits reports, never changes game definitions."""
from pathlib import Path
import re,json,collections,zipfile,hashlib,csv,sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('G:/SteamLibrary/steamapps/common/Hearts of Iron IV')
OUT=ROOT/'tools/ground_model_audit';OUT.mkdir(exist_ok=True)
TOK=re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=]|[^\s{}=#]+')
def parse(text):
    ts=[m.group() for m in TOK.finditer(text) if not m.group().startswith('#')];i=0
    def seq():
        nonlocal i
        out=[]
        while i<len(ts) and ts[i]!='}':
            k=ts[i].strip('"');i+=1
            if i<len(ts) and ts[i]=='=':
                i+=1
                if i<len(ts) and ts[i]=='{':i+=1;v=seq();i+=1
                else:v=ts[i].strip('"') if i<len(ts) else '';i+=1
            else:v=None
            out.append((k,v))
        return out
    return seq()
def val(node,k,default=''):
    return next((v for key,v in reversed(node) if key==k),default)
def walk(node,kind):
    for k,v in node:
        if k==kind and isinstance(v,list):yield v
        if isinstance(v,list):yield from walk(v,kind)
def read(p):return p.read_text(encoding='utf-8-sig',errors='replace')
entities={};meshes={};vanillafiles={};duplicates=collections.defaultdict(list)
def ingest(text,src,mod):
    tree=parse(text)
    for kind,dest in [('entity',entities),('pdxmesh',meshes)]:
        for n in walk(tree,kind):
            name=val(n,'name')
            if not name:continue
            if mod and kind=='entity':duplicates[name].append(src)
            dest[name]={'node':n,'source':src,'mod':mod}
for p in sorted((GAME/'gfx').rglob('*')):
    if p.is_file():
        rel=p.relative_to(GAME).as_posix();vanillafiles[rel.lower()]=str(p)
        if p.suffix.lower() in ('.asset','.gfx'):ingest(read(p),str(p),False)
for base in ('DLC','integrated_dlc'):
    for p in sorted((GAME/base).rglob('*')):
        if p.is_file() and '/gfx/' in p.as_posix():
            virtual='gfx/'+p.as_posix().split('/gfx/',1)[1]
            vanillafiles[virtual.lower()]=str(p)
        if p.is_file() and p.suffix.lower() in ('.asset','.gfx'):
            ingest(read(p),str(p),False)
        if p.suffix.lower()=='.zip':
            with zipfile.ZipFile(p) as z:
                for name in z.namelist():
                    if name.lower().startswith('gfx/'):
                        vanillafiles[name.lower()]=str(p)+'!'+name
                        if name.endswith(('.asset','.gfx')):ingest(z.read(name).decode('utf-8-sig',errors='replace'),str(p)+'!'+name,False)
for p in sorted((ROOT/'gfx').rglob('*')):
    if p.suffix.lower() in ('.asset','.gfx'):ingest(read(p),p.relative_to(ROOT).as_posix(),True)
def resolve(name,seen=()):
    if name in seen:return 'broken','clone cycle: '+name
    e=entities.get(name)
    if not e:return 'missing','entity '+name+' not found'
    mesh=val(e['node'],'pdxmesh');clone=val(e['node'],'clone')
    if not mesh:
        if clone:return resolve(clone,seen+(name,))
        # Infantry attachment-only entities need an explicit separate review.
        return 'unresolved',e['source']+' (no mesh)'
    m=meshes.get(mesh)
    if not m:return 'broken','pdxmesh '+mesh+' not found; '+e['source']
    file=val(m['node'],'file');local=ROOT/file
    if local.is_file():
        vanilla=vanillafiles.get(file.lower())
        if vanilla and '!' not in vanilla and local.read_bytes()==Path(vanilla).read_bytes():return 'vanilla',file+' (identical to base game)'
        return 'mod',file
    if file.lower() in vanillafiles:return 'vanilla',file
    return 'broken','mesh file not found: '+file+'; '+m['source']
loc={}
for p in sorted((ROOT/'localisation/russian').glob('*.yml')):
    for line in read(p).splitlines():
        m=re.match(r'\s*([^#\s:]+):\s*(?:\d+\s*)?"(.*)"',line)
        if m:loc[m[1]]=m[2]
def label(k):
    s=loc.get(k,k)
    for _ in range(4):s=re.sub(r'\$([^$]+)\$',lambda m:loc.get(m[1],m[1]),s)
    return re.sub('§.','',s)
eq={}
for p in sorted((ROOT/'common/units/equipment').glob('*.txt')):
    for group in walk(parse(read(p)),'equipments'):
        for k,n in group:
            if isinstance(n,list):eq[k]={'node':n,'source':p.relative_to(ROOT).as_posix()}
def chain(k,seen=()):
    if k in seen or k not in eq:return []
    n=eq[k]['node'];out=[k]
    for field in ('parent','archetype'):
        for x in chain(val(n,field),seen+(k,)):
            if x not in out:out.append(x)
    return out
exclude=re.compile(r'(planes|helicopter|missile|convoy|uav|uniform|body_armor|grenade_launcher|infantry_equipments|additional_equipment|ES_support|ES_trains)')
rows=[]
for k,e in eq.items():
    if val(e['node'],'is_archetype')=='yes' or exclude.search(Path(e['source']).stem) or Path(e['source']).stem.startswith('00_'):continue
    ancestry=chain(k);sprite='';owner=''
    for a in ancestry:
        s=val(eq[a]['node'],'sprite')
        if isinstance(s,str) and s:sprite=s;owner=a;break
    names=[]
    # Exact and conventional suffixed names are both reported to avoid silently losing malformed references.
    for base in ([sprite] if sprite else [])+[k]+ancestry[1:]:
        for name in [base+'_entity',base]:
            if name in entities and name not in names:names.append(name)
    country=[]
    bases=([sprite] if sprite else [])+[k]+ancestry[1:]
    for name in entities:
        if re.match(r'^[A-Z]{3}_',name) and any(name[4:] in (b,b+'_entity') for b in bases):country.append(name)
    results=[(n,*resolve(n)) for n in names];cr=[(n,*resolve(n)) for n in country]
    if results:status=results[0][1]
    elif cr:status='country_only'
    elif sprite:status='missing'
    else:status='no_binding'
    rows.append(dict(id=k,name=label(k),source=e['source'],sprite=sprite,inherited_from=owner,status=status,models=results,country_models=cr))
units=[]
for p in sorted((ROOT/'common/units').glob('*.txt')):
    if p.stem in ('air','naval'):continue
    for group in walk(parse(read(p)),'sub_units'):
        for k,n in group:
            if not isinstance(n,list):continue
            sprite=val(n,'sprite');sprite=sprite if isinstance(sprite,str) else ''
            candidates=[x for x in (sprite+'_entity',k+'_entity') if x in entities]
            countries=[name for name in entities if re.match(r'^[A-Z]{3}_',name) and name[4:] in (sprite+'_entity',k+'_entity')]
            units.append(dict(id=k,name=label(k),source=p.relative_to(ROOT).as_posix(),sprite=sprite,
                generic=[(x,*resolve(x)) for x in dict.fromkeys(candidates)],countries=[(x,*resolve(x)) for x in countries]))
(OUT/'audit.json').write_text(json.dumps(dict(equipment=rows,units=units,duplicate_entities={k:v for k,v in duplicates.items() if len(v)>1}),ensure_ascii=False,indent=2),encoding='utf-8')
print('Equipment',len(rows),dict(collections.Counter(r['status'] for r in rows)));print('Units',len(units))

status_text={'missing':'Ссылка на отсутствующую entity','no_binding':'Отдельная привязка техники не найдена; возможна общая модель батальона','mod':'Модель из мода','vanilla':'Ванильная модель','broken':'Сломанная цепочка модели','country_only':'Есть только привязки по странам'}
with (OUT/'equipment.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,delimiter=';');w.writerow(['Название','ID','Результат','Sprite','Источник наследования','Файл','Найденные модели'])
    for r in rows:w.writerow([r['name'],r['id'],status_text[r['status']],r['sprite'],r['inherited_from'],r['source'],json.dumps(r['models'],ensure_ascii=False)])
def link(source):return '['+source+']('+ (ROOT/source).as_posix()+')'
def esc(s):return str(s).replace('|','/').replace('\n',' ')
lines=['# Аудит наземных 3D-моделей East Showdown','',
'Проверены 840 записей техники и 87 типов наземных подразделений. Источники: текущий мод, установленная HOI4 и её DLC. Игровые файлы не изменялись.','',
'Это статическая проверка ссылок, а не наблюдение в запущенной игре. Отсутствие отдельной модели шасси не означает невидимый батальон: он может использовать общую модель своего типа и страны.','',
'Проверены sprite, parent/archetype, entity/clone, pdxmesh и наличие mesh. Варианты конструктора отдельно не перечислены: они используют соответствующее шасси. Поезда, самолёты, ракеты, БПЛА и предметы экипировки исключены. Доступность DLC в конкретной игровой сессии не проверялась.','',
'## 1. Прямые ссылки на отсутствующие модели: 27 записей','',
'Проверены как буквальные имена sprite, так и имена с суффиксом `_entity`. Эти ошибки относятся к записи техники; общая модель батальона всё ещё может отображаться.','',
'| Техника | ID | Ссылка sprite | Файл |','|---|---|---|---|']
for r in rows:
    if r['status']=='missing':lines.append('| '+' | '.join([esc(r['name']),'`'+r['id']+'`','`'+r['sprite']+'`',link(r['source'])])+' |')
lines+=['','## 2. Не найдены модели типа батальона','']
for u in units:
    if not u['generic'] and not u['countries']:lines.append('- '+u['name']+' (`'+u['id']+'`): `'+u['sprite']+'_entity` — '+link(u['source']))
lines+=['','## 3. Ванильная пехота и конфликтующие назначения','',
'- В `gfx/entities/ec_flavor_pack.asset` есть `NTO_infantry_entity`, клонирующий `ROM_infantry_entity`: это ванильная румынская пехота из Death or Dishonor. В моде есть несколько определений `NTO_infantry_entity`, поэтому окончательный выбор требует проверки порядка загрузки/в игре.',
'- `POL_infantry_entity` в `gfx/entities/03_tanks_units.asset` клонирует отсутствующую `Stryker_entity`. Это сломанная ссылка, а не доказательство использования ванильной модели. Имя `POL_infantry_entity` также определено несколько раз.',
'- Общая `infantry_entity` остаётся ванильной. Она является запасным вариантом для стран без собственного подходящего определения. В России и Украине есть собственные модели пехоты; их нельзя целиком относить к ванильным.',
'- У Польши существует ванильная `POL_artillery_entity`. Она является кандидатом для подразделений со sprite `artillery`; общий `artillery_entity` в моде заменён на 2С1.','',
'Подразделения, ссылающиеся на общую пехоту (наличие собственной модели по ID/стране указано в полном списке ниже):','']
for u in units:
    if u['sprite']=='infantry':lines.append('- '+u['name']+' (`'+u['id']+'`)')
lines+=['','Подразделения со sprite `artillery`:','']
for u in units:
    if u['sprite']=='artillery':lines.append('- '+u['name']+' (`'+u['id']+'`)')
lines+=['','## 4. Без отдельной привязки техники: 783 записи','',
'Ни sprite в цепочке parent/archetype, ни совпадающая entity техники не найдены. Это список для подключения отдельных моделей, а не список гарантированно невидимых юнитов. Производные САУ, ЗРК, БРЭМ и другие варианты перечислены вместе со своими шасси.','']
groups=collections.defaultdict(list)
for r in rows:
    if r['status']=='no_binding':groups[r['source']].append(r)
for source,rs in groups.items():
    lines+=['### '+Path(source).stem,'',link(source),'']
    for r in rs:lines.append('- '+r['name']+' (`'+r['id']+'`)')
lines+=['','## 5. Все 87 подразделений: общие и страновые кандидаты','',
'Ниже перечислены кандидаты, а не имитация внутреннего порядка выбора движка. Разные определения одной entity и модели по ID подразделения могут менять результат.','']
tags=set()
for p in (ROOT/'common/country_tags').glob('*.txt'):
    tags.update(k for k,v in parse(read(p)) if re.fullmatch('[A-Z0-9]{3}',k))
for u in units:
    lines+=['### '+u['name']+' (`'+u['id']+'`)','', 'Sprite: `'+u['sprite']+'`. '+link(u['source']),'']
    selected=u['generic']+[r for r in u['countries'] if r[0][:3] in tags]
    if not selected:lines.append('Кандидаты не найдены.')
    for name,status,detail in selected:lines.append('- `'+name+'`: '+status_text.get(status,status)+'; `'+detail+'`')
lines+=['','## 6. Общие модели мода, подставленные другой технике','',
'Эти 30 записей не отнесены к отсутствующим или ванильным. Но наличие модели не означает соответствия внешнему виду конкретного образца. Например, БМД используют общую 2С1, а часть ПТРК — 2С7 или 2С3.','']
for r in rows:
    if r['status']=='mod':lines.append('- '+r['name']+' (`'+r['id']+'`) → `'+r['models'][0][2]+'`')
(OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reports:',OUT/'report.md',OUT/'equipment.csv')
