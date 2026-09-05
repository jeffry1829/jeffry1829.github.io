from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_cartography',
        {
            'title': '製圖師',
            'desc': '使用製圖台的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_cartography_table']),
        1921 # stonecutters usable since 19w02a
    ))
