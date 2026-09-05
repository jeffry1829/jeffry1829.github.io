from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_hoe',
        {
            'title': '農夫',
            'desc': '鋤地次數',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.+_hoe'])
    ))
