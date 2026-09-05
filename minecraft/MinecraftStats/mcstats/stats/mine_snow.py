from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_snow',
        {
            'title': '鏟雪機',
            'desc': '清除的雪的數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:snow']),
            mcstats.StatReader(['minecraft:mined','minecraft:snow_block']),
        ])
    ))
