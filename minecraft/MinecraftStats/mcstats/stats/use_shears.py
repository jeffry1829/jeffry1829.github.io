from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_shears',
        {
            'title': '剪刀手',
            'desc': '剪刀使用次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:shears'])
    ))
