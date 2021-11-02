from json import JSONDecodeError

from hawfinch import Hawfinch

countries = [
    {"name": "Algeria", "ref": "3600192756"},
    {"name": "Angola", "ref": "3600195267"},
    {"name": "Benin", "ref": "3600192784"},
    {"name": "Botswana", "ref": "3601889339"},
    {"name": "Burkina Faso", "ref": "3600192783"},
    {"name": "Burundi", "ref": "3600195269"},
    {"name": "Cameroon", "ref": "3600192830"},
    {"name": "Cape Verde", "ref": "3600535774"},
    {"name": "Central African Republic", "ref": "3600192790"},
    {"name": "Chad", "ref": "3602361304"},
    {"name": "Comoros", "ref": "3600535790"},
    {"name": "Côte d'Ivoire", "ref": "3600192779"},
    {"name": "Democratic Republic of the Congo Congo", "ref": "3602237396"},
    {"name": "Djibouti", "ref": "3600192801"},
    {"name": "Egypt", "ref": "3601473947"},
    {"name": "Equatorial Guinea", "ref": "3600192791"},
    {"name": "Eritrea", "ref": "3600296961"},
    {"name": "Ethiopia", "ref": "3600192800"},
    {"name": "Gabon", "ref": "3600192793"},
    {"name": "Ghana", "ref": "3600192781"},
    {"name": "Guinea", "ref": "3600192778"},
    {"name": "Guinea-Bissau", "ref": "3600192776"},
    {"name": "Kenya", "ref": "3600192798"},
    {"name": "Lesotho", "ref": "3602093234"},
    {"name": "Liberia", "ref": "3600192780"},
    {"name": "Libya", "ref": "3600192758"},
    {"name": "Madagascar", "ref": "3600447325"},
    {"name": "Malawi", "ref": "3600195290"},
    {"name": "Mali", "ref": "3600192785"},
    {"name": "Mauritania", "ref": "3600192763"},
    {"name": "Mauritius", "ref": "3600535828"},
    {"name": "Mayotte", "ref": "3603388394"},
    {"name": "Morocco", "ref": "3603630439"},
    {"name": "Mozambique", "ref": "3600195273"},
    {"name": "Namibia", "ref": "3600195266"},
    {"name": "Niger", "ref": "3600192786"},
    {"name": "Nigeria", "ref": "3600192787"},
    {"name": "Republic of the Congo Congo-Brazzaville", "ref": "3600192794"},
    {"name": "Réunion", "ref": "3600077601"},
    {"name": "Rwanda", "ref": "3600171496"},
    {"name": "Saint Helena", "ref": "3604868269"},
    {"name": "São Tomé and Príncipe", "ref": "3600535880"},
    {"name": "Senegal", "ref": "3600192775"},
    {"name": "Seychelles", "ref": "3600536765"},
    {"name": "Sierra Leone", "ref": "3600192777"},
    {"name": "Somalia", "ref": "3600192799"},
    {"name": "South Africa", "ref": "3600087565"},
    {"name": "Sudan", "ref": "3600192789"},
    {"name": "Swaziland", "ref": "3600088210"},
    {"name": "Tanzania", "ref": "3600195270"},
    {"name": "The Gambia", "ref": "3600192774"},
    {"name": "Togo", "ref": "3600192782"},
    {"name": "Tunisia", "ref": "3600192757"},
    {"name": "Uganda", "ref": "3600192796"},
    {"name": "Zambia", "ref": "3600195271"},
    {"name": "Zimbabwe", "ref": "3600195272"}
]

tags = [
    {
        'type': 'amenity',
        'name': 'atm'
    },
    {'type': 'amenity',
     'name': 'bar'
     },
    {'type': 'amenity',
     'name': 'cafe'
     },
    {'type': 'amenity',
     'name': 'fast_food'
     },
    {'type': 'amenity',
     'name': 'food_court'
     },
    {'type': 'amenity',
     'name': 'restaurant'
     },
    {'type': 'amenity',
     'name': 'college'
     },
    {'type': 'amenity',
     'name': 'driving_school'
     },
    # {'type': 'amenity',
    #  'name': 'kindergarten'
    #  },
    {'type': 'amenity',
     'name': 'library'
     },
    {'type': 'amenity',
     'name': 'school'
     },
    {'type': 'amenity',
     'name': 'university'
     },
    {'type': 'amenity',
     'name': 'car_wash'
     },
    {'type': 'amenity',
     'name': 'fuel'
     },
    {'type': 'amenity',
     'name': 'bank'
     },
    {'type': 'amenity',
     'name': 'clinic'
     },
    {'type': 'amenity',
     'name': 'dentist'
     },
    {'type': 'amenity',
     'name': 'doctors'
     },
    {'type': 'amenity',
     'name': 'hospital'
     },
    {'type': 'amenity',
     'name': 'nursing_home'
     },
    {'type': 'amenity',
     'name': 'pharmacy'
     },
    {'type': 'amenity',
     'name': 'veterinary'
     },
    {'type': 'amenity',
     'name': 'courthouse'
     },
    {'type': 'amenity',
     'name': 'embassy'
     },
    {'type': 'office',
     'name': 'diplomatic'
     },
    {'type': 'amenity',
     'name': 'fire_station'
     },
    {'type': 'amenity',
     'name': 'police'
     },
    {'type': 'amenity',
     'name': 'post_box'
     },
    {'type': 'amenity',
     'name': 'post_depot'
     },
    {'type': 'amenity',
     'name': 'townhall'
     },
    {'type': 'amenity',
     'name': 'marketplace'
     },
    {'type': 'amenity',
     'name': 'place_of_worship',
     'religion': 'christian',
     'save_as': 'church'
     },
    {'type': 'amenity',
     'name': 'place_of_worship',
     'religion': 'muslim',
     'save_as': 'church'
     },
    {'type': 'leisure',
     'name': 'fitness_centre'
     },
    {'type': 'leisure',
     'name': 'sports_centre'
     },
    {'type': 'office',
     'name': 'government'
     },
]

if __name__ == '__main__':
    for country in countries:
        for amenity in tags:
            try:
                Hawfinch.get(country=country, amenity=amenity, should_save=True)
            except KeyboardInterrupt:
                print('You cancelled the operation')
                continue
            except JSONDecodeError:
                print('Caught JSONDecodeError')
                continue
