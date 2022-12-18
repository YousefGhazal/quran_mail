from random import randrange
import requests
from celery import shared_task
from .models import User
from .notifications import Email

range_ayah = {
    "1": "7",
    "2": "286",
    "3": "200",
    "4": "176",
    "5": "120",
    "6": "165",
    "7": "206",
    "8": "75",
    "9": "129",
    "10": "109",
    "11": "123",
    "12": "111",
    "13": "43",
    "14": "52",
    "15": "99",
    "16": "128",
    "17": "111",
    "18": "110",
    "19": "98",
    "20": "135",
    "21": "112",
    "22": "78",
    "23": "118",
    "24": "64",
    "25": "77",
    "26": "227",
    "27": "93",
    "28": "88",
    "29": "69",
    "30": "60",
    "31": "34",
    "32": "30",
    "33": "73",
    "34": "54",
    "35": "45",
    "36": "83",
    "37": "182",
    "38": "88",
    "39": "75",
    "40": "85",
    "41": "54",
    "42": "53",
    "43": "89",
    "44": "59",
    "45": "37",
    "46": "35",
    "47": "38",
    "48": "29",
    "49": "18",
    "50": "45",
    "51": "60",
    "52": "49",
    "53": "62",
    "54": "55",
    "55": "78",
    "56": "96",
    "57": "29",
    "58": "22",
    "59": "24",
    "60": "13",
    "61": "14",
    "62": "11",
    "63": "11",
    "64": "18",
    "65": "12",
    "66": "12",
    "67": "30",
    "68": "52",
    "69": "52",
    "70": "44",
    "71": "28",
    "72": "28",
    "73": "20",
    "74": "56",
    "75": "40",
    "76": "31",
    "77": "50",
    "78": "40",
    "79": "46",
    "80": "42",
    "81": "29",
    "82": "19",
    "83": "36",
    "84": "25",
    "85": "22",
    "86": "17",
    "87": "19",
    "88": "26",
    "89": "30",
    "90": "20",
    "91": "15",
    "92": "21",
    "93": "11",
    "94": "8",
    "95": "8",
    "96": "19",
    "97": "5",
    "98": "8",
    "99": "8",
    "100": "11",
    "101": "11",
    "102": "8",
    "103": "3",
    "104": "9",
    "105": "5",
    "106": "4",
    "107": "7",
    "108": "3",
    "109": "6",
    "110": "3",
    "111": "5",
    "112": "4",
    "113": "5",
    "114": "6"
}

def get_ayah():
    sura_number = randrange(1,114)
    ayah = range_ayah[str(sura_number)]
    ayah_number = randrange(2,int(ayah))
   
    url_aya = f'http://api.quran-tafseer.com/quran/{sura_number}/{ayah_number}'
    url_tafseer = f'http://api.quran-tafseer.com/tafseer/1/{sura_number}/{ayah_number}'

    return url_aya, url_tafseer

def send_request(url_aya, url_tafseer):
    response_aya = requests.get(url_aya)
    response_tafseer = requests.get(url_tafseer)
    r_aya = response_aya.json()
    r_tafseer = response_tafseer.json()

    return r_aya['text'], r_tafseer['text'] , r_aya['sura_name'], r_aya["ayah_number"]

# with open('text.txt', 'w') as f:
#     f.write(str(send_request(*get_ayah())))
    
@shared_task
def active_user():
    users = User.objects.filter(active=True)
    m_ayah, m_tafseer, num_ayah, name_sura = send_request(*get_ayah())
    for user in users:
        Email( m_ayah, m_tafseer, num_ayah, name_sura, user.email).send()
        
"""
background task (function) runner
1. normal life cycle -> send function to run in background
   ex: after user registration > send email
  request ------------------   response 
                    |
                    | 
                background -------------------------------------- 
2. cron job (التكرارية)
    function that runs on certain times


project (python) -> message(text) [rabbit mq - redis - others]  -> celery (python)





"""