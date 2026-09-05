from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_soup',
        {
            'title': '湯品愛好者',
            'desc': '喝過的湯/濃湯數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:mushroom_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:beetroot_soup']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit_stew']),
        ])
    ))
