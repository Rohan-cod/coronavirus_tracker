from django.core.management.base import BaseCommand
from selenium import webdriver
import re
from time import sleep
from datetime import datetime
from cases.models import Data

class Command(BaseCommand):
	help = "collect tnew Covid-19 cases"
	def handle(self, *args, **options):
		self.driver = webdriver.Chrome()
		try:
			self.driver.get('https://www.worldometers.info/coronavirus/')
			total_cases = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[2]").text)
			new_cases = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[3]").text)
			total_deaths = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[4]").text)
			new_deaths = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[5]").text)
			active_cases = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[7]").text)
			total_recovered = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[6]").text)
			serious_critical = str(self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr[43]/td[8]").text)
			if(len(total_cases)==0):
				total_cases='0'
			if(len(total_deaths)==0):
				total_deaths='0'
			if(len(total_recovered)==0):
				total_recovered='0'
			if(len(new_cases)==0):
				new_cases='0'
			if(len(new_deaths)==0):
				new_deaths='0'
			if(len(serious_critical)==0):
				serious_critical='0'
			if(len(active_cases)==0):
				active_cases='0'
			try:
				Data.objects.all().delete()
			except:
				pass
			try:

				Data.objects.create(
						total_cases=total_cases,
						new_cases=new_cases,
						total_deaths=total_deaths,
						new_deaths=new_deaths,
						active_cases=active_cases,
						total_recovered=total_recovered,
						serious_critical=serious_critical
					)
			except:
				pass


			self.driver.close()
			print("done")
		except Exception as e:
			print(str(e))
			self.driver.quit()