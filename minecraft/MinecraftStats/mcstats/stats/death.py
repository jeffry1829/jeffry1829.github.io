from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'death',
        {
            'title': '旅鼠',
            'desc': '死過的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:deaths'])
    ))
