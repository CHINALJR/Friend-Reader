#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser,logging

class socialspider(object):

	def __init__(self):
		self.loadConfig()
		self.prepare()
	
	def loadConfig(self):
		self.socialRoot="./social/"
		self.allConfig=configparser.ConfigParser(interpolation=None)
		self.allConfig.read(self.socialRoot+"configspider.properties",encoding='utf-8')
		
	def prepare(self):
		logging.basicConfig(format='%(asctime)s --%(lineno)s -- %(levelname)s:%(message)s', level=logging.DEBUG)
