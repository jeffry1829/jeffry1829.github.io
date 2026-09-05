from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_tnt',
        {
            'title': '壞想法',
            'desc': '製造的TNT數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:tnt'])
    ))
