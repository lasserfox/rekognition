import requests

import requests,time,os.path
from PIL import Image
from io import BytesIO
url = 'https://www.forofosdelrunning.com/fotosdecarreraspopulares/wp-content/gallery/fotos-carrera-popular-villa-de-aranjuez-2018/Fotos-Carrera-Popular-Villa-de-Aranjuez-2018_0005.jpg' #840
url = 'http://www.forofosdelrunning.com/index.php?action=media;sa=media;in=114286' # 2 de 3
#url = 'http://www.forofosdelrunning.com/index.php?action=media;sa=media;in=109415' # Richard & Ivan


dataCarreras = {'aranjuez2018':{'url':'https://www.forofosdelrunning.com/fotosdecarreraspopulares/wp-content/gallery/fotos-carrera-popular-villa-de-aranjuez-2018/','filename':'Fotos-Carrera-Popular-Villa-de-Aranjuez-2018_XXXX.jpg','from':5,'to':840},
                'getafe2019':{'url':'https://www.forofosdelrunning.com/fotosdecarreraspopulares/wp-content/gallery/fotos-media-maraton-de-getafe-2019/','filename':'Media-maraton-de-Getafe-2019_XXXX.jpg','from':1,'to':504},
                }


for carrera in dataCarreras:
    _from = dataCarreras[carrera]['from']
    _to = dataCarreras[carrera]['to']
    for i in range(_from,_to):
        url = dataCarreras[carrera]['url'] + dataCarreras[carrera]['filename'].replace("XXXX",(f"{i:04d}"))
        print (url)
        filename = '/Users/Lasser/Downloads/borrar/'+carrera+'/'+dataCarreras[carrera]['filename'].replace("XXXX",(f"{i:04d}"))
        if not os.path.isfile(filename):
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save(filename)
            time.sleep(300)


