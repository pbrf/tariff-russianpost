#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
import urllib2


class TariffRussianpost:

    def __init__(self):
        self.url = 'http://tariff.russianpost.ru/tariff/v1/'

    def calc(self, data):
        typ = data['type']
        cat = data['cat']
        direction = data['direction']
        date_raw = datetime.date.today()
        date = int(date_raw.strftime('%Y%m%d'))
        weight = data['weight']
        if data['sum_num']:
            sum_num = data['sum_num']
        sumoc = data['Value']
        isavia = data['isavia']
        index_from = data['index_from']
        index_to = data['index_to']
        closed = 1
        service = data['service']
        response_raw = urllib2.urlopen('{0}calculate?json&typ={1}&cat={2}&dir={3}&weight={4}&date={5}&sumoc={6}&from={7}&to={8}&isavia={9}&closed={10}&service={11}'
                                       .format(self.url,
                                               typ,
                                               cat,
                                               direction,
                                               weight,
                                               date,
                                               sumoc,
                                               index_from,
                                               index_to,
                                               isavia,
                                               closed,
                                               service)).read()
        response = json.loads(response_raw.decode('utf-8'))
        response_cost = response['paynds']
        return response_cost

    def category_list(self):
        response_raw = urllib2.urlopen('{0}dictionary?json&category=all'.format(self.url)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response

    def service_list(self):
        response_raw = urllib2.urlopen('{0}dictionary?json&service'.format(self.url)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response

    def object_tariff_list(self, typ, cat, direction):
        response_raw = urllib2.urlopen('{0}dictionary?json&object&typ={1}&cat={2}&dir={3}'.format(self.url, typ, cat, direction)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response

    def object_tariff_details(self, cat):
        response_raw = urllib2.urlopen('{0}dictionary?json&object={1}'.format(self.url, cat)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response

    def object_category_description(self, cat):
        response_raw = urllib2.urlopen('{0}dictionary?json&category={1}'.format(self.url, cat)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response

    def country_list(self):
        response_raw = urllib2.urlopen('{0}dictionary?json&country'.format(self.url)).read()
        response = json.loads(response_raw.decode('utf-8'))
        return response
