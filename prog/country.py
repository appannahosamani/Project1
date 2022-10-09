RevenueData = [
				{"Region":"Europe","Country":"GB","CityID": 1, "Revenue":100},
				{"Region":"Europe","Country":"GB","CityID": 2, "Revenue":200},
				{"Region":"Europe","Country":"GB","CityID": 1, "Revenue":300},
				{"Region":"Europe","Country":"GB","CityID": 1, "Revenue":150},
				{"Region":"Europe","Country":"FR","CityID": 3, "Revenue":170},
				{"Region":"Europe","Country":"FR","CityID": 3, "Revenue":190},
				{"Region":"Asia","Country":"IN","CityID": 4, "Revenue":205},
				{"Region":"Asia","Country":"PK","CityID": 5, "Revenue":186},
				{"Region":"Asia","Country":"BG","CityID": 6, "Revenue":188},
				{"Region":"Asia","Country":"IN","CityID": 4, "Revenue":196},
				{"Region":"Asia","Country":"IN","CityID": 7, "Revenue":191},
				{"Region":"Asia","Country":"IN","CityID": 4, "Revenue":157},
				{"Region":"Europe","Country":"GB","CityID": 1, "Revenue":177}
]
CityData = [
			{"CityID": 1, "CityName": "LON"},
			{"CityID": 2, "CityName": "MAN"},
			{"CityID": 3, "CityName": "PAR"},
			{"CityID": 4, "CityName": "DEL"},
			{"CityID": 5, "CityName": "LAH"},
			{"CityID": 6, "CityName": "DHA"},
			{"CityID": 7, "CityName": "MUM"}
]


finaldata=[]
for i in range(len(CityData)):
    total=0
    res={}
	
    for j in range(len(RevenueData)):
		
		# a=CityData[i][]
    	if CityData[i]['CityID']==RevenueData[j]["CityID"]:
            total+=RevenueData[j]['Revenue']
            res.update(RevenueData[j])
			# res.update(RevenueData[j]['CityID']=)
			
    res['Revenue']=total
	# res['ds']=total
	
	# res.pop('CityID')
	
    finaldata.append(res)
print("finalData",finaldata)

# FinalOutput = [
# 	{"Region": "Europe", "Country": "GB": "City":"LON", "Revenue":<Total>},
# 	{"Region": "Europe", "Country": "GB": "City":"MAN", "Revenue":<Total>},
# 	{"Region": "Europe", "Country": "FR": "City":"PAR", "Revenue":<Total>},
# 	{"Region": "Asia", "Country": "IN": "City":"DEL", "Revenue":<Total>},
# 	{"Region": "Asia", "Country": "PK": "City":"LAH", "Revenue":<Total>},
# 	{"Region": "Asia", "Country": "BG": "City":"DHA", "Revenue":<Total>},
# 	{"Region": "Asia", "Country": "IN": "City":"MUM", "Revenue":<Total>},
# ]

