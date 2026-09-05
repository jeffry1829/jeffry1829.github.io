from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_compass',
        {
            'title': '指南專家',
            'desc': '製造的指南針數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:compass']),
    ))
