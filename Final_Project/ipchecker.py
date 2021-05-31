import codecs
import sys

def main():
    sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'strict')

    app = Ip_detail(input("Please enter ip address: "))
    print(app.Json_self())


class Ip_detail:
    def __init__(self, ip):
        self.ip = ip

    def Check_ip(self):
        '''check if ip is valid'''
        import ipaddress
        if ipaddress.ip_address(self.ip):
            return self.ip
        else:
            return f"Invalid IP Address\nPlease read on about section"

    def Json_self(self):
        a = Ip_detail.Check_ip(self)
        from urllib.request import urlopen
        lin = urlopen('http://api.ipstack.com/' + a + '?access_key=13bcacf3956ec6bfe60a70216b9b024a').read()
        import json
        jss = json.loads(lin)
        out = lambda x, y, z="🔴": f"{z} {x}: {jss.get(y)}\n"
        return f"Final Project for Code In Place\n" \
               f"Here is your result: \n\n" \
               f"{out('TYPE', 'type')}" \
               f"{out('CONTINENT NAME', 'continent_name')}" \
               f"{out('CONTINENT CODE', 'continent_code')}" \
               f"{out('COUNTRY NAME', 'country_name')}" \
               f"{out('COUNTRY CODE', 'country_code')}" \
               f"{out('REGION CODE', 'region_code')}" \
               f"{out('REGION NAME', 'region_name')}" \
               f"{out('CITY', 'city')}" \
               f"{out('ZIP', 'zip')}" \
               f"{out('COUNTRY FLAG', 'country_flag_emoji_unicode')}" \
               f"\n\nMd Shoriful Islam, Github: https://github.com/mdsiaofficial \n" \
               f"Md Shoriful Islam, LinkedIn: https://www.linkedin.com/in/mdsiaofficial/" \
               f" \n" \

if __name__ == '__main__':
    main()