from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_beacon',
        {
            'title': '能量源',
            'desc': '造過的烽火臺數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:beacon']),
    ))
