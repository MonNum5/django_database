import random
import string
import json

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def dummy_crc():
    dict = {
            "header": {
                "name": randomString(stringLength=8),
                "fuel_ID": randomString(stringLength=8),
                "description": randomString(stringLength=8),
                "country": randomString(stringLength=8),
                "city": randomString(stringLength=8),
                "blend": randomString(stringLength=8),
                "author": randomString(stringLength=8),
                "timestamp": "2020-03-20 11:28:09",
                "version": "2-0-0",
                "main_source": {
                    "file": randomString(stringLength=8),
                    "page": 1,
                    "original_fuel_ID": randomString(stringLength=8),
                    "GCxGC_file": randomString(stringLength=8)
                },
                "fuel_type": "JetA",
                "project": randomString(stringLength=8)
            },
        "composition": {
        "saturates": [
            {
                "test_method": "D1319",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "monoaromatics": [
            {
                "test_method": "D6379",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "diaromatics": [
            {
                "test_method": "D6379",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "aromatics_total": [
            {
                "test_method": "D6379",
                "unit": "vol%",
                "value": random.uniform(0,100)
            },
            {
                "test_method": "D1319",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "saturates_total": [
            {
                "test_method": "D6379",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "benzene": [
            {
                "test_method": "GC/MS",
                "unit": "ug/ml",
                "value": random.uniform(0,100)
            }
        ],
        "naphthalene": [
            {
                "test_method": "GC/MS",
                "unit": "ug/ml",
                "value": random.uniform(0,100)
            },
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "cycloparaffins": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "dicycloparaffins": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "tricycloparaffins": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "alkylbenzenes": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "indan_and_teralins": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "indenes_CnH2n-10": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "naphthalenes": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            },
            {
                "test_method": "D1840",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "acenaphthenes": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "acenaphthylenes": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "sulfur_mercaptan": [
            {
                "test_method": "D3227",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "thiols_sulfides_disulfides": [
            {
                "test_method": "",
                "unit": "ppm-m",
                "value": random.uniform(0,100)
            }
        ],
        "thiophenes": [
            {
                "test_method": "",
                "unit": "ppm-m",
                "value": random.uniform(0,100)
            }
        ],
        "benzothiophenes": [
            {
                "test_method": "",
                "unit": "ppm-m",
                "value": random.uniform(0,100)
            }
        ],
        "dibenzothiophenes": [
            {
                "test_method": "",
                "unit": "ppm-m",
                "value": random.uniform(0,100)
            }
        ],
        "hydrogen_content": [
            {
                "test_method": "D3701",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "sulfur_total": [
            {
                "test_method": "D2622",
                "unit": "mass%",
                "value": random.uniform(0,100)
            },
            {
                "test_method": "",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "olefins_total": [
            {
                "test_method": "D1159",
                "unit": "vol%",
                "value": random.uniform(0,100)
            }
        ],
        "paraffins_total": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ],
        "tricycloaromatics": [
            {
                "test_method": "D2425",
                "unit": "mass%",
                "value": random.uniform(0,100)
            }
        ]
    },

    "property": {
        "density": [
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": -35.0
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": -18.4
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": -0.4
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": 19.8
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": 39.6
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": 69.4
            },
            {
                "test_method": "D4052",
                "unit": "kg/m3",
                "value": random.uniform(700,900),
                "temperature_unit": "C",
                "temperature_value": 15.5555555555556
            }
        ],
        "flash_point": [
            {
                "test_method": "D93",
                "unit": "C",
                "value": random.uniform(30,60)
            }
        ],
        "freezing_point": [
            {
                "test_method": "D5972",
                "unit": "C",
                "value": random.uniform(-90,-30)
            }
        ],
        "pour_point": [
            {
                "test_method": "D5949",
                "unit": "C",
                "value": random.uniform(-90,-30)
            }
        ],
        "viscosity_kinematic": [
            {
                "test_method": "D445",
                "unit": "mm2/s",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": 20.0
            },
            {
                "test_method": "D445",
                "unit": "mm2/s",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": -20.0
            },
            {
                "test_method": "D445",
                "unit": "mm2/s",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": -40.0
            }
        ],
        "electrical_conductivity": [
            {
                "test_method": "D2624",
                "unit": "pS/m",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": 5.555555555555543
            },
            {
                "test_method": "D2624",
                "unit": "pS/m",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": 22.222222222222285
            },
            {
                "test_method": "D2624",
                "unit": "pS/m",
                "value": random.uniform(0.2,20),
                "temperature_unit": "C",
                "temperature_value": 37.77777777777783
            }
        ],
        "distillation": [
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 0.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 0.0,
                "information": "test 2"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 10.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 10.0,
                "information": "test 2"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 20.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 20.0,
                "information": "test 2"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 50.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 50.0,
                "information": "test 2"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 90.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 90.0,
                "information": "test 2"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 100.0,
                "information": "test 1"
            },
            {
                "test_method": "D86",
                "unit": "C",
                "value": random.uniform(100,250),
                "volume_evaporated_unit": "%",
                "volume_evaporated_value": 100.0,
                "information": "test 2"
            }
        ],
        "distillation_residue": [
            {
                "test_method": "D1218",
                "unit": "vol%",
                "value": random.uniform(0,2),
                "information": "test 1"
            },
            {
                "test_method": "D1218",
                "unit": "vol%",
                "value": random.uniform(0,2),
                "information": "test 2"
            }
        ],
        "refractive_index": [
            {
                "test_method": "D1218",
                "unit": "-",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": 20.0
            }
        ],
        "net_heat_of_combustion": [
            {
                "test_method": "D4809",
                "unit": "MJ/kg",
                "value": random.uniform(41,45)
            }
        ],
        "net_heat_of_combustion_calculated": [
            {
                "test_method": "D3338",
                "unit": "MJ/kg",
                "value": random.uniform(41,45)
            }
        ],
        "specific_heat_capacitiy_slope": [
            {
                "test_method": "E1269",
                "unit": "J/gK",
                "value": random.uniform(41,45)
            }
        ],
        "specific_heat_capacity": [
            {
                "test_method": "E1269",
                "unit": "kJ/(kg*K)",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": -30.0
            },
            {
                "test_method": "E1269",
                "unit": "kJ/(kg*K)",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": 0.0
            },
            {
                "test_method": "E1269",
                "unit": "kJ/(kg*K)",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": 15.0
            },
            {
                "test_method": "E1269",
                "unit": "kJ/(kg*K)",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": 20.0
            },
            {
                "test_method": "E1269",
                "unit": "kJ/(kg*K)",
                "value": random.uniform(1,2),
                "temperature_unit": "C",
                "temperature_value": 140.0
            }
        ],
        "thermal_stability_breakpoint": [
            {
                "test_method": "D3241",
                "unit": "C",
                "value": random.uniform(250,300)
            }
        ],
        "lubricity_bocle": [
            {
                "test_method": "D5001",
                "unit": "mm",
                "value": random.uniform(0,1)
            }
        ],
        "surface_tension": [
            {
                "test_method": "D971",
                "unit": "mN/m",
                "value": random.uniform(20,27),
                "temperature_unit": "C",
                "temperature_value": 22.222222222222285
            },
            {
                "test_method": "D971",
                "unit": "mN/m",
                "value": random.uniform(20,27),
                "temperature_unit": "C",
                "temperature_value": -10.0
            },
            {
                "test_method": "D971",
                "unit": "mN/m",
                "value": random.uniform(20,27),
                "temperature_unit": "C",
                "temperature_value": 40.0
            }
        ],
        "dielectric_constant": [
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": -36.6
            },
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": -0.4
            },
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": -0.4
            },
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": 19.8
            },
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": 39.8
            },
            {
                "test_method": "K-Cell",
                "unit": "K",
                "value": random.uniform(1.8,3),
                "temperature_unit": "C",
                "temperature_value": 69.6
            }
        ],
        "speed_of_sound": [
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -35.0
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -18.4
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -18.4
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -0.4
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -35.0
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -18.4
            },
            {
                "test_method": "",
                "unit": "m/s",
                "value": random.uniform(1300,2000),
                "temperature_unit": "C",
                "temperature_value": -0.4
            }
        ],
        "acidity_total": [
            {
                "test_method": "D3242",
                "unit": "mg KOH/g",
                "value": random.uniform(0,1)
            }
        ],
        "visual": [
            {
                "test_method": "",
                "unit": "rating",
                "value": ()
            }
        ]
    },
    "change_log": {
        "2-0-0": {
            "Change": [
                randomString()
            ],
            "Timestamp": "31/10/2019, 13:47:30"
        },
        "1-0-0": [
            "-"
        ],
        "Timestamp": "-"
    }
}
        
    return dict

for i in range(0,200):
    dict = dummy_crc()
    name = randomString()

    # Serializing json  
    json_object = json.dumps(dict, indent = 4) 
  
    # Writing to sample.json 
    with open("DummyDB/"+name+".json", "w") as outfile: 
        outfile.write(json_object) 
