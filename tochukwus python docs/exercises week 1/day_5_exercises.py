# Exercises: Day 5
# Exercises: Level 1
# 1
lst = list()

# 2
number = [1, 2, 3, 4, 5, 6, 7, 8]

# 3
print(len(number))

# 4
print(number[0])
print(number[3:5])
print(number[7])

# 5
mixed_data_types = ["Tochukwu", 18, 1.78,
                    "Single", "Gwarinpa, Abuja, Nigeria."]

# 6
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

# 10
it_companies[0] = "Samsung"
print(it_companies)

# 11
it_companies.append("Xiaomi")

# 12
it_companies.insert(3, "Nvidia")
print(it_companies)

# 13
it_companies[2] = "MICROSOFT"
print(it_companies)

# 14
joined = '# '.join(it_companies)
print(joined)

# 15
print("Google" in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
print(it_companies[0:3])

# 19
print(it_companies[6:9])

# 20
middle = len(it_companies) // 2
print(it_companies[middle])


# 21
it_companies.pop(0)
print(it_companies)

# 22
middle = len(it_companies) // 2
del it_companies[middle]
print(it_companies)

# 23
del it_companies[-1]
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies
# print(it_companies) #"Will display NameError: name 'it_companies' is not defined, as the list has been deleted."

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

stack = front_end + back_end
print(stack)

#27
full_stack = stack.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

#Exercises: Level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}, Max age: {max_age}")

#2
ages.extend([min_age, max_age])
ages.sort() 
median_age = (ages[5] + ages[6]) / 2
print(f"Median age: {median_age}")
print(ages)


#3
median_term1 = ages[5]
median_term2 = ages[6]
median_age = (median_term1 + median_term2)/2
print(f"Median age: {median_age}")

#4
term1,term2,term3,term4,term5,term6,term7,term8,term9,term10,term11,term12 = ages
print(term1)
average_age = (term1+term2+term3+term4+term5+term6+term7+term8+term9+term10+term11+term12)/12
print(f"Average age: {average_age}")

#or
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

#5
age_range = max_age - min_age

#6
print(abs(min_age - average_age) == (max_age - average_age))

#last part
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

#1
middle_index = len(countries) // 2
print(countries[middle_index])

#2
half = len(countries) // 2
first_half = countries[:half + 1] 
second_half = countries[half + 1:]
print(f"First half: {len(first_half)} countries")
print(f"Second half: {len(second_half)} countries")

# 3
small_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = small_list
print(china)   
print(russia)   
print(usa)      
print(scandic)  