#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_excel(r'../data/raw/data_glotip.xlsx')
print(df.head())


# In[2]:


new_columns = df.iloc[1].tolist()
df.columns = new_columns
df = df.drop(1).reset_index(drop=True)
df = df.drop(0).reset_index(drop=True)
display(df.head())


# In[3]:


df.drop(columns='Iso3_code',  inplace=True)
df.drop(columns='Unit of measurement',  inplace=True)
df.drop(columns='Source',  inplace=True)
display(df.head())


# In[4]:


import numpy as np
df['Sex'] = df['Sex'].replace('Total', 'Unknown')
df['Sex'] = df['Sex'].str.capitalize()


# In[5]:


print(df['Sex'].unique())


# In[6]:


df['Sex'].value_counts()


# In[7]:


print(df['Age'].unique())


# In[8]:


import numpy as np

df['Age'] = df['Age'].replace({
    '0 to 17 years': 'Minor',
    '18 years or over': 'Adult',
    'Total': 'Unknown',
    'Unknown': 'Unknown',
})


# In[9]:


print(df['Age'].unique())


# In[10]:


df['Age'].value_counts()


# In[11]:


df.shape[0]


# In[12]:


df = df.rename(columns={'txtVALUE': 'Nr_of_victims'})
df['Nr_of_victims'].nunique()


# In[13]:


display(df.head())


# In[14]:


df1 = df[df['Indicator'] == 'Detected trafficking victims'].copy()


# In[15]:


df1.head()


# In[16]:


df1.shape


# In[17]:


df1['Nr_of_victims']= df1['Nr_of_victims'].replace('<5',2.5)


# In[18]:


df1.head()


# In[19]:


df1.shape


# In[20]:


df1['Nr_of_victims'].unique()


# In[21]:


df1['Nr_of_victims']= df1['Nr_of_victims'].astype(str).str.replace(',', '')


# In[22]:


df1['Nr_of_victims'].unique()


# In[23]:


df1.dtypes


# In[24]:


df1['Nr_of_victims'] = df1['Nr_of_victims'].astype(float)
print(f"The new data type of the 'Nr_of_victims' column is: {df1['Nr_of_victims'].dtype}")


# In[25]:


df1['Year'] = pd.to_datetime(df1['Year'], format='%Y').dt.year
df1.dtypes


# In[26]:


df1.shape


# In[27]:


df1['Dimension'] = df['Dimension'].replace('Total', 'Unknown')


# In[28]:


df1['Category'] = df['Category'].replace('Total', 'Unknown')


# In[29]:


df1['Category'].unique()


# In[30]:


# Diccionario de correcciones para estandarizar nombres de países y nacionalidades
corrections = {
    # Variaciones de países en español/inglés
    'ARGENTINA': 'Argentina',
    'BOLIVIA': 'Bolivia',
    'BRASIL': 'Brazil',
    'BARSIL': 'Brazil',
    'Bresil': 'Brazil',
    'Brasil': 'Brazil',
    'Brasilero': 'Brazil',
    'BRASILERA': 'Brazil',
    'Brazilian': 'Brazil',
    'CHILE': 'Chile',
    'COLOMBIA': 'Colombia',
    'Columbia': 'Colombia',
    'Colombie': 'Colombia',
    'COLOMBIANA': 'Colombia',
    'Colombiano': 'Colombia',
    'Colombian': 'Colombia',
    'ECUADOR': 'Ecuador',
    'Ecuatoriana': 'Ecuador',
    'Ecuadorean': 'Ecuador',
    'PERU': 'Peru',
    'PERO': 'Peru',
    'PER�': 'Peru',
    'Per�': 'Peru',
    'Peruana': 'Peru',
    'Peruano': 'Peru',
    'Peruvian': 'Peru',
    'PARAGUAY': 'Paraguay',
    'Paraguayo': 'Paraguay',
    'Paraguayian': 'Paraguay',
    'VENEZUELA': 'Venezuela',
    'VENEZOLANA': 'Venezuela',
    'Venezolano': 'Venezuela',
    'Venezuelan': 'Venezuela',
    'Venezuelans': 'Venezuela',
    'URUGUAY': 'Uruguay',
    'Uruguayan': 'Uruguay',

    # República Dominicana
    'R.DOMINICANA': 'Dominican Republic',
    'R.Dominicana': 'Dominican Republic',
    'R.dominicana': 'Dominican Republic',
    'Rep�blica Dominicana': 'Dominican Republic',
    'Rep. Dominicana': 'Dominican Republic',
    'REP. DOMINICANA': 'Dominican Republic',
    'REP�BLICA DOMINICANA': 'Dominican Republic',
    'REPUBLICA DOMINICANA': 'Dominican Republic',
    'República Dominicana': 'Dominican Republic',
    'DOMINICANA': 'Dominican Republic',
    'Dominican rep': 'Dominican Republic',
    'Dominican Rep': 'Dominican Republic',
    'Dominican Rebublic': 'Dominican Republic',

    # México
    'MEXICO': 'Mexico',
    'M�XICO': 'Mexico',
    'México': 'Mexico',
    'MEXICANA': 'Mexico',
    'Mexican': 'Mexico',

    # Panamá
    'PANAM�': 'Panama',
    'Panamá': 'Panama',
    'Panam�': 'Panama',
    'PANAM�': 'Panama',

    # España
    'ESPA�A': 'Spain',
    'España': 'Spain',
    'Espa�a': 'Spain',
    'Spanish': 'Spain',
    'Spania': 'Spain',

    # Estados Unidos
    'Estados Unidos': 'United States',
    'USA': 'United States',
    'United States of America': 'United States',

    # Centroamérica
    'GUATEMALA': 'Guatemala',
    'GUATEMALTECA': 'Guatemala',
    'Guatemalean': 'Guatemala',
    'HONDURAS': 'Honduras',
    'HONDUREÑA': 'Honduras',
    'HONDURE�A': 'Honduras',
    'Hondureans': 'Honduras',
    'Honduranian': 'Honduras',
    'Hodruanian': 'Honduras',
    'NICARAGUA': 'Nicaragua',
    'NICARAGUENSE': 'Nicaragua',
    'Nicaraguarean': 'Nicaragua',
    'COSTA RICA': 'Costa Rica',
    'EL SALVADOR': 'El Salvador',
    'SALVADOREÑA': 'El Salvador',
    'SALVADORE�A': 'El Salvador',
    'Salvadorean': 'El Salvador',
    'BELICE': 'Belize',
    'BELICEÑA': 'Belize',
    'BELICE�A': 'Belize',
    'Belizean': 'Belize',
    'Belizeean': 'Belize',

    # Caribe
    'CUBA': 'Cuba',
    'Cubano': 'Cuba',
    'Cubana': 'Cuba',
    'Cuban': 'Cuba',
    'Cubans': 'Cuba',
    'HAITI': 'Haiti',
    'Hait�': 'Haiti',
    'Haitiano': 'Haiti',
    'Haitiana': 'Haiti',
    'Haitian': 'Haiti',
    'Haitians': 'Haiti',
    'JAMAICA': 'Jamaica',
    'Jamaican': 'Jamaica',
    'Jamaicans': 'Jamaica',

    # China
    'CHINA': 'China',
    'Chino': 'China',
    'Chines': 'China',
    'chiness': 'China',
    'Chinese': 'China',
    'Chine': 'China',
    'Cina Popolare': 'China',
    'China, Taiwan Province of China': 'Taiwan',
    'China, Hong Kong SAR': 'Hong Kong',
    'China, Hong Kong Special Administrative Region': 'Hong Kong',
    'TAIWAN': 'Taiwan',
    'Taiwan': 'Taiwan',
    'Taiwanese': 'Taiwan',

    # India
    'INDIA': 'India',
    'Inde': 'India',
    'Indian': 'India',
    'Mumbai, India': 'India',

    # Filipinas
    'FILIPINAS': 'Philippines',
    'PHILIPPINES': 'Philippines',
    'Filippino': 'Philippines',
    'Filipino': 'Philippines',
    'Philippine': 'Philippines',
    'Filippine': 'Philippines',

    # Tailandia
    'TAILANDIA': 'Thailand',
    'THAILAND': 'Thailand',
    'THAILANDE': 'Thailand',
    'Tailandesa': 'Thailand',
    'Thai': 'Thailand',

    # Vietnam
    'VIETNAM': 'Vietnam',
    'Viet Nam': 'Vietnam',
    'Vietnam': 'Vietnam',
    'Vietnamita': 'Vietnam',
    'Vietnamese': 'Vietnam',
    'vietnamese': 'Vietnam',

    # Otros países asiáticos
    'BANGLADESH': 'Bangladesh',
    'Bangladeshi': 'Bangladesh',
    'CAMBODIA': 'Cambodia',
    'CAMBOYA': 'Cambodia',
    'Cambodia': 'Cambodia',
    'Cambodian': 'Cambodia',
    'INDONESIA': 'Indonesia',
    'Indonesian': 'Indonesia',
    'LAOS': 'Laos',
    'Laos': 'Laos',
    'Laotian': 'Laos',
    "Lao People's Democratic Republic": 'Laos',
    'MALAYSIA': 'Malaysia',
    'Malaysian': 'Malaysia',
    'MONGOLIA': 'Mongolia',
    'Mongolia': 'Mongolia',
    'Mongolian': 'Mongolia',
    'MYANMAR': 'Myanmar',
    'Myanmar': 'Myanmar',
    'MyanMar': 'Myanmar',
    'Burmese': 'Myanmar',
    'Domestic (Myanmar)': 'Myanmar',
    'NEPAL': 'Nepal',
    'Nepalese': 'Nepal',
    'SINGAPORE': 'Singapore',
    'SINGAPUR': 'Singapore',
    'Singapore': 'Singapore',
    'Singaporean': 'Singapore',
    'UZBEKISTAN': 'Uzbekistan',
    'Uzbecki': 'Uzbekistan',
    'Republic of Korea': 'South Korea',
    'COREA DEL SUR': 'South Korea',
    'Corea del Sur': 'South Korea',
    'South Korean': 'South Korea',
    "Democratic People's Republic of Korea": 'North Korea',
    'North Korean': 'North Korea',
    'JAPAN': 'Japan',
    'Japan': 'Japan',
    'Japanese': 'Japan',

    # Países del Medio Oriente
    'SYRIA': 'Syria',
    'SIRIA': 'Syria',
    'Syria': 'Syria',
    'Siria': 'Syria',
    'Syrian Arab Republic': 'Syria',
    'Syrian': 'Syria',
    'IRAQ': 'Iraq',
    'Iranian': 'Iran',
    'Iran (Islamic Republic of)': 'Iran',
    'ISRAEL': 'Israel',
    'Israeli': 'Israel',
    'Israelian': 'Israel',
    'LEBANON': 'Lebanon',
    'Lebanon': 'Lebanon',
    'Libanon': 'Lebanon',
    'Lebanese': 'Lebanon',
    'KUWAIT': 'Kuwait',
    'Kuwait': 'Kuwait',
    'QATAR': 'Qatar',
    'Qatar': 'Qatar',
    'Qatari': 'Qatar',
    'OMAN': 'Oman',
    'Oman': 'Oman',
    'Omani': 'Oman',
    'United Arab Emirates': 'UAE',
    'UAE': 'UAE',
    'Emirati (UAE)': 'UAE',
    'Saudi Arabia': 'Saudi Arabia',
    'Saudi': 'Saudi Arabia',
    'Yemen': 'Yemen',
    'Yemeni': 'Yemen',
    'Jordan': 'Jordan',
    'Jordanian': 'Jordan',
    'State of Palestine': 'Palestine',
    'Palestine': 'Palestine',
    'Palestinian Authority': 'Palestine',
    'Turkey': 'Turkey',
    'T�rkiye': 'Turkey',
    'Turqu�a': 'Turkey',
    'Turkish': 'Turkey',

    # Países africanos
    'NIGERIA': 'Nigeria',
    'Nigerian': 'Nigeria',
    'Nigerians': 'Nigeria',
    'NIGERIANA': 'Nigeria',
    'Nigerin': 'Nigeria',
    'GHANA': 'Ghana',
    'Ghana': 'Ghana',
    'Gana': 'Ghana',
    'ghana': 'Ghana',
    'Ghanaian': 'Ghana',
    'Ghanean': 'Ghana',
    'SOUTH AFRICA': 'South Africa',
    'South Africa': 'South Africa',
    'Sudafrica': 'South Africa',
    'South African': 'South Africa',
    'EGYPT': 'Egypt',
    'EGYBT': 'Egypt',
    'Egypt': 'Egypt',
    'Egitto': 'Egypt',
    'Egyptian': 'Egypt',
    'ETHIOPIA': 'Ethiopia',
    'Ethiopia': 'Ethiopia',
    'Etiopia': 'Ethiopia',
    'Ethopia': 'Ethiopia',
    'Ethiopian': 'Ethiopia',
    'UGANDA': 'Uganda',
    'Uganda': 'Uganda',
    'Ugandan': 'Uganda',
    'Ugandean': 'Uganda',
    'KENYA': 'Kenya',
    'Kenya': 'Kenya',
    'Keniano': 'Kenya',
    'Kenyan': 'Kenya',
    'TANZANIA': 'Tanzania',
    'Tanzania': 'Tanzania',
    'United Republic of Tanzania': 'Tanzania',
    'Tanzanian': 'Tanzania',
    'TANZANIANS': 'Tanzania',
    'TAZANIANS': 'Tanzania',
    'RWANDA': 'Rwanda',
    'Rwanda': 'Rwanda',
    'Rwandean': 'Rwanda',
    'BURUNDI': 'Burundi',
    'Burundi': 'Burundi',
    'Burundean': 'Burundi',
    'BURUNDIANS': 'Burundi',
    'MOROCCO': 'Morocco',
    'Morocco': 'Morocco',
    'Marruecos': 'Morocco',
    'MARRUECOS': 'Morocco',
    'Marocco': 'Morocco',
    'Moroccan': 'Morocco',
    'Marroquie': 'Morocco',
    'TUNISIA': 'Tunisia',
    'Tunisia': 'Tunisia',
    'Tunisa': 'Tunisia',
    'Tunisie': 'Tunisia',
    'ALGERIA': 'Algeria',
    'Algerians': 'Algeria',
    'LIBYA': 'Libya',
    'Libya': 'Libya',
    'Lybia': 'Libya',
    'Lybians': 'Libya',
    'SUDAN': 'Sudan',
    'Sudan': 'Sudan',
    'Sudanese': 'Sudan',
    'South Sudan': 'South Sudan',
    'ERITREA': 'Eritrea',
    'Eritrea': 'Eritrea',
    'Eritrej': 'Eritrea',
    'Eritrean': 'Eritrea',
    'Erithera': 'Eritrea',
    'SOMALIA': 'Somalia',
    'Somalia': 'Somalia',
    'Somali': 'Somalia',
    'ZIMBABWE': 'Zimbabwe',
    'Zimbabwe': 'Zimbabwe',
    'Zimbabwean': 'Zimbabwe',
    'ZAMBIA': 'Zambia',
    'Zambia': 'Zambia',
    'Zambian': 'Zambia',
    'BOTSWANA': 'Botswana',
    'Botswana': 'Botswana',
    'Botzwana': 'Botswana',
    'MALI': 'Mali',
    'Mali': 'Mali',
    'Malian': 'Mali',
    'NIGER': 'Niger',
    'Niger': 'Niger',
    'Niger Rep': 'Niger',
    'BURKINA FASO': 'Burkina Faso',
    'Burkina Faso': 'Burkina Faso',
    'Burkinabe': 'Burkina Faso',
    'BENIN': 'Benin',
    'Benin': 'Benin',
    'Benin Rep': 'Benin',
    'Beninoise': 'Benin',
    'TOGO': 'Togo',
    'Togo': 'Togo',
    'Togolese': 'Togo',
    'GUINEA': 'Guinea',
    'GUINEE': 'Guinea',
    'Guinea': 'Guinea',
    'GUINEE CONAKRY': 'Guinea',
    'Guinea Conakry': 'Guinea',
    'GUINEANA': 'Guinea',
    'Guinean': 'Guinea',
    'SIERRA LEONE': 'Sierra Leone',
    'Sierra Leone': 'Sierra Leone',
    'Sierra leone': 'Sierra Leone',
    'Sierra Leonean': 'Sierra Leone',
    'LIBERIA': 'Liberia',
    'Liberia': 'Liberia',
    'Liberian': 'Liberia',
    "COTE D'IVOIRE": "Cote d'Ivoire",
    "Cote d'Ivoire": "Cote d'Ivoire",
    "Cote d'ivoire": "Cote d'Ivoire",
    "Costa d'Avorio": "Cote d'Ivoire",
    'C�te d�Ivoire': "Cote d'Ivoire",
    'Ivory Coast': "Cote d'Ivoire",
    'Czech Rep': "Cote d'Ivoire",
    'SENEGAL': 'Senegal',
    'Senegal': 'Senegal',
    'Senegalese': 'Senegal',
    'GAMBIA': 'Gambia',
    'Gambia': 'Gambia',
    'Gambian': 'Gambia',
    'MAURITANIA': 'Mauritania',
    'Mauritania': 'Mauritania',
    'Mauritanian': 'Mauritania',
    'MAURITIUS': 'Mauritius',
    'Mauritius': 'Mauritius',
    'MADAGASCAR': 'Madagascar',
    'Madagascar': 'Madagascar',
    'CAMEROON': 'Cameroon',
    'Cameroon': 'Cameroon',
    'Cameroun': 'Cameroon',
    'Cameroonian': 'Cameroon',
    'CHAD': 'Chad',
    'Chad': 'Chad',
    'Chadian': 'Chad',
    'GABON': 'Gabon',
    'Gabon': 'Gabon',
    'CAR': 'Central African Republic',
    'Centrel African Republic': 'Central African Republic',
    'Congo': 'Democratic Republic of the Congo',
    'Democratic Republic of the Congo': 'Democratic Republic of the Congo',
    'RDC': 'Democratic Republic of the Congo',
    'Congolese (DRC)': 'Democratic Republic of the Congo',
    'Dr Kongo': 'Democratic Republic of the Congo',
    'Democratic Kongo': 'Democratic Republic of the Congo',
    'Angola': 'Angola',
    'Angolan': 'Angola',
    'Angolans': 'Angola',
    'Cabo Verde': 'Cape Verde',
    'Cape Ver': 'Cape Verde',
    'Sao Tome': 'Sao Tome and Principe',
    'Equatorial Guinea': 'Equatorial Guinea',
    'Guinea-Bissau': 'Guinea-Bissau',
    'Comoros': 'Comoros',
    'Comorian islands': 'Comoros',
    'Seychelles': 'Seychelles',
    'Djibouti': 'Djibouti',
    'Djiboutean': 'Djibouti',
    'Swaziland': 'Eswatini',
    'Swasiland': 'Eswatini',
    'Lesotho': 'Lesotho',
    'Malawi': 'Malawi',
    'Mozambique': 'Mozambique',
    'Namibia': 'Namibia',
    'Western Sahara': 'Western Sahara',

    # Países europeos
    'ALEMANIA': 'Germany',
    'GERMANY': 'Germany',
    'Germany': 'Germany',
    'Germans': 'Germany',
    'German': 'Germany',
    'FRANCE': 'France',
    'FRANCIA': 'France',
    'France': 'France',
    'French': 'France',
    'ITALY': 'Italy',
    'ITALIA': 'Italy',
    'Italy': 'Italy',
    'Italian': 'Italy',
    'UK': 'United Kingdom',
    'United Kingdom': 'United Kingdom',
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'Great Britain': 'United Kingdom',
    'NETHERLANDS': 'Netherlands',
    'Netherlands': 'Netherlands',
    'HOLANDA': 'Netherlands',
    'Nederland': 'Netherlands',
    'the Netherlands': 'Netherlands',
    'The Netherlands': 'Netherlands',
    'Netherlands (own country)': 'Netherlands',
    'Dutch': 'Netherlands',
    'NORWAY': 'Norway',
    'NORUEGA': 'Norway',
    'Norway': 'Norway',
    'Norvegian': 'Norway',
    'SWEDEN': 'Sweden',
    'Sweden': 'Sweden',
    'Sweeden': 'Sweden',
    'Swedesh': 'Sweden',
    'DENMARK': 'Denmark',
    'Denmark': 'Denmark',
    'Danish': 'Denmark',
    'FINLAND': 'Finland',
    'Finland': 'Finland',
    'Finns': 'Finland',
    'ICELAND': 'Iceland',
    'Iceland': 'Iceland',
    'SWITZERLAND': 'Switzerland',
    'SUIZA': 'Switzerland',
    'Switzerland': 'Switzerland',
    'AUSTRIA': 'Austria',
    'Austria': 'Austria',
    'Austrians': 'Austria',
    'PORTUGAL': 'Portugal',
    'Portugal': 'Portugal',
    'Portuguese': 'Portugal',
    'POLAND': 'Poland',
    'POLONIA': 'Poland',
    'Poland': 'Poland',
    'Poles': 'Poland',
    'Polish': 'Poland',
    'CZECH REPUBLIC': 'Czech Republic',
    'REPÚBLICA CHECA': 'Czech Republic',
    'République tchèque': 'Czech Republic',
    'Czechia': 'Czech Republic',
    'Czech': 'Czech Republic',
    'Czeck Republic': 'Czech Republic',
    'SLOVAKIA': 'Slovakia',
    'Slovakia': 'Slovakia',
    'Slovaks': 'Slovakia',
    'Slovak': 'Slovakia',
    'SLOVENIA': 'Slovenia',
    'Slovenia': 'Slovenia',
    'Slovenian': 'Slovenia',
    'HUNGARY': 'Hungary',
    'HUNGRÍA': 'Hungary',
    'Hungary': 'Hungary',
    'Hongrie': 'Hungary',
    'Hungarians': 'Hungary',
    'Hungarian': 'Hungary',
    'ROMANIA': 'Romania',
    'RUMANÍA': 'Romania',
    'Romania': 'Romania',
    'Rumania': 'Romania',
    'Roumanie': 'Romania',
    'Romanian': 'Romania',
    'BULGARIA': 'Bulgaria',
    'Bulgaria': 'Bulgaria',
    'Bulgarian': 'Bulgaria',
    'CROATIA': 'Croatia',
    'Croatia': 'Croatia',
    'croatia': 'Croatia',
    'Croazia': 'Croatia',
    'Croatian': 'Croatia',
    'SERBIA': 'Serbia',
    'Serbia': 'Serbia',
    'Serbian': 'Serbia',
    'Serbians': 'Serbia',
    'Bosnia and Herzegovina': 'Bosnia and Herzegovina',
    'Bosnia i Herzegovinia': 'Bosnia and Herzegovina',
    'Bosnia Erzegovina': 'Bosnia and Herzegovina',
    'Bosnia': 'Bosnia and Herzegovina',
    'Bosnian': 'Bosnia and Herzegovina',
    'ALBANIA': 'Albania',
    'Albania': 'Albania',
    'Abania': 'Albania',
    'Albanie': 'Albania',
    'Albanian': 'Albania',
    'albanian': 'Albania',
    'Albanians': 'Albania',
    'MONTENEGRO': 'Montenegro',
    'Montenegro': 'Montenegro',
    'North Macedonia': 'North Macedonia',
    'The former Yugoslav Republic of Macedonia': 'North Macedonia',
    'Macedonian': 'North Macedonia',
    'Kosovo': 'Kosovo',
    'Kosovo under UNSCR 1244': 'Kosovo',
    'Kosovar': 'Kosovo',
    'MOLDOVA': 'Moldova',
    'MOLDAVIA': 'Moldova',
    'Moldova': 'Moldova',
    'Moldavia': 'Moldova',
    'Republic of Moldova': 'Moldova',
    'République de Moldavie': 'Moldova',
    'Moldovan': 'Moldova',
    'Moldavian': 'Moldova',
    'Moldovian': 'Moldova',
    'UKRAINE': 'Ukraine',
    'UCRANIA': 'Ukraine',
    'Ukraine': 'Ukraine',
    'The Ukraine': 'Ukraine',
    'Ukrainian': 'Ukraine',
    'Ukranian': 'Ukraine',
    'Ukraineans': 'Ukraine',
    'Ukrainian national repatriated from Slovakia to Ukraine': 'Ukraine',
    'RUSSIA': 'Russia',
    'RUSIA': 'Russia',
    'Russia': 'Russia',
    'Russian Federation': 'Russia',
    'Russian': 'Russia',
    'BELARUS': 'Belarus',
    'BIELORRUSIA': 'Belarus',
    'Belarus': 'Belarus',
    'Byelorussian': 'Belarus',
    'LITHUANIA': 'Lithuania',
    'Lithuania': 'Lithuania',
    'Lithuanian': 'Lithuania',
    'LATVIA': 'Latvia',
    'Latvia': 'Latvia',
    'Latvian': 'Latvia',
    'ESTONIA': 'Estonia',
    'Estonia': 'Estonia',
    'Estonians': 'Estonia',
    'GREECE': 'Greece',
    'Greece': 'Greece',
    'Greek': 'Greece',
    'CYPRUS': 'Cyprus',
    'Cyprus': 'Cyprus',
    'MALTA': 'Malta',
    'Malta': 'Malta',
    'Maltese': 'Malta',
    'LUXEMBOURG': 'Luxembourg',
    'Luxembourg': 'Luxembourg',
    'IRELAND': 'Ireland',
    'Ireland': 'Ireland',
    'BELGIUM': 'Belgium',
    'Belgium': 'Belgium',
    'Belga': 'Belgium',
    'Former Yugoslavia': 'Former Yugoslavia',
    'B & H': 'Bosnia and Herzegovina',

    # Países de Asia Central
    'KAZAKHSTAN': 'Kazakhstan',
    'Kazakhstan': 'Kazakhstan',
    'Kazalhstan': 'Kazakhstan',
    'Kazahstan': 'Kazakhstan',
    'Kazakhistan': 'Kazakhstan',
    'Kazaki': 'Kazakhstan',
    'KYRGYZSTAN': 'Kyrgyzstan',
    'Kyrgyzstan': 'Kyrgyzstan',
    'Kyrgysi': 'Kyrgyzstan',
    'TAJIKISTAN': 'Tajikistan',
    'Tajikistan': 'Tajikistan',
    'Tajiki': 'Tajikistan',
    'TURKMENISTAN': 'Turkmenistan',
    'Turkmenistan': 'Turkmenistan',
    'Turkmeni': 'Turkmenistan',
    'AZERBAIJAN': 'Azerbaijan',
    'Azerbaijan': 'Azerbaijan',
    'Azerbaijani': 'Azerbaijan',
    'ARMENIA': 'Armenia',
    'Armenia': 'Armenia',
    'Armenians': 'Armenia',
    'GEORGIA': 'Georgia',
    'Georgia': 'Georgia',
    'Georgian': 'Georgia',

    # Países de Oceanía
    'AUSTRALIA': 'Australia',
    'Australia': 'Australia',
    'Australians': 'Australia',
    'NEW ZEALAND': 'New Zealand',
    'New Zealand': 'New Zealand',
    'New Zealander': 'New Zealand',
    'FIJI': 'Fiji',
    'Fiji': 'Fiji',
    'Fijian': 'Fiji',
    'PAPUA NEW GUINEA': 'Papua New Guinea',
    'Papua New Guinea': 'Papua New Guinea',
    'Solomon Islands': 'Solomon Islands',
    'solomon islands': 'Solomon Islands',
    'Solomon islanders': 'Solomon Islands',
    'Solomon Isands': 'Solomon Islands',
    'Samoa': 'Samoa',
    'Vanuatu': 'Vanuatu',
    'Tonga': 'Tonga',
    'Palau': 'Palau',
    'Maldives': 'Maldives',

    # Otros países
    'CANADA': 'Canada',
    'Canada': 'Canada',
    'Canadians': 'Canada',
    'BARBADOS': 'Barbados',
    'Barbados': 'Barbados',
    'Trinidad and Tobago': 'Trinidad and Tobago',
    'Saint Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
    'St Vincent': 'Saint Vincent and the Grenadines',
    'Guyana': 'Guyana',
    'Guayanean': 'Guyana',
    'Suriname': 'Suriname',
    'French Guiana': 'French Guiana',
    'Timor-Leste': 'Timor-Leste',
    'Timor Este': 'Timor-Leste',
    'Bhutan': 'Bhutan',
    'Bhutanese': 'Bhutan',
    'Bhuatnese': 'Bhutan',
    'Sri Lanka': 'Sri Lanka',
    'SRI LANKA': 'Sri Lanka',
    'Sri lanka': 'Sri Lanka',
    'Sri Lankan': 'Sri Lanka',
    'Afghanistan': 'Afghanistan',
    'Afganistan': 'Afghanistan',
    'Afghani': 'Afghanistan',
    'Pakistan': 'Pakistan',
    'PAKISTÁN': 'Pakistan',
    'Pakistani': 'Pakistan',

    # Valores a eliminar o categorizar
    'Unknown': 'Unknown',
    'Desconocido': 'Unknown',
    'DESCONOCIDA': 'Unknown',
    'NO DETERMINADA': 'Unknown',
    'No Determinado': 'Unknown',
    'NO DETERMINADAS': 'Unknown',
    'NO REGISTRA': 'Unknown',
    'Sin determinar': 'Unknown',
    'without': 'Unknown',
    'Disputed': 'Unknown',
    'Nationality': 'Unknown',
    '0': 'Unknown',
    '145': 'Unknown',
    'TOTAL': 'Unknown',
    'TOTAL POR AÑO': 'Unknown',
    'RMI': 'Unknown',

    # Categorías regionales
    'Abroad': 'Abroad',
    'Nationals': 'Nationals',
    'Ciudadanos de su país': 'Nationals',
    'Personnes de nationalité étrangère': 'Foreign Nationals',
    'Africa': 'Africa',
    'Americas': 'Americas',
    'Amercias': 'Americas',
    'Asia': 'Asia',
    'European Economic Area': 'European Economic Area',
    'Africa and Middle East': 'Africa and Middle East',
    'Other Asia': 'Other Asia',
    'Other Central America and Caribbean': 'Other Central America and Caribbean',
    'Other Central America and Car': 'Other Central America and Caribbean',
    'Caribbean (Trinidad and Tobago, Barbados, etc)': 'Caribbean',
    'Other Countries (Dominica, Panama, French Guiana, Brazil, etc.)': 'Other Countries',

    # Tipos de explotación
    'Sexual exploitation': 'Sexual exploitation',
    'Forced labour': 'Forced labour',
    'Other forms of exploitation': 'Other forms of exploitation',
    'Personnes de nationalit� �trang�re': 'foreign',
    'Boliviana': 'Bolivia',
    'Colombiana': 'Colombia',
    'Paraguaya': 'Paraguay',
    'Venezolana': 'Venezuela',
    'Timor-Leste': 'Timor-Leste',
    "C�TE D'IVOIRE": "Côte d'Ivoire",
    'Oman': 'Oman',
    'Qatar': 'Qatar',
    'BAHAMAS': 'Bahamas',
    '(especifique el pa�s)': 'Unknown',
    'Ciudadanos de su pa�s': 'Unknown',
    'Argentina': 'Argentina',
    'Brasil': 'Brazil',
    'Venezuela (Bolivarian Republic of)': 'Venezuela',
    'Bolivia (Plurinational State of)': 'Bolivia',
    # Especificaciones
    '(especifique el país)': 'nan',
    '(especifique otras nacionalidades)': '(specify other nationalities)',
    '(especifique el país)': '(specify the country)',
    '(Nationality not stated)': '(Nationality not stated)',
    '(Oman)': 'Oman',
    '(Lebanon)': 'Lebanon',
    '(Senegal)': 'Senegal',
    'Kurdistan, Iraq': 'Kurdistan, Iraq',
    'Dubai': 'UAE',
    'OTROS': 'Others',
    'Total': 'Unknown',
}


# In[31]:


df1['Category'] = df['Category'].replace(corrections)


# In[32]:


df1['Category'].unique()


# In[33]:


display(df1)


# In[34]:


display(df1.head())


# In[35]:


df1.to_csv('clean.csv', index=False)


# In[36]:


display(df1.iloc[1053],df1.iloc[1054],df1.iloc[1055 ])


# In[37]:


df1_region = df1[['Region']].reset_index(drop=True)
unique_regions = df1["Region"].unique()
unique_regions_df = pd.DataFrame({"Region_id": [i+1 for i in range(len(unique_regions))], "Region": unique_regions})
unique_regions_df.to_csv("../data/clean/unique_regions.csv", index=False, encoding="utf-8")
unique_regions_df
#df1_region['Region_id'] = df1_region.index + 1


# In[38]:


unique_subregions = df1["Subregion"].unique()
unique_subregions_df = pd.DataFrame({"Subregion_id": [i+1 for i in range(len(unique_subregions))], "Subregion": unique_subregions})
unique_subregions_df.to_csv("../data/clean/unique_subregions.csv", index=False, encoding="utf-8")
unique_subregions_df


# In[39]:


display(df1_region)


# In[40]:


df1_region.to_csv('region.csv', index=False)


# In[42]:


# Crear df1_Subregion con columnas seleccionadas
df1_Subregion = df1[['Subregion', 'Region']].reset_index(drop=True)

# Mostrar ejemplos
display(df1_Subregion.head())


# Combinar con unique_regions_df
df1_Subregion_new2 = df1_Subregion.merge(unique_regions_df, on='Region', how="left")
display(df1_Subregion_new2)

# Renombrar columnas correctamente
df1_Subregion = df1_Subregion.rename(columns={'Subregion': 'Subregion_name'})

# Asignar Subregion_id
df1_Subregion['Subregion_id'] = df1_Subregion.index + 1


# In[43]:


display(df1_Subregion)


# In[44]:


df1_Subregion.to_csv('Subregion.csv', index=False)


# In[45]:


df_country = df1[['Country', 'Subregion']].drop_duplicates().reset_index(drop=True)
df_country = df_country.merge(unique_subregions_df, on='Subregion', how='left')
df_country.insert(0, 'Country_id', range(1, len(df_country) + 1))
df_country = df_country.rename(columns={'Country': 'Country_name'})
df_country.to_csv("../data/clean/unique_countries.csv", index=False, encoding="utf-8")

df_country.head()


# In[46]:


df_victim = df1[['Sex', 'Age']].drop_duplicates().reset_index(drop=True)

# Asign IDs
df_victim.insert(0, 'Victim_id', range(1, len(df_victim) + 1))

# Export
df_victim.to_csv("../data/clean/victims.csv", index=False, encoding="utf-8")

df_victim.head()


# In[47]:


df_offense = df1.merge(df_country[['Country_name', 'Country_id']], left_on='Country', right_on='Country_name', how='left')


df_offense = df_offense.merge(df_victim, on=['Sex', 'Age'], how='left')


df_offense = df_offense[['Year', 'Dimension', 'Category', 'Nr_of_victims', 'Country_id', 'Victim_id']]


df_offense.insert(0, 'Offense_id', range(1, len(df_offense) + 1))


df_offense.to_csv("../data/clean/offenses.csv", index=False, encoding="utf-8")

df_offense.head()


# In[48]:


df2 = df1[df1['Dimension'] == 'by form of exploitation'].copy()
display(df2.head())


# In[ ]:




