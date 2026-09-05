from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_spawner',
        {
            'title': '快挖掉！',
            'desc': '挖掉的重生磚數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:spawner'])
    ))
