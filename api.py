import urllib
import json
import time
import web

db = web.database(dbn='sqlite', db='MovieSite.db')

movie_ids = []
for index in range(0, 250 ,50):
    print index
    response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
    data = response.read()
    # print data

    data_json = json.loads(data)
    movie250 = data_json['subjects']
    for movie in movie250:
        movie_ids.append(movie['id'])
        print movie['id'], movie['title']
    time.sleep(3)
print movie_ids

# movie_ids = [u'1292052', u'1295644', u'1292720', u'1291546', u'1292063', u'1292001', u'1295124', u'1291561', u'2131459', u'1292722', u'3541415', u'3793023', u'1291549', u'3011091', u'1291560', u'1291841', u'1292213', u'1300267', u'1291828', u'1292000', u'1849031', u'1292064', u'1291552', u'1293839', u'3442220', u'1293350', u'6786002', u'1293182', u'1291583', u'1291858', u'1292224', u'2129039', u'1299398', u'3319755', u'1900841', u'1292215', u'1309046', u'1307914', u'1298624', u'1851857', u'1291572', u'1291571', u'5912992', u'1306029', u'1292365', u'1299131', u'1292370', u'1292223', u'1929463', u'1292220', u'1294639', u'1308807', u'1291548', u'1292262', u'1296736', u'1294408', u'1780330', u'1301753', u'1787291', u'1303021', u'3072124', u'1291832', u'2149806', u'1292343', u'1293544', u'1485260', u'1291545', u'1316510', u'1291843', u'1291875', u'1297359', u'1292849', u'1297630', u'3742360', u'1292208', u'4917726', u'1291818', u'1292656', u'1293318', u'1292402', u'1418019', u'1292434', u'1305164', u'1291999', u'3443389', u'1292679', u'1296339', u'1291990', u'1291585', u'1295865', u'1298070', u'4268598', u'2353023', u'1296909', u'1652587', u'1297052', u'1297192', u'1292401', u'1293359', u'5322596', u'2334904', u'1417598', u'1292274', u'1294371', u'1292528', u'3287562', u'4202302', u'1292328', u'1937946', u'3792799', u'1293964', u'1291870', u'2209573', u'1295399', u'1418834', u'1309163', u'1304447', u'1578507', u'1305487', u'1291579', u'1297447', u'1291822', u'2043546', u'1306861', u'1293460', u'1858711', u'1300960', u'1302827', u'1907966', u'3008247', u'1388216', u'3007773', u'1294240', u'1760622', u'21937445', u'1418200', u'1295409', u'1297574', u'1291578', u'1300992', u'1295038', u'1292281', u'2297265', u'1300299', u'1905462', u'1293172', u'1978709', u'1308857', u'6985810', u'1292270', u'1303037', u'1397546', u'1296141', u'2213597', u'1419936', u'1307793', u'1291879', u'5964718', u'1300374', u'21937452', u'1865703', u'4798888', u'5989818', u'1292728', u'1296753', u'1291853', u'2363506', u'1292217', u'1308817', u'1294638', u'3011235', u'1304102', u'1292659', u'2053515', u'1293181', u'1297478', u'1308767', u'1305690', u'1292233', u'3157605', u'1308575', u'11525673', u'2300586', u'1299361', u'1302476', u'2365260', u'1292056', u'1293764', u'1292218', u'1307811', u'1292214', u'1307315', u'1291557', u'1401118', u'1309027', u'1299327', u'1306249', u'1291844', u'1292062', u'1308777', u'1291992', u'1292287', u'3217169', u'1303394', u'1301171', u'1293908', u'1302425', u'1959195', u'1302467', u'4739952', u'1867345', u'10777687', u'3011051', u'1291568', u'1301169', u'1438652', u'3075287', u'1756073', u'1301617', u'1292055', u'1316572', u'1298653', u'1292329', u'4023638', u'1428175', u'1293530', u'6146955', u'1962116', u'1293399', u'1291565', u'3073124', u'1305725', u'1293929', u'21360417', u'1292925', u'1844413', u'1292348', u'1395091', u'5908478', u'6534248', u'1304073', u'3824274', u'1369747', u'1292047', u'1291824', u'1300117', u'1293708', u'1300741', u'1862151', u'1304056']

def add_movie(movie,num):
    movie = json.loads(data)
    db.insert('movie',
        no=num+1,
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts=','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
    )
    print movie['title']


count = 0
for mid in movie_ids:
    print count, mid
    response = urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' % mid)
    data = response.read()
    add_movie(data,count)
    count += 1
    time.sleep(1)