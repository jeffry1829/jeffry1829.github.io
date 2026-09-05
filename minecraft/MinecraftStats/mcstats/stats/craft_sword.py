from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sword',
        {
            'title': '鐵匠',
            'desc': '製造的劍的數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_sword'])
    ))
