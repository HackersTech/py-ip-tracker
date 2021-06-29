#
import os
os.system('bash ip.sh')
import pygeoip
gi  =  pygeoip.GeoIP('GeoLiteCity.dat')

print ("\033[5;35m made by Hackers Tech ")

print ('example -192.168.50.229')
ip=input("\033[5;36m enter ip address here :")
if ip !="":
	def printRecord(ip):
		rec  =  gi.record_by_name(ip)
		city  =  rec['city']
		region  =  rec['region_name']
		country  =  rec['country_name']
		long  =  rec['longitude']
		lat  =  rec['latitude']
		print ('\033[5;32m [*] Target: '  +  ip  +  ' Geo-located. ')
		print ('\033[5;33m [+] Latitude: '+str(lat)+  ' Longitude: '+  str(long))

	printRecord(ip)

else :
	print ("\033[5;31m invalid input exiting !!!")

