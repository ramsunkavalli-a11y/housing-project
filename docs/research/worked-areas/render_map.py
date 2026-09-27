"""Render the map from saved evidence; requires matplotlib and pyproj."""
import pathlib,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Patch
from matplotlib.lines import Line2D
from pyproj import Transformer
root=pathlib.Path(__file__).resolve().parent
g=json.loads((root/'geographies.json').read_text());a=json.loads((root/'osm-anchors.json').read_text())['anchors']
fig,axes=plt.subplots(1,2,figsize=(13,6.4));fig.patch.set_facecolor('#faf9f6')
for ax,city,epsg,title in zip(axes,['granada','ames'],[32611,32615],['Granada Hills, Los Angeles','Old Town vicinity, Ames']):
 t=Transformer.from_crs(4326,epsg,always_xy=True)
 anchor=a[city];x0,y0=t.transform(anchor['longitude'],anchor['latitude'])
 def coords(ring):
  x,y=t.transform(*zip(*ring));return [((p-x0)/1000,(q-y0)/1000) for p,q in zip(x,y)]
 for f in g[city]['tract-shape']['features']:
  for ring in f['geometry']['rings']:ax.add_patch(Polygon(coords(ring),fc='#e7ebee',ec='#697781',lw=1.5))
 for f in g[city]['bg-shape']['features']:
  for ring in f['geometry']['rings']:ax.add_patch(Polygon(coords(ring),fc='#69b9c4',alpha=.52,ec='#067180',lw=2))
 for f in g[city]['epa_features']:
  for ring in f['geometry']['rings']:ax.add_patch(Polygon(coords(ring),fill=False,ec='#bc6235',lw=1.6,ls='--'))
 ax.plot(0,0,'o',color='#1f2830',ms=7,zorder=5)
 ax.annotate(anchor['name'].replace(' & ',' &\n'),(0,0),xytext=(8,14) if city=='ames' else (8,-33),textcoords='offset points',fontsize=9,bbox=dict(fc='white',ec='none',alpha=.85),zorder=6)
 lib=g[city]['library-geocode']['result']['addressMatches'][0]['coordinates'];x,y=t.transform(lib['x'],lib['y']);lx,ly=(x-x0)/1000,(y-y0)/1000
 ax.plot(lx,ly,'s',color='#7e4787',ms=7,zorder=5)
 ax.annotate('Public library\n(address estimate)',(lx,ly),xytext=(8,-28) if city=='ames' else (-8,-35),ha='left' if city=='ames' else 'right',textcoords='offset points',fontsize=9,zorder=6)
 ax.autoscale_view();ax.margins(.13);ax.set_aspect('equal');ax.set_facecolor('#faf9f6');ax.grid(alpha=.13);ax.set_title(title,loc='left',fontsize=15,fontweight='bold',pad=14)
 ax.set_xlabel('Kilometers east / west of starting point');ax.set_ylabel('Kilometers north / south')
 for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle('Which area do the numbers describe?',x=.06,y=.98,ha='left',fontsize=20,fontweight='bold')
fig.text(.06,.915,'These are statistical boundaries, not neighborhood outlines. Each panel has its own scale.',fontsize=11,color='#47535b')
handles=[Patch(fc='#e7ebee',ec='#697781',label='ACS 2024 tract: main housing figures'),Patch(fc='#69b9c4',alpha=.6,label='ACS 2024 block group: smaller-area check'),Line2D([0],[0],color='#bc6235',ls='--',label='EPA 2021 release: older block groups')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.074),ncol=3,frameon=False,fontsize=9)
fig.text(.06,.034,'Sources: U.S. Census Bureau; U.S. EPA. Intersection locations: © OpenStreetMap contributors (ODbL).',fontsize=9,color='#47535b')
fig.text(.06,.010,'Retrieved 27 Sep 2026 • openstreetmap.org/copyright • Granada EPA point query was empty; nearby polygons are shown.',fontsize=9,color='#47535b')
fig.subplots_adjust(top=.83,bottom=.22,wspace=.28,left=.07,right=.97)
out=root.parents[1]/'assets'/'worked-area-geographies.png';fig.savefig(out,dpi=160,facecolor=fig.get_facecolor())
print(out)
for city in ['granada','ames']:
 p=a[city];q=g[city]['library-geocode']['result']['addressMatches'][0]['coordinates']
 phi1,phi2=map(math.radians,[p['latitude'],q['y']]);dp=phi2-phi1;dl=math.radians(q['x']-p['longitude'])
 distance=6371.0088*2*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(phi1)*math.cos(phi2)*math.sin(dl/2)**2))
 print(city,'library km',distance)
