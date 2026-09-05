from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'breed',
        {
            'title': '牧場主',
            'desc': '繁殖的動物數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:animals_bred'])
    ))
