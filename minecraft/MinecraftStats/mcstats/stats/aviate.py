from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'aviate',
        {
            'title': '飛行員',
            'desc': '用鞘翅飛的距離',
            'icon': 'items/elytra.png',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:aviate_one_cm'])
    ))
