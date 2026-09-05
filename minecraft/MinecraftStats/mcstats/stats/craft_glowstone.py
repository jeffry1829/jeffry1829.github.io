from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_glowstone',
        {
            'title': '光線師',
            'desc': '製造的螢光石數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:glowstone']),
    ))
