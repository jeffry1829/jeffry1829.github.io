from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'jump',
        {
            'title': '青蛙跳',
            'desc': '跳躍次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:jump'])
    ))
