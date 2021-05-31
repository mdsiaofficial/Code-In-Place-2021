# Enter a city name or type 'help' for more

class WorldTimeZone:
    global Region1, regd1
    author = 'Mirielle'

    def __init__(self, region) -> 'INIT':
        self.region = region

    def Continent(self):
        '''Return list of all continents'''
        print('\n'.join(
            set([x[0] for i, x in enumerate(regd1)])))

    def Location1(self):
        '''Return lists of all supported regions'''
        return [x[1] for i, x in enumerate(regd1)]

    def Ldict1(self):
        '''Return a dictionary of continents and regions'''
        return dict(
            zip(
                [x[1] for i, x in enumerate(regd1)],
                [x[0] for i, x in enumerate(regd1)]
            ))


inp = input() or 'Moscow'

from sys import exit

Region1 = """Africa/Abidjan
Africa/Accra
Africa/Algiers
Africa/Bissau
Africa/Cairo
Africa/Casablanca
Africa/Ceuta
Africa/El_Aaiun
Africa/Johannesburg
Africa/Juba
Africa/Khartoum
Africa/Lagos
Africa/Maputo
Africa/Monrovia
Africa/Nairobi
Africa/Ndjamena
Africa/Sao_Tome
Africa/Tripoli
Africa/Tunis
Africa/Windhoek
America/Adak
America/Anchorage
America/Araguaina
America/Asuncion
America/Atikokan
America/Bahia
America/Bahia_Banderas
America/Barbados
America/Belem
America/Belize
America/Blanc-Sablon
America/Boa_Vista
America/Bogota
America/Boise
America/Cambridge_Bay
America/Campo_Grande
America/Cancun
America/Caracas
America/Cayenne
America/Chicago
America/Chihuahua
America/Costa_Rica
America/Creston
America/Cuiaba
America/Curacao
America/Danmarkshavn
America/Dawson
America/Dawson_Creek
America/Denver
America/Detroit
America/Edmonton
America/Eirunepe
America/El_Salvador
America/Fort_Nelson
America/Fortaleza
America/Glace_Bay
America/Godthab
America/Goose_Bay
America/Grand_Turk
America/Guatemala
America/Guayaquil
America/Guyana
America/Halifax
America/Havana
America/Hermosillo
America/Inuvik
America/Iqaluit
America/Jamaica
America/Juneau
America/La_Paz
America/Lima
America/Los_Angeles
America/Maceio
America/Managua
America/Manaus
America/Martinique
America/Matamoros
America/Mazatlan
America/Menominee
America/Merida
America/Metlakatla
America/Mexico_City
America/Miquelon
America/Moncton
America/Monterrey
America/Montevideo
America/Nassau
America/New_York
America/Nipigon
America/Nome
America/Noronha
America/Ojinaga
America/Panama
America/Pangnirtung
America/Paramaribo
America/Phoenix
America/Port-au-Prince
America/Port_of_Spain
America/Porto_Velho
America/Puerto_Rico
America/Punta_Arenas
America/Rainy_River
America/Rankin_Inlet
America/Recife
America/Regina
America/Resolute
America/Rio_Branco
America/Santarem
America/Santiago
America/Santo_Domingo
America/Sao_Paulo
America/Scoresbysund
America/Sitka
America/St_Johns
America/Swift_Current
America/Tegucigalpa
America/Thule
America/Thunder_Bay
America/Tijuana
America/Toronto
America/Vancouver
America/Whitehorse
America/Winnipeg
America/Yakutat
America/Yellowknife
Antarctica/Casey
Antarctica/Davis
Antarctica/DumontDUrville
Antarctica/Macquarie
Antarctica/Mawson
Antarctica/Palmer
Antarctica/Rothera
Antarctica/Syowa
Antarctica/Troll
Antarctica/Vostok
Asia/Almaty
Asia/Amman
Asia/Anadyr
Asia/Aqtau
Asia/Aqtobe
Asia/Ashgabat
Asia/Atyrau
Asia/Baghdad
Asia/Baku
Asia/Bangkok
Asia/Barnaul
Asia/Beirut
Asia/Bishkek
Asia/Brunei
Asia/Chita
Asia/Choibalsan
Asia/Colombo
Asia/Damascus
Asia/Dhaka
Asia/Dili
Asia/Dubai
Asia/Dushanbe
Asia/Famagusta
Asia/Gaza
Asia/Hebron
Asia/Ho_Chi_Minh
Asia/Hong_Kong
Asia/Hovd
Asia/Irkutsk
Asia/Jakarta
Asia/Jayapura
Asia/Jerusalem
Asia/Kabul
Asia/Kamchatka
Asia/Karachi
Asia/Kathmandu
Asia/Khandyga
Asia/Kolkata
Asia/Krasnoyarsk
Asia/Kuala_Lumpur
Asia/Kuching
Asia/Macau
Asia/Magadan
Asia/Makassar
Asia/Manila
Asia/Nicosia
Asia/Novokuznetsk
Asia/Novosibirsk
Asia/Omsk
Asia/Oral
Asia/Pontianak
Asia/Pyongyang
Asia/Qatar
Asia/Qostanay
Asia/Qyzylorda
Asia/Riyadh
Asia/Sakhalin
Asia/Samarkand
Asia/Seoul
Asia/Shanghai
Asia/Singapore
Asia/Srednekolymsk
Asia/Taipei
Asia/Tashkent
Asia/Tbilisi
Asia/Tehran
Asia/Thimphu
Asia/Tokyo
Asia/Tomsk
Asia/Ulaanbaatar
Asia/Urumqi
Asia/Ust-Nera
Asia/Vladivostok
Asia/Yakutsk
Asia/Yangon
Asia/Yekaterinburg
Asia/Yerevan
Atlantic/Azores
Atlantic/Bermuda
Atlantic/Canary
Atlantic/Cape_Verde
Atlantic/Faroe
Atlantic/Madeira
Atlantic/Reykjavik
Atlantic/South_Georgia
Atlantic/Stanley
Australia/Adelaide
Australia/Brisbane
Australia/Broken_Hill
Australia/Currie
Australia/Darwin
Australia/Eucla
Australia/Hobart
Australia/Lindeman
Australia/Lord_Howe
Australia/Melbourne
Australia/Perth
Australia/Sydney
Europe/Amsterdam
Europe/Andorra
Europe/Astrakhan
Europe/Athens
Europe/Belgrade
Europe/Berlin
Europe/Brussels
Europe/Bucharest
Europe/Budapest
Europe/Chisinau
Europe/Copenhagen
Europe/Dublin
Europe/Gibraltar
Europe/Helsinki
Europe/Istanbul
Europe/Kaliningrad
Europe/Kiev
Europe/Kirov
Europe/Lisbon
Europe/London
Europe/Luxembourg
Europe/Madrid
Europe/Malta
Europe/Minsk
Europe/Monaco
Europe/Moscow
Europe/Oslo
Europe/Paris
Europe/Prague
Europe/Riga
Europe/Rome
Europe/Samara
Europe/Saratov
Europe/Simferopol
Europe/Sofia
Europe/Stockholm
Europe/Tallinn
Europe/Tirane
Europe/Ulyanovsk
Europe/Uzhgorod
Europe/Vienna
Europe/Vilnius
Europe/Volgograd
Europe/Warsaw
Europe/Zaporozhye
Europe/Zurich
Indian/Chagos
Indian/Christmas
Indian/Cocos
Indian/Kerguelen
Indian/Mahe
Indian/Maldives
Indian/Mauritius
Indian/Reunion
Pacific/Apia
Pacific/Auckland
Pacific/Bougainville
Pacific/Chatham
Pacific/Chuuk
Pacific/Easter
Pacific/Efate
Pacific/Enderbury
Pacific/Fakaofo
Pacific/Fiji
Pacific/Funafuti
Pacific/Galapagos
Pacific/Gambier
Pacific/Guadalcanal
Pacific/Guam
Pacific/Honolulu
Pacific/Kiritimati
Pacific/Kosrae
Pacific/Kwajalein
Pacific/Majuro
Pacific/Marquesas
Pacific/Nauru
Pacific/Niue
Pacific/Norfolk
Pacific/Noumea
Pacific/Pago_Pago
Pacific/Palau
Pacific/Pitcairn
Pacific/Pohnpei
Pacific/Port_Moresby
Pacific/Rarotonga
Pacific/Tahiti
Pacific/Tarawa
Pacific/Tongatapu
Pacific/Wake
Pacific/Wallis""".split('\n')

regd1 = list(map(lambda x: x.split('/'), Region1))


class WorldTimeZone2(WorldTimeZone):
    global Region2, regd2

    def LocationAll(self):
        '''Return list of all supported locatons'''
        a = WorldTimeZone.Location1(self)
        return [
            print(i, '\t', x)
            for i, x in enumerate(a + [c for a, b, c in regd2])]

    def AllDict(self):
        '''return dict of all locations and their TZ'''
        Ldict2 = {c: a + '/' + b for a, b, c in regd2}
        return {**Ldict2, **WorldTimeZone.Ldict1(self)}


Region2 = """America/Argentina/Buenos_Aires
America/Argentina/Catamarca
America/Argentina/Cordoba
America/Argentina/Jujuy
America/Argentina/La_Rioja
America/Argentina/Mendoza
America/Argentina/Rio_Gallegos
America/Argentina/Salta
America/Argentina/San_Juan
America/Argentina/San_Luis
America/Argentina/Tucuman
America/Argentina/Ushuaia
America/Indiana/Indianapolis
America/Indiana/Knox
America/Indiana/Marengo
America/Indiana/Petersburg
America/Indiana/Tell_City
America/Indiana/Vevay
America/Indiana/Vincennes
America/Indiana/Winamac
America/Kentucky/Louisville
America/Kentucky/Monticello
America/North_Dakota/Beulah
America/North_Dakota/Center
America/North_Dakota/New_Salem""".split('\n')

regd2 = list(map(lambda x: x.split('/'), Region2))

help_ = '''
<-----search options----->

... continents = [list of all continents]
... available  = [list of all supported regions]
... help       = [return help]

or

ENTER a city name e.g moscow, sydney, seoul'''


class Application(WorldTimeZone2):
    # validates input
    def Validate(self):

        a = WorldTimeZone2.AllDict(self)

        if (self.region).lower() == 'continents':
            print("Lists of Available Continents are:",
                  '-' * 20, sep='\n')
            WorldTimeZone2.Continent(self)
            print(
                '\n\nAuthor : Mirielle\nDate : Sept. 2019')
            return exit()

        if (self.region).lower() == 'available':
            print(WorldTimeZone2.LocationAll(self))
            return exit()

        if (self.region).lower() == 'help':
            global help_
            print(help_)
            return exit()

        if (self.region).title().replace(' ', '_') in a.keys():
            from urllib.request import urlopen
            import json
            self.region = (self.region).title().replace(' ', '_')
            link = urlopen('http://worldtimeapi.org/api/timezone/{}/{}'.format(
                a[self.region], self.region)).read()
            js_ = json.loads(link)
            return [js_.get('datetime'), js_.get('timezone')]
        else:
            print('Bad input using default!\nPlease type help for more')
            return exit()

    def Time(self):
        a = Application.Validate(self)
        tz = a[1]
        t = a[0].split('T')
        t = t[1].split('.')
        t = t[0].split(':')
        hour, minn = t[0], t[1]
        print(
            f'{chr(9193) * 3} "{self.region}" right now{chr(9200)} {chr(9194) * 3}\n',
            sep='\n',
            end='\n'
        )
        return f'{hour}:{minn}'


from sys import stdout

stdout.reconfigure(encoding='utf-16')

app = Application(inp)

timey = app.Time()

zero, one, two, three, four, five, six, seven, eight, nine, m, a, p, sep = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1],
                                                                            [1, 0, 0, 0, 1], [1, 0, 0, 0, 1],
                                                                            [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [
                                                                               [0, 0, 1, 0, 0], [0, 1, 1, 0, 0],
                                                                               [1, 0, 1, 0, 0], [0, 0, 1, 0, 0],
                                                                               [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]], [
                                                                               [0, 1, 1, 1, 0], [1, 0, 0, 0, 1],
                                                                               [0, 0, 0, 1, 0], [0, 0, 1, 0, 0],
                                                                               [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]], [
                                                                               [1, 1, 1, 1, 0], [0, 0, 0, 0, 1],
                                                                               [1, 1, 1, 1, 1], [0, 0, 0, 0, 1],
                                                                               [0, 0, 0, 0, 1], [1, 1, 1, 1, 0]], [
                                                                               [1, 0, 0, 0, 0], [1, 0, 0, 0, 0],
                                                                               [1, 0, 1, 0, 0], [1, 1, 1, 1, 1],
                                                                               [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], [
                                                                               [1, 1, 1, 1, 1], [1, 0, 0, 0, 0],
                                                                               [1, 0, 0, 0, 0], [1, 1, 1, 1, 1],
                                                                               [0, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [
                                                                               [0, 1, 1, 1, 0], [1, 0, 0, 0, 0],
                                                                               [1, 0, 0, 0, 0], [1, 1, 1, 1, 0],
                                                                               [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [
                                                                               [1, 1, 1, 1, 0], [0, 0, 0, 0, 1],
                                                                               [0, 0, 0, 0, 1], [0, 0, 0, 0, 1],
                                                                               [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]], [
                                                                               [0, 1, 1, 1, 0], [1, 0, 0, 0, 1],
                                                                               [1, 1, 1, 1, 1], [1, 0, 0, 0, 1],
                                                                               [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [
                                                                               [0, 1, 1, 1, 0], [1, 0, 0, 0, 1],
                                                                               [0, 1, 1, 1, 1], [0, 0, 0, 0, 1],
                                                                               [0, 0, 0, 0, 1], [0, 1, 1, 1, 0]], [
                                                                               [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                                                               [0, 0, 0, 0, 0], [1, 1, 0, 1, 1],
                                                                               [1, 0, 1, 0, 1], [1, 0, 0, 0, 1],
                                                                               [1, 0, 0, 0, 1]], [[0, 0, 0, 0, 0],
                                                                                                  [0, 0, 0, 0, 0],
                                                                                                  [0, 1, 1, 0, 0],
                                                                                                  [1, 0, 0, 1, 0],
                                                                                                  [1, 1, 1, 1, 0],
                                                                                                  [1, 0, 0, 1, 0]], [
                                                                               [0, 0, 0, 0, 0], [1, 1, 1, 1, 0],
                                                                               [1, 0, 0, 1, 0], [1, 1, 1, 1, 0],
                                                                               [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], [
                                                                               [0, 0, 0, 0, 0], [0, 0, 2, 0, 0],
                                                                               [0, 0, 2, 0, 0], [0, 0, 0, 0, 0],
                                                                               [0, 0, 2, 0, 0], [0, 0, 2, 0, 0]]

digdict_ = {str(i): v for i, v in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}
alpdict_ = {'a': a, 'm': m, 'p': p, ':': sep}
all_dict = {**digdict_, **alpdict_}

for i in range(6):
    for time in timey:
        for col in all_dict[time][i]:
            if col == 0:
                print(' ', end="")
            elif col == 1:
                print('#', end="")
            elif col == 2:
                print('*', end='')
        print(" ", end="")
    print()

print(chr(11036) * 22, sep='')
[print(
    chr(11035), a, b)
    for a, b in
    [('Author', 'Mirielle'),
     ('Date  ', 'Sept. 2019')
     ]
]