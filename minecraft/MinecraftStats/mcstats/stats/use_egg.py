from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_egg',
        {
            'title': '抓到了!',
            'desc': '丟擲雞蛋次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:egg'])
    ))
