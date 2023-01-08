from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from poll.serializers import SurveyCategoryCreateSerializer
from utilities.models import Lga, State
from utilities.serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def seed_states(request):

    if request.method == 'POST':
        data =  [(1,'Abia'),(2,'Adamawa'),(3,'Akwa Ibom'),(4,'Anambra'),(5,'Bauchi'),(6,'Bayelsa'),(7,'Benue'),(8,'Borno'),(9,'Cross river'),(10,'Delta'),(11,'Ebonyi'),(12,'Edo'),(13,'Ekiti'),(14,'Enugu'),(15,'Fct'),(16,'Gombe'),(17,'Imo'),(18,'Jigawa'),(19,'Kaduna'),(20,'Kano'),(21,'Katsina'),(22,'Kebbi'),(23,'Kogi'),(24,'Kwara'),(25,'Lagos'),(26,'Nasarawa'),(27,'Niger'),(28,'Ogun'),(29,'Ondo'),(30,'Osun'),(31,'Oyo'),(32,'Plateau'),(33,'Rivers'),(34,'Sokoto'),(35,'Taraba'),(36,'Yobe'),(37,'Zamfara')]
        for i in data:
            json_data = {"name" : i[1]}
            serialized_data = StateSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)


@api_view(['POST'])
def seed_lga(request):
        if request.method == 'POST': 
            data = (3,'Aba north',1,1),(3,'Aba south',1,1),(2,'Arochukwu',1, 2),(2,'Bende',1),(1,'Ikwuano',1),(1,'Isiala ngwa north',1),(1,'Isiala ngwa south',1),(2,'Isuikwuato',1),(3,'Obingwa',1),(2,'Ohafia',1,2),(3,'Osisioma',1),(3,'Ugwunagbo',1),(3,'Ukwa  west',1),(3,'Ukwa east',1),(2,'Umu - nneochi',1),(1,'Umuahia  south',1),(1,'Umuahia north',1),(6,'Demsa',2),(4,'Fufore',2),(6,'Ganye',2),(4,'Gire 1',2),(22,'Gombi',2),(6,'Guyuk',2),(4,'Hong',2),(6,'Jada',2),(6,'Lamurde',2),(5,'Madagali',2),(5,'Maiha',2),(6,'Mayo - belwa',2),(5,'Michika',2),(5,'Mubi north',2),(5,'Mubi south',2),(6,'Numan',2),(6,'Shelleng',2),(4,'Song',2),(6,'Toungo',2),(4,'Yola north',2),(4,'Yola south',2),(8,'Abak',3),(9,'Eastern obolo',3),(9,'Eket',3),(9,'Esit eket (uquo)',3),(8,'Essien udim',3),(8,'Etim ekpo',3),(7,'Etinan',3),(9,'Ibeno',3),(7,'Ibesikpo asutan',3),(7,'Ibiono ibom',3),(8,'Ika',3),(8,'Ikono',3),(9,'Ikot abasi',3),(8,'Ikot ekpene',3),(8,'Ini',3),(7,'Itu',3),(9,'Mbo',3),(9,'Mkpat enin',3),(7,'Nsit atai',3),(7,'Nsit ibom',3),(59,'Nsit ubium',3),(8,'Obot akara',3),(9,'Okobo',3),(9,'Onna',3),(9,'Oron',3),(8,'Oruk anam',3),(9,'Udung uko',3),(8,'Ukanafun',3),(7,'Uruan',3),(9,'Urue offong oruko',3),(7,'Uyo',3),(12,'Aguata',4),(11,'Anambra east',4),(11,'Anambra west',4),(10,'Anaocha',4),(10,'Awka north',4),(10,'Awka south',4),(11,'Ayamelum',4),(10,'Dunukofia',4),(12,'Ekwusigo',4),(10,'Idemili north',4),(10,'Idemili-south',4),(12,'Ihala',4),(10,'Njikoka',4),(12,'Nnewi north',4),(12,'Nnewi south',4),(11,'Ogbaru',4),(11,'Onitsha -south',4),(11,'Onitsha-north',4),(12,'Orumba  south',4),(12,'Orumba north',4),(11,'Oyi',4),(15,'Alkaleri',5),(15,'Bauchi',5),(15,'Bogoro',5),(94,'Dambam',13),(95,'Darazo',13),(15,'Dass',5),(14,'Gamawa',5),(13,'Ganjuwa',5),(14,'Giade',5),(14,'Itas/gadau',5),(14,'Jama\'are',5),(14,'Katagum',5),(15,'Kirfi',5),(13,'Misau',5),(13,'Ningi',5),(14,'Shira',5),(15,'Tafawa balewa',5),(15,'Toro',5),(13,'Warji',5),(14,'Zaki',5),(17,'Brass',6),(18,'Ekeremor',6),(16,'Kolokuma/opokuma',6),(17,'Nembe',6),(17,'Ogbia',6),(18,'Sagbama',6),(16,'Southern ijaw',6),(16,'Yenagoa',6),(21,'Ado',7),(21,'Agatu',7),(21,'Apa',7),(20,'Buruku',7),(20,'Gboko',7),(20,'Guma',7),(20,'Gwer east',7),(20,'Gwer west',7),(19,'Katsina-ala',7),(19,'Konshisha',7),(19,'Kwande',7),(19,'Logo',7),(20,'Makurdi',7),(21,'Obi',7),(21,'Ogbadibo',7),(21,'Ohimini',7),(21,'Oju',7),(21,'Okpokwu',7),(21,'Otukpo',7),(20,'Tarka',7),(19,'Ukum',7),(19,'Ushongo',7),(19,'Vandeikya',7),(23,'Abadam',8),(24,'Askira / uba',8),(22,'Bama',8),(24,'Bayo',8),(24,'Biu',8),(24,'Chibok',8),(24,'Damboa',8),(22,'Dikwa',8),(23,'Gubio',8),(23,'Guzamala',8),(24,'Gwoza',8),(24,'Hawul',8),(22,'Jere',8),(22,'Kaga',8),(22,'Kala balge',8),(22,'Konduga',8),(23,'Kukawa',8),(24,'Kwaya / kusar',8),(22,'Mafa',8),(23,'Magumeri',8),(22,'Maiduguri m. c.',8),(163,'Marte',8),(23,'Mobbar',8),(23,'Monguno',8),(22,'Ngala',8),(23,'Nganzai',8),(24,'Shani',8),(25,'Abi',9),(27,'Akamkpa',9),(27,'Akpabuyo',9),(27,'Bakassi',9),(26,'Bekwarra',9),(26,'Biase',9),(25,'Boki',9),(27,'Calabar municipality',9),(27,'Calabar south',9),(25,'Etung',9),(25,'Ikom',9),(26,'Obanliku',9),(25,'Obubra',9),(26,'Obudu',9),(27,'Odukpani',9),(26,'Ogoja',9),(25,'Yakurr',9),(26,'Yala',9),(29,'Aniocha - south',10),(29,'Aniocha north',10),(30,'Bomadi',10),(30,'Burutu',10),(28,'Ethiope  east',10),(28,'Ethiope  west',10),(29,'Ika - south',10),(29,'Ika north- east',10),(30,'Isoko north',10),(30,'Isoko south',10),(29,'Ndokwa east',10),(29,'Ndokwa west',10),(28,'Okpe',10),(29,'Oshimili - north',10),(29,'Oshimili - south',10),(30,'Patani',10),(28,'Sapele',10),(28,'Udu',10),(28,'Ughelli north',10),(28,'Ughelli south',10),(29,'Ukwuani',10),(28,'Uvwie',10),(30,'Warri  north',10),(30,'Warri south',10),(30,'Warri south  west',10),(33,'Abakaliki',11),(31,'Afikpo  south',11),(31,'Afikpo north',11),(33,'Ebonyi',11),(32,'Ezza north',11),(32,'Ezza south',11),(32,'Ikwo',11),(32,'Ishielu',11),(31,'Ivo',11),(33,'Izzi',11),(31,'Ohaozara',11),(33,'Ohaukwu',11),(31,'Onicha',11),(36,'Akoko edo',12),(34,'Egor',12),(35,'Esan central',12),(35,'Esan north east',12),(35,'Esan south east',12),(35,'Esan west',12),(36,'Etsako  west',12),(36,'Etsako central',12),(36,'Etsako east',12),(35,'Igueben',12),(34,'Ikpoba/okha',12),(34,'Oredo',12),(34,'Orhionmwon',12),(34,'Ovia north east',12),(34,'Ovia south west',12),(36,'Owan east',12),(36,'Owan west',12),(34,'Uhunmwode',12),(38,'Ado ekiti',13),(38,'Efon',13),(37,'Ekiti east',13),(37,'Ekiti south west',13),(38,'Ekiti west',13),(37,'Emure',13),(37,'Gbonyin',13),(39,'Ido / osi',13),(38,'Ijero',13),(37,'Ikere',13),(39,'Ikole',13),(39,'Ilejemeje',13),(38,'Irepodun / ifelodun',13),(37,'Ise / orun',13),(39,'Moba',13),(39,'Oye',13),(42,'Aninri',14),(42,'Awgu',14),(41,'Enugu east',14),(41,'Enugu north',14),(41,'Enugu south',14),(42,'Ezeagu',14),(40,'Igbo etiti',14),(40,'Igbo eze north',14),(40,'Igbo eze south',14),(41,'Isi uzo',14),(41,'Nkanu east',14),(41,'Nkanu west',14),(40,'Nsukka',14),(42,'Oji-river',14),(40,'Udenu',14),(42,'Udi',14),(40,'Uzo-uwani',14),(43,'Abaji',15),(43,'Bwari',15),(43,'Gwagwalada',15),(43,'Kuje',15),(43,'Kwali',15),(43,'Municipal',15),(44,'Akko',16),(46,'Balanga',16),(46,'Billiri',16),(45,'Dukku',16),(45,'Funakaye',16),(45,'Gombe',16),(46,'Kaltungo',16),(45,'Kwami',16),(45,'Nafada',16),(46,'Shongom',16),(44,'Yalmaltu/ deba',16),(47,'Aboh mbaise',17),(47,'Ahiazu mbaise',17),(48,'Ehime mbano',17),(47,'Ezinihitte mbaise',17),(49,'Ideato north',17),(49,'Ideato south',17),(48,'Ihitte/uboma (isinweke)',17),(47,'Ikeduru (iho)',17),(48,'Isiala mbano (umuelemai)',17),(49,'Isu (umundugba)',17),(47,'Mbaitoli (nwaorieubi)',17),(47,'Ngor okpala (umuneke)',17),(49,'Njaba (nnenasa)',17),(49,'Nkwerre',17),(49,'Nwangele (onu-nwangele amaigbo)',17),(48,'Obowo (otoko)',17),(49,'Oguta (oguta)',17),(49,'Ohaji/egbema (mmahu-egbema)',17),(48,'Okigwe(okigwe)',17),(48,'Onuimo (okwe)',17),(49,'Orlu',17),(49,'Orsu (awo idemili)',17),(49,'Oru west (mgbidi)',17),(49,'Oru-east',17),(47,'Owerri north (orie uratta)',17),(47,'Owerri urban',17),(47,'Owerri west (umuguma)',17),(51,'Auyo',18),(50,'Babura',18),(52,'Birnin kudu',18),(51,'Birniwa',18),(52,'Buji',18),(52,'Dutse',18),(50,'Gagarawa',18),(50,'Garki',18),(50,'Gumel',18),(51,'Guri',18),(52,'Gwaram',18),(50,'Gwiwa',18),(51,'Hadejia',18),(52,'Jahun',18),(51,'Kafin hausa',18),(51,'Kaugama',18),(50,'Kazaure',18),(51,'Kirika samma',18),(52,'Kiyawa',18),(50,'Maigatari',18),(51,'Malam madori',18),(52,'Miga',18),(50,'Ringim',18),(50,'Roni',18),(50,'Sule-tankarkar',18),(50,'Taura',18),(50,'Yankwashi',18),(53,'Birnin gwari',19),(53,'Chikun',19),(53,'Giwa',19),(53,'Igabi',19),(54,'Ikara',19),(55,'Jaba',19),(55,'Jema\'a',19),(55,'Kachia',19),(53,'Kaduna north',19),(53,'Kaduna south',19),(55,'Kagarko',19),(53,'Kajuru',19),(55,'Kaura',19),(55,'Kauru',19),(54,'Kubau',19),(54,'Kudan',19),(54,'Lere',19),(54,'Makarfi',19),(54,'Sabon gari',19),(55,'Sanga',19),(54,'Soba',19),(55,'Zangon kataf',19),(54,'Zaria',19),(56,'Ajingi',20),(56,'Albasu',20),(58,'Bagwai',20),(56,'Bebeji',20),(58,'Bichi',20),(56,'Bunkure',20),(57,'Dala',20),(58,'Danbata',20),(57,'Dawaki kudu',20),(58,'Dawaki tofa',20),(56,'Doguwa',20),(57,'Fagge',20),(58,'Gabasawa',20),(56,'Garko',20),(57,'Garun malam',20),(56,'Gaya',20),(57,'Gezawa',20),(57,'Gwale',20),(58,'Gwarzo',20),(58,'Kabo',20),(57,'Kano municipal',20),(58,'Karaye',20),(56,'Kibiya',20),(56,'Kiru',20),(57,'Kumbotso',20),(58,'Kunchi',20),(57,'Kura',20),(57,'Madobi',20),(58,'Makoda',20),(57,'Minjibir',20),(57,'Nasarawa',20),(56,'Rano',20),(58,'Rimin gado',20),(56,'Rogo',20),(58,'Shanono',20),(56,'Sumaila',20),(56,'Takai',20),(57,'Tarauni',20),(58,'Tofa',20),(58,'Tsanyawa',20),(56,'Tudun wada',20),(57,'Ungogo',20),(57,'Warawa',20),(56,'Wudil',20),(61,'Bakori',21),(59,'Batagarawa',21),(59,'Batsari',21),(60,'Baure',21),(60,'Bindawa',21),(59,'Charanchi',21),(59,'Dan musa',21),(61,'Dandume',21),(61,'Danja',21),(60,'Daura',21),(60,'Dutsi',21),(59,'Dutsin-ma',21),(61,'Faskari',21),(61,'Funtua',21),(60,'Ingawa',21),(59,'Jibia',21),(61,'Kafur',21),(59,'Kaita',21),(61,'Kankara',21),(60,'Kankia',21),(59,'Katsina',21),(59,'Kurfi',21),(60,'Kusada',21),(60,'Mai\'adua',21),(61,'Malufashi',21),(60,'Mani',21),(60,'Mashi',21),(61,'Matazu',21),(61,'Musawa',21),(59,'Rimi',21),(61,'Sabuwa',21),(59,'Safana',21),(60,'Sandamu',21),(60,'Zango',21),(62,'Aliero',22),(63,'Arewa',22),(63,'Argungu',22),(63,'Augie',22),(63,'Bagudo',22),(62,'Birnin kebbi',22),(62,'Bunza',22),(63,'Dandi',22),(64,'Fakai',22),(62,'Gwandu',22),(63,'Jega',22),(62,'Kalgo',22),(62,'Koko/besse',22),(62,'Maiyama',22),(64,'Ngaski',22),(64,'Sakaba',22),(64,'Shanga',22),(63,'Suru',22),(64,'Wasagu/danko',22),(64,'Yauri',22),(64,'Zuru',22),(65,'Adavi',23),(65,'Ajaokuta',23),(66,'Ankpa',23),(66,'Bassa',23),(66,'Dekina',23),(66,'Ibaji',23),(66,'Idah',23),(66,'Igalamela/odolu',23),(67,'Ijumu',23),(67,'Kabba/bunu',23),(479,'Kogi . k. k.',23),(67,'Lokoja',23),(67,'Mopa moro',23),(66,'Ofu',23),(65,'Ogori mangogo',23),(65,'Okehi',23),(65,'Okene',23),(66,'Olamaboro',23),(66,'Omala',23),(67,'Yagba east',23),(67,'Yagba west',23),(68,'Asa',24),(69,'Baruten',24),(69,'Edu',24),(70,'Ekiti',24),(70,'Ifelodun',24),(68,'Ilorin east',24),(68,'Ilorin-south',24),(68,'Ilorin-west',24),(70,'Irepodun',24),(70,'Isin',24),(69,'Kaiama',24),(69,'Moro',24),(68,'Offa',24),(70,'Oke - ero',24),(70,'Oyun',24),(69,'Patigi',24),(71,'Agege',25),(71,'Ajeromi/ifelodun',25),(71,'Alimosho',25),(71,'Amuwo-odofin',25),(72,'Apapa',25),(71,'Badagry',25),(73,'Epe',25),(72,'Eti-osa',25),(73,'Ibeju/lekki',25),(71,'Ifako-ijaye',25),(71,'Ikeja',25),(73,'Ikorodu',25),(73,'Kosofe',25),(72,'Lagos island',25),(72,'Lagos mainland',25),(71,'Mushin',25),(71,'Ojo',25),(71,'Oshodi/isolo',25),(73,'Somolu',25),(72,'Surulere',25),(75,'Akwanga',26),(74,'Awe',26),(74,'Doma',26),(76,'Karu',26),(74,'Keana',26),(76,'Keffi',26),(76,'Kokona',26),(74,'Lafia',26),(76,'Nasarawa',26),(75,'Nasarawa eggon',26),(74,'Obi',26),(76,'Toto',26),(75,'Wamba',26),(79,'Agaie',27),(78,'Agwara',27),(79,'Bida',27),(78,'Borgu',27),(77,'Bosso',27),(77,'Chanchaga',27),(79,'Edatti',27),(79,'Gbako',27),(77,'Gurara',27),(79,'Katcha',27),(78,'Kontagora',27),(79,'Lapai',27),(79,'Lavun',27),(78,'Magama',27),(78,'Mariga',27),(78,'Mashegu',27),(79,'Mokwa',27),(77,'Munya',27),(77,'Paikoro',27),(77,'Rafi',27),(78,'Rijau',27),(77,'Shiroro',27),(77,'Suleja',27),(77,'Tafa',27),(78,'Wushishi',27),(80,'Abeokuta north',28),(80,'Abeokuta south',28),(82,'Ado odo-ota',28),(82,'Egbado north',28),(82,'Egbado south',28),(80,'Ewekoro',28),(80,'Ifo',28),(81,'Ijebu east',28),(81,'Ijebu north',28),(81,'Ijebu north east',28),(81,'Ijebu ode',28),(81,'Ikenne',28),(82,'Imeko/afon',28),(82,'Ipokia',28),(80,'Obafemi/owode',28),(80,'Odeda',28),(81,'Odogbolu',28),(81,'Ogun water side',28),(81,'Remo north',28),(81,'Sagamu',28),(84,'Akoko north east',29),(84,'Akoko north west',29),(84,'Akoko south east',29),(84,'Akoko south west',29),(83,'Akure north',29),(83,'Akure south',29),(85,'Ese-odo',29),(83,'Idanre',29),(83,'Ifedore',29),(85,'Ilaje',29),(85,'Ileoluji/okeigbo',29),(85,'Irele',29),(85,'Odigbo',29),(85,'Okitipupa',29),(83,'Ondo east',29),(83,'Ondo west',29),(84,'Ose',29),(84,'Owo',29),(87,'Atakumosa east',30),(87,'Atakumosa west',30),(88,'Ayedaade',30),(88,'Ayedire',30),(86,'Boluwaduro',30),(86,'Boripe',30),(88,'Ede north',30),(88,'Ede south',30),(88,'Egbedore',30),(88,'Ejigbo',30),(87,'Ife central',30),(87,'Ife east',30),(87,'Ife north',30),(87,'Ife south',30),(86,'Ifedayo',30),(86,'Ifelodun',30),(86,'Ila',30),(87,'Ilesa east',30),(87,'Ilesa west',30),(86,'Irepodun',30),(88,'Irewole',30),(88,'Isokan',30),(88,'Iwo',30),(87,'Obokun',30),(86,'Odo-otin',30),(88,'Ola-oluwa',30),(86,'Olorunda',30),(87,'Oriade',30),(86,'Orolu',30),(86,'Osogbo',30),(89,'Afijio',31),(89,'Akinyele',31),(89,'Atiba',31),(90,'Atisbo',31),(89,'Egbeda',31),(91,'Ibadan north',31),(91,'Ibadan north east',31),(91,'Ibadan north west',31),(91,'Ibadan south west',31),(91,'Ibadan south-east',31),(91,'Ibarapa central',31),(91,'Ibarapa east',31),(91,'Ibarapa north',31),(91,'Ido',31),(90,'Irepo',31),(90,'Iseyin',31),(90,'Itesiwaju',31),(90,'Iwajowa',31),(90,'Kajola',31),(89,'Lagelu',31),(90,'Ogbomoso north',31),(90,'Ogbomoso south',31),(89,'Ogo-oluwa',31),(90,'Olorunsogo',31),(89,'Oluyole',31),(89,'Ona-ara',31),(90,'Oorelope',31),(90,'Ori ire',31),(89,'Oyo east',31),(89,'Oyo west',31),(90,'Saki east',31),(90,'Saki west',31),(89,'Surulere',31),(93,'Barikin ladi',32),(93,'Bassa',32),(92,'Bokkos',32),(93,'Jos east',32),(93,'Jos north',32),(93,'Jos south',32),(92,'Kanam',32),(92,'Kanke',32),(94,'Langtang north',32),(94,'Langtang south',32),(92,'Mangu',32),(94,'Mikang',32),(92,'Pankshin',32),(94,'Qua\'an pan',32),(93,'Riyom',32),(94,'Shendam',32),(94,'Wase',32),(97,'Abua-odual',33),(97,'Ahoada east',33),(97,'Ahoada west',33),(97,'Akuku toru',33),(96,'Andoni',33),(97,'Asari-toru',33),(97,'Bonny',33),(97,'Degema',33),(96,'Eleme',33),(95,'Emohua',33),(95,'Etche',33),(96,'Gokana',33),(95,'Ikwerre',33),(96,'Khana',33),(95,'Obio/akpor',33),(97,'Ogba/egbema/ndoni',33),(95,'Ogu/bolo',33),(95,'Okrika',33),(95,'Omuma',33),(96,'Opobo/nekoro',33),(96,'Oyigbo',33),(95,'Port harcourt',33),(96,'Tai',33),(99,'Binji',34),(100,'Bodinga',34),(100,'Dange/shuni',34),(98,'Gada',34),(98,'Goronyo',34),(99,'Gudu',34),(98,'Gwadabawa',34),(98,'Illela',34),(98,'Isa',34),(100,'Kebbe',34),(99,'Kware',34),(98,'Rabah',34),(98,'S/birni',34),(100,'Shagari',34),(99,'Silame',34),(99,'Sokoto north',34),(99,'Sokoto south',34),(100,'Tambuwal',34),(99,'Tangaza',34),(100,'Tureta',34),(99,'Wamakko',34),(98,'Wurno',34),(100,'Yabo',34),(102,'Ardo - kola',35),(101,'Bali',35),(103,'Donga',35),(101,'Gashaka',35),(101,'Gassol',35),(103,'Ibi',35),(102,'Jalingo',35),(102,'Karim-lamido',35),(101,'Kurmi',35),(102,'Lau',35),(101,'Sardauna',35),(103,'Takum',35),(103,'Ussa',35),(103,'Wukari',35),(102,'Yorro',35),(102,'Zing',35),(105,'Bade',36),(104,'Bursari',36),(106,'Damaturu',36),(106,'Fika',36),(106,'Fune',36),(104,'Geidam',36),(104,'Gujba',36),(104,'Gulani',36),(105,'Jakusko',36),(105,'Karasawa',36),(105,'Machina',36),(106,'Nangere',36),(105,'Nguru',36),(106,'Potiskum',36),(104,'Tarmuwa',36),(104,'Yunusari',36),(105,'Yusufari',36),(109,'Anka',37),(109,'Bakura',37),(108,'Birnin magaji',37),(109,'Bukkuyum',37),(107,'Bungudu',37),(109,'Gummi',37),(107,'Gusau',37),(108,'Kaura namoda',37),(109,'Maradun',37),(107,'Maru',37),(108,'Shinkafi',37),(108,'Talata mafara',37),(107,'Tsafe',37),(108,'Zurmi',37)
            for i in data:
                json_data = {"name" : i[1], "state_id" : i[2], "senatorial_id" : i[0], "constituency_id" : i[3]}
                serialized_data = LgaSerializer(data=json_data)
                if serialized_data.is_valid():
                    serialized_data.save()
            return Response(serialized_data.data)



@api_view(['POST'])
def seed_senatorial(request):

    if request.method == 'POST':
        data = [('Abia Central',1),('Abia North',1),('Abia South',1),('Adamawa Central',2),('Adamawa North',2),('Adamawa South',2),('Akwa Ibom North East',3),('Akwa Ibom North West',3),('Akwa Ibom South',3),('Anambra Central',4),('Anambra North',4),('Anambra South',4),('Bauchi Central',5),('Bauchi North',5),('Bauchi South',5),('Bayelsa Central',6),('Bayelsa East',6),('Bayelsa West',6),('Benue North East',7),('Benue North West',7),('Benue South',7),('Borno Central',8),('Borno North',8),('Borno South',8),('Cross River Central',9),('Cross River North',9),('Cross River South',9),('Delta Central',10),('Delta North',10),('Delta South',10),('Ebonyi South',11),('Ebonyi Central',11),('Ebonyi North',11),('Edo South',12),('Edo Central',12),('Edo North',12),('Ekiti South',13),('Ekiti Central',13),('Ekiti North',13),('Enugu North',14),('Enugu East',14),('Enugu West',14),('Federal Capital Territory',15),('Gombe Central',16),('Gombe North',16),('Gombe South',16),('Imo East',17),('Imo North',17),('Imo West',17),('Jigawa North - West',18),('Jigawa North - East',18),('Jigawa South - West',18),('Kaduna Central',19),('Kaduna North',19),('Kaduna South',19),('Kano South',20),('Kano Central',20),('Kano North',20),("Katsina Central",21),('Katsina North',21),('Katsina South',21),('Kebbi Central',22),('Kebbi North',22),('Kebbi South',22),('Kogi Central',23),('Kogi East',23),('Kogi West',23),('Kwara Central',24),('Kwara North',24),('Kwara South',24),('Lagos West',25),('Lagos Central',25),('Lagos East',25),('Nasarawa South',26),('Nasarawa North',26),('Nasarawa West',26),('Niger East',27),('Niger North',27),('Niger South',27),('Ogun Central',28),('Ogun East',28),('Ogun West',28),('Ondo Central',29),('Ondo North',29),('Ondo South',29),('Osun Central',30),('Osun East',30),('Osun West',30),("Oyo Central",31),('Oyo North',31),('Oyo South',31),('Plateau Central',32),('Plateau North',32),('Plateau South',32),('Rivers East',33),('Rivers South East',33),('Rivers West',33),('Sokoto East',34),('Sokoto North',34),('Sokoto South',34),('Taraba Central',35),('Taraba North',35),('Taraba South',35),('Yobe East',36),('Yobe North',36),('Yobe South',36),('Zamfara Central',37),('Zamfara North',37),('Zamfara West',37)]
        for i in data:
            json_data = {"name" : i[0], "state_id" : i[1]}
            serialized_data = SenatorialSerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)

@api_view(['POST'])
def seed_constituencies(request):

    if request.method == 'POST':
        data = [('Aba N/S',1),('Arochukwu/Ohafia',1),('Bende',1),('Nsiala Ngwa N/S',1),('Isuikwuato/Umu-Nneochi',1),('Obingwa/Ugwunagbo/Osisioma',1),('Umuahia(N/S)/Ikwuano',1),('Ukwa E/W',1),('Demsa/Numan/Lamurde',2),('Furore/Song',2),('Mayo Belwa/Ganye/Jada/Toungo',2),('Gombi/Hong',2),('Guyuk/Shelleng',2),('Madagali/Michika',2),('Maiha/Mubi(N/S)',2),('Yola(N/S)/Girei',2),('Anambra(E/W)',3),('Onitcha(N/S)',3),('Ogbaru',3),('Aguata',3),('Oyi/Ayamelum',3),('Awka(N/S)',3),('Nijikoka/Dunukofia/Anaocha',3),('Idemili(N/S)',3),('Ihiala',3),('Nnewi(N/S)/Ekwusigo',3),('Orumba(N/S)',3),('Abak/Etim Ekpo/Ika',4),('Eket/Onna/Esit Eket/Ibeno',4),('Etinan/Nsit Ibom/Nsit Ubium',4),('Ikono/Ini',4),('Ikot Absai/Mkpat Enin/Eastern Obolo',4),('Ikot Ekpene/Essien Udim/Obot Akara',4),('Itu/Ibiono Ibom',4),('Oron/Mbo/Okobo/Udung Uko/Urue Offong/Uruko',4),('Ukanafun/Oruk Anam',4),('Uyo/Uruan/Nsit Atai/Ibesikpo Asutan',4),('Alkaleri/Kirfi',5),('Bauchi',5),('Bogoro/Dass/Tafawa Balewa',5),('Toro',5),('Ningi/Warji',5),('Darazo/Gunjuwa',5),('Misau/Dambam',5),('Zaki',5),('Gamawa',5),('Jamaare/Itas-Gadau',5),('Shira/Giade',5),('Katagum',5),('Brass/Nembe',6),('Ogbia',6),('Sagbama/Ekeremor)',6),('Southern Ijaw',6),('Yenagoa/Kolokuna/Opokuma',6),('Ado/Obadigbo/Okpokwu',7),('Apa/Agatu',7),('Buruku',7),('Gboko/Tarka',7),('Guma/Makurdi',7),('Gwer East/West',7),('Konshisha/Vandeikya',7),('Kwande/Ushongo',7),('Oju/Obi',7),('Otukpo/Ohimini',7),('Askira-Uba/Hawul',8),('Bama/Ngala/Kala-Balge',8),('Biu/Kwaya-Kusar, Shani/Bayo',8),('Dikwa/Mafa/Konduga',8),('Damboa/Gwoza/Chibok',8),('Kaga/Gubio/Magumeri',8),('Monguno/Nganzai/Marte',8),('Kukawa/Mobbar/Abadam/ Guzamali',8),('Maiduguri (Metropolitan)',8),('Jere',8),
        ('Yakurr/Abi',9),('Akamkpa/Biase',9),('Boki/Ikom',9),('Calabar South/Akpabuyo/Bakassi',9),('Calabar Municipal/Odukpani',9),('Obanliku/Obudu/Bekwarra',9),('Obubra/Etung',9),('Ogoja/Yala',9),('Aniocha(N/S)/Oshimili(N/S)',10),('Bomadi/Patani',10),('Ethiope East/Ethiope West',10),('Ika North East/Ika South',10),('Isoko(N/S)',10),('Nkokwa(E&S)/Ukwuani',10),('Okpe/Sapele/Uvwie)',10),('Burutu',10),('Ughelli(N/S)/Udu',10),('Warri(N/S/SE)',10),('Ebonyi/Ohaukwu',11),('Abakaliki/Izzi',11),('Ezza North/Ishielu',11),('Ezza South/Ikwo',11),('Ivo-Ohaozara/Onicha',11),('Afikpo(N/S)',11),('Akoko-Edo',12),('Esan Central/Esan South/Igueben',12),('Esan North East/Esan South East',12),('Etsako (E/W/C) ',12),('Egor/Ikpoba-Okha',12),('Oredo',12),('Orhionmwon/Uhunmwonde',12),('Ovia(NE/SW)',12),('Owan(E/W)',12),('Ado Ekiti/Irepodun/Ifelodun',13),('Ekiti South West/Ikere/Orun/Ise',13),('Emure/Gbonyin/Ekiti East',13),('Ido/Osi, Moba/Ilejeme',13),('Ijero/Ekiti West/Efon',13),('Ikole/Oye',13),('Aninri/Awgu/Oji River',14),('IEnugu East/Isi Uzo',14),
        ('Enugu(N/S)',14),('Ezeagu/Udi',14),('Igbo-Etiti/Uzo-Uwani',14),('Igbo-Eze North/Udenu',14),
        ('Nkanu East/Nkanu West',14),('Nsukka/Igbo-Eze South',14),('Akko',15),('Yamaltu/Deba',15),('Balanga/Billiri',15),('Kaltungo/Shongom',15),('Gombe/Kwami/Funakaye',15),('Dukku/Nafada',15),('Ehime Mbano/Ihite-Uboma/Obowo',16),('Isiala Mbano/Okigwe/Onuimo',16),('Ideato(N/S)',16),('Isu/Njaba/Nkwerre/Nwangele',16),('Oguta/Ohaji-Egbema/Oru West',16),('Oru East/Orsu/Orlu',16),('Aboh Mbaise/Ngor Okpala',16),('Ahiazu Mbaise/Ezinihitte',16),('Ikeduru/Mbaitoli',16),('Owerri Municipal/Owerri(N/W)',16),('Babura/Garki',17),('Birnin Kudu/Buji',17),('Birniwa Guri/Kirikasamma',17),('Dutse/Kiyawa',17),('Gwaram',17),('Gumel/Maigatari/Sule Tankarkar/Gagarawa',17),('Hadejia/Kafin Hausa',17),('Jahun/Miga',17),('Mallam Madori/Kaugama',17),('Kazaure/Roni/Gwiwa/Yankwashi',17),('Ringim/Taura',17),('Kaduna North',18),('Zaria',18),('Soba',18),('Igabi',18),('Ikara/Kubau',18),('Makarfi/Kudan',18),('Lere',18),('Kachia/Kagarko',18),('Chikun/Kajuru',18),('Jemaa/Sanga',18),('Birnin Gwari/Giwa',18),('Sabon Gari',18),('Kaduna South',18),('Kaura',18),('Kauru',18),('Zangon Kataf/Jaba',18),('Alabasu/Gaya/Ajingi',19),('Shanono/Bagwai',19),('Bebeji/Kiru',19),('Bichi',19),('Rano/Bunkure/Kibiya',19),('Dala',19),('Gwale',19),('Dambatta/Makoda',19),('Dawakin Kudu/Warawa',19),('Dawakin Tofa/Tofa/Rimin Gado',19),('Doguwa/Tudun Wada',19),('Gezawa/Gabasawa',19),('Gwarzo/Ikabo',19),('Municipal',19),('Tarauni',19),('Karaye/Rogo',19),('Kumbotso',19),('Kura/Madobi/Garun Mallam',19),('Nassarawa',19),('Fagge',19),('Sumaila/Takai',19),('Minjibir/Ungogo',19),('Tsanyawa/Kunchi',19),('Wudil/Garko',19),('Bakori/Danja',20),('Batagarawa/Charanchi/Rimi',20),('Batsari/Safana/Danmusa',20),('Bindawa/Mani',20),('Daura/Sandamu/Maiadua',20),('Dutsin-ma/Kurfi',20),('Faskari/Kankara/Sabuwa',20),('Funtua/Dandume',20),('Ingawa/Kankia/Kusada',20),('Jibia/Kaita',20),('Malumfashi/Kafur',20),('Katsina',20),('Mashi/Dutsi',20),('Matazu/Musawa',20),('Zango/Baure',20),('Arewa/Dandi',21),('Argungu/Augie',21),('Bagudo/Suru',21),('Bunza/Birnin Kebbi/Kalgo',21),('Aleiro/Gwandu/Jega',21),('Koko-Besse/Maiyama',21),('Fakai/Sakaba/Wasagu/Danko/Zuru',21),('Ngaski/Shanga/Yauri',21),('Adavi/Okehi',22),('Ankpa/Omala/Olamaboro',22),('Bassa/Dekina',22),('Idah/Igalamela Odolu/Ibaji/ Ofu',22),('Ijumu/Kabba-Bunu',22),('Ajaokuta',22),('Kogi (Lokoja)/Kogi (K.K.)',22),('Okene/Ogori-Magogo',22),('Yagba East/Yagba West/ Mopamuro',22),('Baruten/Kaiama',23),('Edu/Moro/Pategi',23),('Ekiti/Isin/Irepodun/Oke-Ero',23),('Ilorin East/Ilorin South',23),('Ilorin West/Asa',23),('Ifelodun/Offa/Oyun',23),('Agege',24),('Ifako/Ijaiye',24),('Alimosho',24),('Badagry',24),('Epe',24),('Ibeju Lekki',24),('Eti-Osa',24),('Apapa',24),('Ikeja',24),('Ikorodu',24),('Lagos Island I',24),('Lagos Island II',24),('Lagos Mainland',24),('Mushin I',24),('Mushin II',24),('Ojo',24),('Amuwo-Odofin',24),('Ajeromi/Ifelodun',24),('Oshodi/Isolo I',24),('Oshodi/Isolo II',24),('Shomolu',24),('Kosofe',24),('Surulere I',24),('Surulere II',24),('Akwanga/Nassarawa Eggon/ Wamba',25),('Awe/Doma/Keana',25),('Keffi/Karu/Kokona',25),('Lafia/Obi',25),('Nassarawa/Toto',25),('Agaie/Lapai',26),('Agwara/Borgu',26),('Bida/Gbako/Katcha',26),('Booso/Paikoro',26),('Chanchaga',26),('Gurara/Suleja/Tapa',26),('Lavun/Mokwa/Edati',26),('Magama/Rijau',26),('Kontagora/Wushishi/Mariga/ Mashegu',26),('Shiroro/Rafi/Munya',26),('Abeokuta North/ Obafemi-Owode/Odeda',27),('Abeokuta South',27),('Ado-Odo/Ota',27),('Egbado North/Imeko-Afon',27),('Egbado South/Ipokia',27),('Ifo/Ewekoro',27),('Ijebu North/Ijebu East/Ogun Waterside',27),('Ijebu Ode /Odogbolu /Ijebu North East',27),('Ikenne/Shagamu/Remo North',27),('Akoko North East/Akoko North West',28),('Akoko South East/Akoko South West',28),('Akure North/Akure South',28),('Idanre/Ifedore',28),('Ileoluji/Okeigbo/Odigbo',28),('Okitipupa/Irele',28),('Eseodo/Ilaje',28),('Ondo East/Ondo West',28),('Owo/Ose',28),('Irepodun/Olorunda/Osogbo/Orolu',29),('Odo-Otin/Ifelodun/Boripe',29),('Boluwaduro/Ifedayo/Ila',29),('Atakunmosa(E&W)/Ilesha(E&W)',29),('Obokun/Oriade',29),('Ife(C/N/S/E)',29),('Ayedire/Iwo/Ola-Oluwa',29),('Ayedaade/Irewole/Isokan',29),('Ede(N/S)/Egbedore/Ejigbo',29),('Afijio/Oyo(E/W)/Atiba',30),('Akinyele/Lagelu',30),('Egbeda/Ona-Ara',30),('Ibarapa Central/Ibarapa North',30),('Ibarapa East/Ido',30),('Saki(E/W)/Atisbo',30),('Irepo/Orelope/Olorunsogo',30),('Iseyin/Itesiwaju/Kajola/Iwajowa',30),('Ogbomoso(N/S)/Orire',30),('Ogo-Oluwa/Surulere',30),('Oluyole',30),('Ibadan NorthEast/Ibadan SouthEast',30),('Ibadan South West/Ibadan North West',30),('Ibadan North',30),('Jos North/Bassa',31),('Jos South/Jos East',31),('Barkin Ladi/Riyom',31),('Bokkos/Mangu',31),('Kanke/Pankshin/Kanam',31),('Wase',31),('Langtang North/Langtang South',31),('Mikang/Quaan/Pan/Shedam',31),('Abua-Odual/Ahaoda East',32),('Ahoada West/Ogba Egbema',32),('Degema/Bonny',32),('Akuku-Toru/Asari-Toru',32),('Okrika/Ogu-Bolo',32),('Opobo/Nkoro/Andoni',32),('Eleme/Tai/Oyigbo',32),('Khana/Gokana',32),('Ikwerre/Umohua',32),('Etche/Omuma',32),('Obio Akpor',32),('Port Harcourt I',32),('Port Harcourt II',32),('Isa/Sabon Birni',33),('Goronyo/Gada',33),('Wurno/Rabah',33),('Illela/Gwadabawa',33),('Tangaza/Gudu',33),('Binji/Silame',33),('Kware/Wamakko',33),('Sokoto North/Sokoto South',33),('Dange-Shuni/Bodinga/Tureta',33),('Yabo/Shagari',33),('Kebbe/Tambuwal',33),('Bali/Gassol',34),('Takum/Donga/Ussa',34),('Sardauna/Kurmi/Gashaka',34),('Ibi/Wukari',34),('Jalingo/Yorro/Zing',34),('Karim Lamido/Lau/Ardo-Kola',34),('Bade/Jakusko',35),('Bursari/Geidam/Yunusari',35),('Damaturu/Gujba/Gulani/ Tarmuwa',35),('Fika/Fune',35),('Machina/Nguru/Yusufari/ Karasuwa',35),('Nangere/Potiskm',35),('Kaura-Namoda/Birnin Magaji',36),('Shinkafi/Zurmi',36),('Gusau/Tsafe',36),('Bungudu/Maru',36),('Anka/Talata Mafara',36),('Bakura/Maradun',36),('Gummi/Bukkuyum',36),('Abaji/Gwagwalada/Kwali/Kuje',37),('Municipal/Bwari',37)
        ]
        for i in data:
            json_data = {"name" : i[0], "state_id" : i[1]}
            serialized_data = ConstituencySerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)
 
@api_view(['DELETE'])
def clearStates(request):
    count = State.objects.all().delete
    return Response({'Message':'States Deleted'})

@api_view(['DELETE'])
def clearLga(request):
    count = Lga.objects.all().delete
    return Response({'Message':'LGAs Deleted'})

@api_view(['POST'])
def seed_parties(request):

    if request.method == 'POST':
        data =  [('Accord', 'A'),('Action Alliance', 'AA'),('Action Democratic Party', 'ADP'),('Action Peoples Party','APP'),('African Action Congress','AAC'),('African Democratic Congress', 'ADC'),('All Progressives Congress','APC'),('All Progressives Grand Alliance','APGA'),('Allied Peoples Movement', 'APM'),('Boot Party', 'BP'),('Labour Party', 'LP'),('National Rescue Movement', 'NRM'),('New Nigeria Peoples Party', 'NNPP'),('Peoples Democratic Party', 'PDP'),('Peoples Redemption Party', 'PRP'),('Social Democratic Party', 'SDP'),('Young Progressive Party', 'YPP'),('Zenith Labour Party', 'ZLP')]
        for i in data:
            json_data = {"name" : i[0], "abbr" : i[1]}
            serialized_data = PartySerializer(data=json_data)
            if serialized_data.is_valid():
                serialized_data.save()
        return Response(serialized_data.data)

@api_view(['POST'])
def seed_survey(request):

    if request.method == 'POST':
        serialized_data = SurveyCategoryCreateSerializer(data = {"surveyName" : "Others" })
        if serialized_data.is_valid():
            serialized_data.save()
        return Response(serialized_data.data)