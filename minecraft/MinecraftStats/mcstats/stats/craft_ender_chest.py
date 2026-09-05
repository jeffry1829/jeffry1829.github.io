from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_ender_chest',
        {
            'title': '破壞這個！',
            'desc': '製造的終界箱數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:ender_chest']),
    ))
