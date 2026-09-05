from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_campfire',
        {
            'title': '原始人',
            'desc': '使用營火的數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_campfire']),
        1921 # campfires added in 19w02a
    ))
