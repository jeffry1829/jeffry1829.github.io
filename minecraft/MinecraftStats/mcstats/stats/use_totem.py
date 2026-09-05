from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_totem',
        {
            'title': '九命怪貓',
            'desc': '不死圖騰使用次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:totem_of_undying'])
    ))
