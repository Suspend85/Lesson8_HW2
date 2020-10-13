# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.
# Задача №2. Написать программу для файла в формате xml.

import xml
from pprint import pprint
from collections import Counter
import xml.etree.ElementTree as ET


def getting_text_from_xml(filename):
    """ Opening file anf reading data to news_text"""
    tree = ET.parse("newsafr.xml")
    root = tree.getroot()
    items = root.findall("channel/item")
    news_text = ''
    for item in items:
        news_text += item.find("description").text
    return news_text


def counting_news_text(news_text, char_count):
    """ Creating list of words and their rating """
    words = news_text.split()
    filter_list = []
    res = []
    for word in words:
        if len(word) >= int(char_count):
            filter_list.append(word)
    word_counts = Counter([word.lower() for word in filter_list])
    for key, value in word_counts.items():
        res.append([key, value])
    return res


def rating_news(res, word_count):
    """ Creating top list """
    res = sorted(res, key=lambda x: x[1], reverse=True)
    top_words = res[: int(word_count)]
    return top_words


def main():
    pprint(rating_news(counting_news_text(getting_text_from_xml(
        "newsafr.xml"), input("Кол-во символов: ")), input("кол-во слов: ")))


main()