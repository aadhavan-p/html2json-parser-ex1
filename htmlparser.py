from bs4 import BeautifulSoup
import json


class Parser:

    def __init__(self) -> None:
        self.__capitals = []


    def __parse_data(self, file) -> list:
        soup = BeautifulSoup(file, 'lxml')

        return self.__parse_list_tag(soup.find_all("li"))


    def parse(self, file) -> json:
        self.__parse_data(file)
        
        return self.__jsonify(self.__capitals)


    def __parse_list_tag(self, lst: list):
        for i in lst:
            capital = self.__clean(i.strong.text)
            state = self.__clean(i.span.text)
            self.__capitals.append({"capital":capital, "state":state})


    def __clean(seld, s: str) -> list:
        return s.lstrip().rstrip()


    def __jsonify(self, lst: list):
        custom_json = {
            'capitals': lst,
            'summary': {
                'numberOfCapitals': len(lst)
            }
        }
        self.__capitals.clear
        return json.dumps(custom_json, indent=1)


